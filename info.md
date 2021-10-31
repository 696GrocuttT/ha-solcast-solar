### Breaking Changes

Complete re write. v2.0 now 
- uses recorder to save forecast data, api count, last api call datetime


### Changes

- Lots
- New service call function for update forecasts and delete all forecast data
- saves forecast data into the DB
- limit api calls setting
- much much more

### Polling Imformation

Solcast has a 50 API poll limit per day.

You can set the total number of api polls for each day in the integration settings
You can also use the service items to call updates manually or using an automation or script
