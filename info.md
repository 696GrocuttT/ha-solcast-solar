### Changes

v2.1.5
learnt some new ha api functions to make things nicer
move the forecast graph over by 30min. looks better now
some code clean up.. less messy

v2.1.4
got removed.. buggy

v2.1.3
forecast values for today and remaining today where not correct after the first api fetch

v2.1.2
Fixed the not updating every hour problem
Added a new event 'solcast_log_debug_data' to log out debug information 


v2.1.1
Better databasing of data
new events to control deleting all data and fetching all data

Complete re write. v2.0 now 
- uses recorder to save forecast data, api count, last api call datetime

Make sure that the Recorder setting in the configuration.yaml file include the solcast integration items.. something like
```
recorder:
  purge_keep_days: 31
  include:
    entity_globs:
      - sensor.solcast*
```


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
