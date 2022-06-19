# Solcast Solar 

Home Assistant(https://www.home-assistant.io/) Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

This custom component integrates the Solcast API into Home Assistant.

Modified from the great works of
* dannerph/homeassistant-solcast
* cjtapper/solcast-py
* home-assistant-libs/forecast_solar

## Solcast Requirements:
Sign up for an API key (https://solcast.com/)

Solcast may take up to 24hrs to apply the 50 API counter from the default 10.. give it time to work:)

Create Rooftop entities on the Solcast website with all the data about your solar panel setup.
Copy the API Key for use with this integration.
## Basic Installation/Configuration Instructions:
Add a new HA Integration selecting 'Solcast PV Solar'

If you have more than one Solcast account because you have more than 2 rooftop setups, enter both account API keys seperated by a comma

![img6](https://user-images.githubusercontent.com/1471841/174471090-4a9f84dd-3327-4db7-a7c0-14d68a150d27.png)

### Set up HA Energy Dashboard settings
Go to the HA>Settings>Dashboards>Energy 
Click the edit the Solar Production item you have created. 

![img4](https://user-images.githubusercontent.com/1471841/149643349-d776f1ad-530c-46aa-91dc-8b9e7c7f3123.png)

Click the Forecast option button and select the Solcast Solar option.. Click SAVE.. HA will do all the rest for you

![img5](https://user-images.githubusercontent.com/1471841/174471543-0833b141-0c97-4b90-a058-cf986e89bbce.png)

## HA Views:
### HA Energy Tab
![img1](https://user-images.githubusercontent.com/1471841/135556872-ff5b51ac-699e-4ea5-869c-f9b0d0c5b815.png)
![img2](https://user-images.githubusercontent.com/1471841/135556549-1cdd1621-9351-43d2-85d1-cb335f0b77ba.png)
![img3](https://user-images.githubusercontent.com/1471841/149643244-245c9a5a-cb0f-4de4-b641-631bcf7fe764.png)

### HA Solcast Integration Sensors
![img31](https://user-images.githubusercontent.com/1471841/174471633-4aa0bb1d-009e-4d33-9c41-f0b6489cb995.png)
