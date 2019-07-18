#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: python script for retrieving and collecting IP addresses
                and meta data from apache2 server requests logs

'''

from functions import *

def parse_win_logs():

    for winlog in os.listdir(win_log_location):

        win_csv_file = winlog + '_raw_log.csv'

        log_path = os.path.join(win_log_location, winlog)
        csv_out = os.path.join(created_logs_dir, win_csv_file)

        clean_log = clean_win_logs(log_path, csv_out)

        file_ops(clean_log, winlog)

        #find_location(winlog)


def clean_win_logs(log, csv):

    headers = ['Date', 'Time', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'IP',
                'Options', 'D10', 'Code', 'D13', 'D14', 'Bytes']


    with open(log, 'r') as f, open(csv, 'w') as fout:
        for row in f:
            if row[0].isdigit():
                fout.write(row)

    try:

        win_logs = pd.read_csv(csv, sep=" ", header=None, names=headers)
        logging.info('From clean_logs(): Log % has been Loaded to a Pandas DF',
                        log)

        win_logs.to_csv(csv, index=False)

    except Exception as e:
        logging.debug(e)
        win_logs = 'Didnt work'

    win_logs['Date'] = win_logs['Date'].map(lambda x: str(x)[1:])

    # strip all irrelvant columns
    stripped_log = win_logs.drop(win_logs.columns[[1, 2, 3, 4, 5, 6,
                                                    7, 10, 13, 14]], axis=1)

    #print(stripped_log)
    logging.info('From clean_logs() \nLog %s has been cleaned' % (log))


    return stripped_log
