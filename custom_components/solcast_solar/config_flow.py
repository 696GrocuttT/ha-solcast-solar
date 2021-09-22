"""Config flow for Solcast Solar integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.const import CONF_LATITUDE, CONF_LONGITUDE, CONF_NAME
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_APIKEY,
    CONF_AZIMUTH,
    CONF_TILT,
    CONF_EFFICIENCYFACTOR,
    CONF_CAPACITY,
    DOMAIN,
)


class SolcastSolarFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Solcast Solar."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> SolcastSolarOptionFlowHandler:
        """Get the options flow for this handler."""
        return SolcastSolarOptionFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initiated by the user."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data={
                    CONF_LATITUDE: user_input[CONF_LATITUDE],
                    CONF_LONGITUDE: user_input[CONF_LONGITUDE],
                },
                options={
                    CONF_APIKEY: user_input[CONF_APIKEY],
                    CONF_AZIMUTH: user_input[CONF_AZIMUTH],
                    CONF_TILT: user_input[CONF_TILT],
                    CONF_EFFICIENCYFACTOR: user_input[CONF_EFFICIENCYFACTOR],
                    CONF_CAPACITY: user_input[CONF_CAPACITY],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default=self.hass.config.location_name
                    ): str,
                    vol.Required(
                        CONF_LATITUDE, default=self.hass.config.latitude
                    ): cv.latitude,
                    vol.Required(
                        CONF_LONGITUDE, default=self.hass.config.longitude
                    ): cv.longitude,
                    vol.Required(
                        CONF_APIKEY, default=''
                    ): str,
                    vol.Required(CONF_AZIMUTH, default=180): vol.All(
                        vol.Coerce(int), vol.Range(min=0, max=360)
                    ),
                    vol.Required(CONF_TILT, default=23): vol.All(
                        vol.Coerce(int), vol.Range(min=0, max=90)
                    ),
                    vol.Required(CONF_EFFICIENCYFACTOR, default=0.9): vol.All(
                        vol.Coerce(float), vol.Range(min=0.1, max=1.0)
                    ),
                    vol.Required(CONF_CAPACITY, default=7500): vol.Coerce(int),
                }
            ),
        )


class SolcastSolarOptionFlowHandler(OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                { 
                    vol.Required(
                        CONF_APIKEY,
                        default=self.config_entry.options.get(CONF_APIKEY),
                    ): str,
                    vol.Required(
                        CONF_AZIMUTH,
                        default=self.config_entry.options.get(CONF_AZIMUTH),
                    ): vol.All(vol.Coerce(int), vol.Range(min=-0, max=360)),
                    vol.Required(
                        CONF_TILT,
                        default=self.config_entry.options[CONF_TILT],
                    ): vol.All(vol.Coerce(int), vol.Range(min=0, max=90)),
                    vol.Required(
                        CONF_EFFICIENCYFACTOR,
                        default=self.config_entry.options[CONF_EFFICIENCYFACTOR],
                    ): vol.All(vol.Coerce(int), vol.Range(min=0.1, max=1.0)),
                    vol.Required(
                        CONF_CAPACITY,
                        default=self.config_entry.options[CONF_CAPACITY],
                    ): vol.Coerce(int),
                }
            ),
        )