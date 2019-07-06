#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: file operation functions for black lists.
'''

#from functions import var
from functions import *




def file_ops(df, server):

    named_full_log = server + full_log
    named_ip = server + ip
    named_ok = server + ok
    named_reject = server + reject
    flog = os.path.join(created_logs_dir, named_full_log)
    fip = os.path.join(created_logs_dir, named_ip)
    fok = os.path.join(created_logs_dir, named_ok)
    freject = os.path.join(created_logs_dir, named_reject)

    try:
        # create csv of all relevant columns
        df.to_csv(flog, index=False)

        # create csv of unique Ip address' and the frequency they appear
        ip_count = pd.DataFrame(columns=['IP', 'Frequency'])
        ip_count.IP = df.IP
        ip_count = ip_count.groupby('IP').agg({'Frequency': len})
        ip_count = ip_count.sort_values(by=['Frequency'], ascending=False)

        ip_count.to_csv(fip, index=True)

        # create csv of all OK request code 200
        ip_ok = df.loc[df.Code == 200]
        ip_ok.to_csv(fok, index=False)

        # create csv of all rejected request not code 200
        ip_rej = df.loc[df.Code != 200]
        ip_rej.to_csv(freject, index=False)

        logging.info("From file_ops() CSV's have been Created")


    except Exception as e:
        logging.error('From file_ops()' + str(e))
