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
Sign up for an API key (https://solcast.com/)

Create a Rooftop entity on the Solcast website. This will generate a rooftop_id (resource id)
Copy the id and api for this integration to work