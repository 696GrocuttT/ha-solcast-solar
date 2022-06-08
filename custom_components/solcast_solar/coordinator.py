"""The Airzone integration."""
from __future__ import annotations

from .solcastapi import SolcastApi

import logging
import traceback
from datetime import timedelta

import async_timeout
import homeassistant.util.dt as dt_util
from homeassistant.const import SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_track_utc_time_change
from homeassistant.helpers.sun import (get_astral_location,
                                        get_location_astral_event_next)
from homeassistant.helpers.update_coordinator import (DataUpdateCoordinator,
                                                        UpdateFailed)




from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class SolcastUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the Airzone device."""

    def __init__(self, hass: HomeAssistant, solcast: SolcastApi) -> None:
        """Initialize."""
        self.solcast = solcast
        self._hass = hass
        self._auto_fetch_tracker = None
        self._starthour = 6
        self._finishhour = 19

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            #update_interval = timedelta(minutes=1)
        )


    async def _async_update_data(self):
        _LOGGER.debug("_async_update_data called")
        """Update data via library."""
        async with async_timeout.timeout(30):
            try:
                await self.update_forecast()
            except Exception as error:
                raise UpdateFailed(error) from error
            return self.solcast._data

    async def reset_api_counter(self, *args):
        try:
            await self.solcast.reset_api_counter()
        except Exception as error:
            _LOGGER.warn("Solcast - Error resetting API counter")

    async def setup(self):
        await self.setup_auto_fetch()
        async_track_utc_time_change(self._hass, self.reset_api_counter, hour=0, minute=0, second=0, local=False)

    async def setup_auto_fetch(self):
        try:
            _LOGGER.debug("Solcast - Registering API auto fetching hourly between sun up and sun set")
            location, elevation = get_astral_location(self._hass)
            next_setting = get_location_astral_event_next(
                location, elevation, SUN_EVENT_SUNSET, dt_util.utcnow()
            ) + timedelta(hours=1)
            
            self._finishhour= next_setting.astimezone().hour # already one hour ahead
            

            self._auto_fetch_tracker = async_track_utc_time_change(self._hass, self.update_forecast, minute=0, second=0, local=True)

            _LOGGER.debug("Solcast - API will only connect between the hours %s and %s and at midnight",self._starthour,self._finishhour)

        except Exception:
            _LOGGER.error("setup_auto_fetch: %s", traceback.format_exc())

    async def update_forecast(self,*args):
        """Update forecast state."""

        try:
            last_update = self.solcast.get_last_updated_datetime() + timedelta(seconds=3500)
            date_now = dt_util.now() #.replace(hour=0, minute=0, second=0, microsecond=0)
            if last_update < date_now:
                #
                date_now = dt_util.now().replace(hour=0, minute=0, second=0, microsecond=0)
                if last_update < date_now:
                    await self.solcast.force_api_poll()
                else:
                    _hournow = dt_util.now().hour
                    _LOGGER.debug(_hournow, self._starthour,  self._finishhour)
                    if _hournow == 0 or (_hournow > self._starthour and _hournow < self._finishhour):
                        await self.solcast.force_api_poll()
            else:
                _LOGGER.debug("Solcast - API poll called, but did not happen as the last update is less than an hour old")
            
            #self.async_set_updated_data(True)
            for update_callback in self._listeners:
                update_callback()

        except Exception:
            _LOGGER.error("update_forecast: %s", traceback.format_exc())

    async def service_event_update(self, *args):
        _LOGGER.debug("Solcast - Event called to force an update of data from Solcast API")
        await self.solcast.force_api_poll()
        for update_callback in self._listeners:
                update_callback()

    def get_energy_tab_data(self):
        return self.solcast.get_energy_data()

    def get_sensor_value(self, key=""):
        if key == "total_kwh_forecast_today":
            return self.solcast.get_total_kwh_forecast_today()
        elif key == "peak_w_today":
            return self.solcast.get_peak_w_today()
        elif key == "peak_w_time_today":
            return self.solcast.get_peak_w_time_today()
        elif key == "forecast_this_hour":
            return self.solcast.get_forecast_this_hour()
        elif key == "forecast_next_hour":
            return self.solcast.get_forecast_next_hour()
        elif key == "total_kwh_forecast_tomorrow":
            return self.solcast.get_total_kwh_forecast_tomorrow()
        elif key == "peak_w_tomorrow":
            return self.solcast.get_peak_w_tomorrow()
        elif key == "peak_w_time_tomorrow":
            return self.solcast.get_peak_w_time_tomorrow()
        elif key == "get_remaining_today":
            return self.solcast.get_remaining_today()
        elif key == "api_counter":
            return self.solcast.get_api_used_count()
        elif key == "lastupdated":
            return self.solcast.get_last_updated_datetime()

        #just in case
        return None

    def get_sensor_extra_attributes(self, key=""):
        if key == "total_kwh_forecast_today":
            return self.solcast.get_forecast_today()
        elif key == "total_kwh_forecast_tomorrow":
            return self.solcast.get_forecast_tomorrow()

        #just in case
        return None

    def get_site_value(self, key=""):
        return self.solcast.get_rooftop_site_total_today(key)

    def get_site_extra_attributes(self, key=""):
        return self.solcast.get_rooftop_site_extra_data(key)


