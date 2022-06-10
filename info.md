### Changes

v3.0.5 beta
fixed 'this hour' amd 'next hour' sensor values
slow down the api polling if more than 1 rooftop to poll
fix first hour graph plot data
possibly RC1?? will see

v3.0.4 beta
bug fixes

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

