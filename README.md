# Solcast Solar 

Home Assistant(https://www.home-assistant.io/) Component
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This custom component integrates the Solcast API into Home Assistant.

Modified from the great works of
* dannerph/homeassistant-solcast
* cjtapper/solcast-py
* home-assistant-libs/forecast_solar

![Demo](https://user-images.githubusercontent.com/1471841/134319252-aad9346a-d650-4172-9b7e-b2a215de1f15.png)

## Basic Installation/Configuration Instructions:
Add a new HA Integration selecting 'Solcast PV Solar'

#### Getting a Solcast API Key:
Sign up for an API key (https://www.home-assistant.io/)


#### Integration variables:
* **api_key**: Your API key from Solcast.
* **name**: a name for the integration
* **latitude**: default collected from home-assistant value
* **longtiude**: default collected from home-assistant value
* **azimuth**: The angle between a line pointing due north to the sun's current position in the sky. Negative to the East. Positive to the West. 0 at due North.
* **tilt**: The angle (degrees) that the PV system is tilted off the horizontal. Must be between 0 and 90
* **efficiency factor**: loss factor of the pv system. 0.0 -> 1.0. 0.6 your returned power will be a maximum of 60% of AC capacity.
* **pv system capacity**: your pv system inverter max power output in watts (7.5kw system is 7500).
