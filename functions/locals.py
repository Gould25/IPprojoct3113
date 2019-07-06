#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@author: Jeff Gould

@description: file operation functions for black lists.
'''

#from functions import var
from functions import *


def find_location(server):

    uni_ip = server + '_uni_ip.csv'
    uni_locations_whois = server + locations_whois

    fip = os.path.join(created_logs_dir, uni_ip)
    locate_whois = os.path.join(created_logs_dir, uni_locations_whois)
    location_whois = pd.DataFrame(columns=['IP', 'Country', 'Description',
                                            'Registry', 'Attempts'])
    loc = []

    try:
        with open(fip, 'r') as ip_cnt:
            read = csv.reader(ip_cnt)
            next(read, None)
            ips = list(read)

        for i, ip in enumerate(ips):
            loc = ip[0]
            logging.info("Whois is looking up IP address: %s" % loc)
            try:

                ipw = IPWhois(loc)

                results = ipw.lookup_whois(inc_nir=True, retry_count=1)
                locw = [ip[0], results['asn_country_code'],
                                results['asn_description'],
                                results['asn_registry'],
                                ip[1]]

                location_whois.loc[i] = locw

            except Exception as e:
                logging.error('From Ip lookup' + str(e))

        location_whois.to_csv(locate_whois, index=False)
        logging.info("Created csv file: %s" % locate_whois)

    except Exception as e:
        logging.error('From find_location()' + str(e))
