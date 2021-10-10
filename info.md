{% if installed %}
### Breaking Changes

Any previous integration setup must be deleted and re-created. So many things have been changed in this version that it just isnt possible to be backward compatible
### Changes

- Stores forecast data so if HA is restarted the API is not polled using up the API Limit.
- New sensor 'States' items
- Sensor states updated in HA every hour
- If API limit reached it just uses the last saved data
- Polls the Forecasts API only during the hours of 5am - 7pm ( 0500 - 1900)
- Polls the Actuals API for acturate forecasts at 1000, 1200, 1400, 1600, and 1900 hours

### Polling Imformation

Solcast has a 50 API poll limit per day.

Integrations with a poll interval hour time of 1:
Each created Integration will poll the API a total of 20 times.
If you have two rooftop items created within Solcast this would poll the API 40 times a day.
If you have more than 2 rooftop items created and within HA setting the Interval Hours greater than 1 will help.