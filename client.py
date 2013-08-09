#!/usr/bin/python

from statsd import StatsClient
import os

statsd = StatsClient(host='metrics.ccs.neu.edu')

if os.getenv('PAM_TYPE') == 'open_session':
  statsd.incr('ccs.linux.102.logins')
else:
  statsd.decr('ccs.linux.102.logins')

