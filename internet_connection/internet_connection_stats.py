#!/usr/bin/env python3

import speedtest
import logging
import check_connection as conn_check

stats = speedtest.Speedtest()

class internetConnection():
    def __init__(self):
        self.connection = conn_check.internet_conn()

    def isvalid(self):
        if(self.connection == True):
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.info('Internet connection check')
        else:
            exit(-1)

def connection_speed():
    
    #Create object
    internet_conn_exists = internetConnection()
    internet_conn_exists.isvalid()

    #Results
    download_speed = stats.download()
    upload_speed = stats.upload()
    ping = stats.results.ping
        
    #Combined results
    results = {
        "download": download_speed,
        "upload": upload_speed,
        "ping": ping
    }

    return results