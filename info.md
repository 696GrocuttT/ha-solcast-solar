### Changes

v3.0.7
- **users upgrading from v3.0.5 or lover, need to delete the 'solcast.json' file in the HA>config directory to stop any errors**
- renamed sensors with the prefix "solcast_" to help naming sensors easier
- ** you will get double ups of the sensors in the integration because of the naming change. these will show greyed out in the list or with the values like unknown or unavailable etc.. just delete these old sensors one by one from the integration **

v3.0.6
- **users upgrading from v3.0.x need to delete the 'solcast.json' file in the HA>config directory**
- fixed lots of little bugs and problems.
- added ability to add multiple solcast accounts. Just comma seperate the api_keys in the integration config.
- remained API Counter to API Left. shows how many is remaining rather than used count.
- 'actual forecast' data is now only called once, the last api call at sunset. OR during integration install first run.
- forecast data is still called every hour between sunrise and sunset and once at midnight every day.
*Just delete the old API Counter sensor as its not used now*

v3.0.5 beta
- fixed 'this hour' amd 'next hour' sensor values.
- slow down the api polling if more than 1 rooftop to poll.
- fix first hour graph plot data.
- possibly RC1?? will see.

v3.0.4 beta
- bug fixes.

Complete re write. v3.0 now 
**Do not update this if you like the way the older version worked**
*There are many changes to this integration*

Simple setup.. just need the API key

- This is now as it should be, a 'forecast' integration (it does not graph past data *currently*)
- Forecast includes sensors for "today" and "tomorrow" total production, max hour production and time.. this hour and next production
- Forecast graph info for the next 7 days of data available

Integration contains
  - API Counter             (int)
  - API Last Polled         (date/time)
  - Forecast Next Hour      (Wh)
  - Forecast This Hour      (Wh)
  - Forecast Today          (kWh) (Attributes calculated from 'pv_estimate')
  - Forecast Tomorrow       (kWh) (Attributes calculated from 'pv_estimate')
  - Peak Forecast Today     (Wh)
  - Peak Forecast Tomorrow  (Wh)
  - Peak Time Today         (date/time)
  - Peak Time Tomorrow      (date/time)

![demo](https://user-images.githubusercontent.com/1471841/172541966-cb3f84a9-66bd-4f0f-99de-6d3e52cfd2ba.png)



### Polling Imformation
Solcast has a 50 API poll limit per day.

