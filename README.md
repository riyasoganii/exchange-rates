# exchange-rates
Creating functions in python by accessing the data of currency exchange rates from the open source website ​https://exchangeratesapi.io/​.

function getLatestRates returns a JSON string that is a response to a latest rates.

function changeBase takes the amount, original currency, desired currency and date and converts the amount of original currency to the desired currency on the specified date.

function printAscending prints sorted order of latest rates

function extremeFridays returns, in a given period, on which friday was currency the strongest and on which was it the weakest

function findMissingDates returns the dates that are not present when you do a json query from startDate to endDate
