## Metrics3

Metrics is a project used to collect arbitrary data from machines. The primary
use case for this is knowing how many people use the lab machines over time.

## The Stack

We are using statsd as an endpoint for any services to send data to.

Statsd is going to store this data into couchdb.

We can visualize this data by performing mapreduce jobs on couchdb and sending
to some graphing library, such as highcharts.js or graphite.

## Clients

We can track lab machine usage by using a script that will increment or
decrement a counter upon login and logout.

## Notes

Graphite is provided by
puppet module install garether/graphite

Statsd needs to be installed through NPM which will need puppetlabs/nodejs for a provider

puppet module install puppetlabs/nodejs

# Finish this later
