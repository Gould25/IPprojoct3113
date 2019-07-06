#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: edit all variables here to customize black lists.
'''

#number of previous days to use from logs
#num_days = 20

# day to split linux logs to add 1 for indexing
stop_day = 6

##### Directory Variables (Temp Directories are deleted on clean run)

# Temp directory created to store server logs
#data_dir='data'

# Temp directory created to store tempoarary logs
created_logs_dir = 'created_logs'

# Directory to store windows log files
win_log_location='win_data/'

# Directory to store linux log files
lin_log_location='lin_data/'

# log file and directory for cron job logs
cron_log = 'IP_log'

###### File Variables

### Following files will be deleted on a clean run

# File for full log after stripping irrelevant columns and IP's
full_log = '_full_log.csv'

# file for a count of attempts from a unique IP address
ip = '_uni_ip.csv'

# File for list of "OK" code 200 requests
ok = '_ok.csv'

# File for rejected code 404
reject = '_code_404.csv'

# file for a locations of IP address
locations_whois = '_locations_whois.csv'
