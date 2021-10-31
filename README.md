# Solcast Solar 

Home Assistant(https://www.home-assistant.io/) Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This custom component integrates the Solcast API into Home Assistant.

Modified from the great works of
* dannerph/homeassistant-solcast
* cjtapper/solcast-py
* home-assistant-libs/forecast_solar
## Basic Installation/Configuration Instructions:
Add a new HA Integration selecting 'Solcast PV Solar'

Setup the Recorder to record data.. something like
```
recorder:
  purge_keep_days: 31
  include:
    entity_globs:
      - sensor.solcast*
```

![integration](https://user-images.githubusercontent.com/1471841/135556342-bd92b717-61ee-4dcd-95ed-2694714489bf.png)

#### Getting a Solcast API Key:
Sign up for an API key (https://solcast.com/)

Create a Rooftop entity on the Solcast website. This will generate a rooftop_id (resource id)
Copy the id and api for this integration to work.

![img1](https://user-images.githubusercontent.com/1471841/135556872-ff5b51ac-699e-4ea5-869c-f9b0d0c5b815.png)
![img2](https://user-images.githubusercontent.com/1471841/135556549-1cdd1621-9351-43d2-85d1-cb335f0b77ba.png)
