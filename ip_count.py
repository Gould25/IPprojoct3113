#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: python script for retrieving and collecting IP addresses
                and meta data from apache2 server requests logs

'''

from functions import *

def main():

    start = time.perf_counter()

    dirs = [created_logs_dir, stats_ip_count, stats_location]

    clean_dirs = [created_logs_dir, stats_ip_count, stats_location]

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--type',
                        help="""choices = [clean cron normal]:
                            clean -> Deletes all Created and Data directories;
                            cron ->  output to a log file;
                            info -> only info tags to terminal;
                            warn -> warn and up output to terminal;
                            default -> info""",
                        default='info')

    args = parser.parse_args()


    if args.type == 'info' or args.type == 'cron' \
                             or args.type == 'warn' \
                              or args.type == 'debug':

        if args.type == 'cron':
            logging.basicConfig(filename=cron_log, level=logging.DEBUG)
        elif args.type == 'info':
            logging.basicConfig(level=logging.INFO)
        elif args.type == 'warn':
            logging.basicConfig(level=logging.WARN)
        else:
            logging.basicConfig(level=logging.DEBUG)

        set_up_env(dirs)

        parse_lin_logs()

        parse_win_logs()

        figure_stats()

    elif args.type == 'clean':
        logging.basicConfig(level=logging.DEBUG)

        scrub_data(clean_dirs)

    logging.info("This run took %s seconds" % round(time.perf_counter()-start,4))

if __name__ == "__main__":
    main()
