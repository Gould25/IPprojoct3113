#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: house keeping functions for directory and file creation and
    deletion.
'''

from functions import *

def set_up_env(dir):

    for d in dir:
        create_dir(d)

    #create_files()

def create_dir(dir):

    if not os.path.exists(dir):
        try:
            os.mkdir(dir)

            logging.info("From create_dir() The Directory (%s) " +
                                "has Been Created.", dir)

        except Exception as e:
            logging.error("From create_dir()" + e)


    else:
        logging.info("From create_dir() The Directory (%s) already exists.", dir)

def create_files():

    bl = os.path.join(black_list_dir, black_list_file)
    wt = os.path.join(black_list_dir, white_list_file)

    try:

        if not os.path.exists(bl):

            black = pd.DataFrame(columns=['IP'])
            black.loc['IP'] = gateway_ip
            black.to_csv(bl, index=False)
            logging.info("From create_files() The File (%s) " +
                            "has Been Created.", bl)
        else:
            logging.info("From create_files() The File (%s) already exists.", bl)

        if not os.path.exists(wt):

            white = pd.DataFrame(columns=['IP'])
            white.loc['IP'] = gateway_ip
            white.to_csv(wt, index=False)
            logging.info("From create_files() The File (%s) " +
                            "has Been Created.", wt)
        else:
            logging.info("From create_files() The File (%s) already exists.", wt)

    except Exception as e:
        logging.error("From create_files()" + str(e))


def scrub_data(dir):
    for d in dir:
        remove_data(d)

def remove_data(dir):

    if os.path.exists(dir):

        input("Warning You ARE About To DELETE All of " +
                "Your Data !!!!!! Hit Enter to confirm")

        try:
            if shutil.rmtree(dir):
                logging.info("From remove_data() " +
                                "The Directory % has Been Deleted.", dir)

        except Exception as e:
            logging.error("From remove_data()" + e)
    else:
        logging.info('There is nothing to clean up')
