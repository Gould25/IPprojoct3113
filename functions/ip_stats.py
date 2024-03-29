#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: run statistics on sorted csv's

'''

from functions import *

def figure_stats():

    print(" Figuring Statistics for IP's ")

    suffix = '_uni_ip.csv'

    copy_csv(created_logs_dir, stats_ip_count, suffix)

    suffix = '_locations_whois.csv'

    #copy_csv(created_logs_dir, stats_location, suffix)

    headers = ['Server', "Total_Count", "OK_request", "Other_requests", "Min", "Max", "Mean", 'Var', "Std_dev"]

    counts = []

    aggregate_results = pd.DataFrame(columns=headers)

    try:

        for file in os.listdir(stats_ip_count):
            sts = os.path.join(stats_ip_count,file)
            ok_file = file[0:16] + '_ok.csv'
            okcsv = os.path.join(created_logs_dir,ok_file)
            ok = pd.read_csv(okcsv, header=0)
            df = pd.read_csv(sts, header=0)
            counts = [file]
            counts.append(df['Frequency'].sum(axis=0))
            counts.append(ok.shape[0])
            counts.append(df['Frequency'].sum(axis=0) - ok.shape[0])
            counts.append(df['Frequency'].min(axis=0))
            counts.append(df['Frequency'].max(axis=0))
            counts.append(df['Frequency'].mean(axis=0))
            counts.append(df['Frequency'].var(axis=0))
            counts.append(df['Frequency'].std(axis=0))

            logging.info('%s has been summarized' % file)
            #logging.info(df['Frequency'].describe())

            aggregate_results.loc[len(aggregate_results)] = counts
    except Exception as e:
        logging.error('From figure_stats()' + str(e))
    aggregate_results = aggregate_results.sort_values(by="Server")
    aggregate_results = aggregate_results.reset_index(drop=True)


    aggregate_results.to_csv("count_stats.csv")

    #print(aggregate_results)
if __name__ == "__main__":
    figure_stats()
