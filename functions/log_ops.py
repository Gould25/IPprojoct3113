#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: log operation functions for black lists.
'''

from functions import *

def parse_lin_logs():

    for linlog in os.listdir(lin_log_location):

        lin_csv_file = linlog + '_raw_log.csv'

        log_path = os.path.join(lin_log_location, linlog)
        csv_out = os.path.join(created_logs_dir, lin_csv_file)

        clean_log = clean_logs(log_path, csv_out)

        split_by_date(clean_log, linlog)



def split_by_date(df, log):

    for i in range(3,stop_day):

        #print(i)
        fetch_date = datetime.date(2019,7,i)

        df_by_date = df[df['Date'] == fetch_date]

        #print(df_by_date)

        server = log + '_' + str(fetch_date)

        #print(server)

        file_ops(df_by_date, server)

        find_location(server)



def getlogs(log):

    try:

        if os.path.exists(data_dir):
            log_read = subprocess.run(log,
                                  timeout=1440,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
            if log_read.returncode:
                logging.error('From getlogs(): Error * log not read')

            else:
                logging.info("From getlogs(): The Log % has Been read.",
                                log[1])

        else:
            logging.error('From getlogs(): Directory %s does not exist',
                            data_dir)
            sys.exit('EXITING Log Files Not Read')

    except Exception as e:
        logging.error('From getlogs(): ' + str(e))

# read in log and clean up data frame
def clean_logs(log, server):

    headers = ['IP', 'D1', 'D2', 'Date', 'D3',
                'Options', 'Code', 'Bytes', 'M1', 'M2']

    try:
        raw_logs = pd.read_csv(log, sep=" ", header=None,
                                names=headers)
        logging.info('From clean_logs(): Log % has been Loaded to a Pandas DF',
                        log)

    except Exception as e:
        logging.debug(e)

    raw_logs.to_csv(server, index=False)

    raw_logs['Date'] = raw_logs['Date'].map(lambda x: str(x)[1:])
    raw_logs['Date'] = pd.to_datetime(raw_logs['Date'],
                                        format='%d/%b/%Y:%H:%M:%S') #:%H:%M:%S

    ip_strip = raw_logs[~raw_logs['IP'].astype(str).str.startswith(':')]

    ip_strip['Date'] = ip_strip['Date'].apply(lambda x: x.date())

    # strip all irrelvant columns
    stripped_log = ip_strip.drop(ip_strip.columns[[1, 2, 4, 8, 9]],
                                                    axis=1)

    logging.info('From clean_logs() Log %s has been cleaned and prepped ' % (log))

    return stripped_log
