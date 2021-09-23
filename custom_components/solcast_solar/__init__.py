"""The Solcast Solar integration."""
from __future__ import annotations

from datetime import datetime, timedelta, date
import logging

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .pv_power_forecasts import PvPowerForecasts

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_BASE_URL = 'https://api.solcast.com.au/'

from .const import (
    CONF_APIKEY,
    CONF_AZIMUTH,
    CONF_TILT,
    CONF_EFFICIENCYFACTOR,
    CONF_CAPACITY,
    DOMAIN,
)

PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Solcast Solar from a config entry."""

    session = async_get_clientsession(hass)

    forecast = PvPowerForecasts(session=session,
                                latitude=entry.data[CONF_LATITUDE],
                                longitude=entry.data[CONF_LONGITUDE],
                                capacity=entry.options[CONF_CAPACITY],
                                api_key=entry.options[CONF_APIKEY],
                                tilt=(entry.options[CONF_TILT]),
                                azimuth=(entry.options[CONF_AZIMUTH] - 180),
                                efficiencyfactor=(entry.options[CONF_EFFICIENCYFACTOR] / 100),
    )
    
    # update interval. 
    update_interval = timedelta(hours=2)

    coordinator: DataUpdateCoordinator = DataUpdateCoordinator(
        hass,
        logging.getLogger(__name__),
        name=DOMAIN,
        update_method=forecast.estimate,
        update_interval=update_interval,
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_update_options))

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok

async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update options."""
    await hass.config_entries.async_reload(entry.entry_id)



