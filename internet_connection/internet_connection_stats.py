#!/usr/bin/env python3

import socket
import json
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

def connection_speed(*args, **kwargs):
    
    #Create object
    internet_conn_exists = internetConnection()
    internet_conn_exists.isvalid()

    #Optional parameters
    check_for = kwargs.get('check_for', None)

    #Results
    download_speed = stats.download()
    upload_speed = stats.upload()
    ping = stats.results.ping

    if(check_for == 'ping'):
        return f'Ping: {ping}'

    elif(check_for == 'download'):
        return f'Download: {download_speed}'
    
    elif(check_for == 'upload'):
        return f'Upload: {upload_speed}'
        
    #Combined results
    results = {
        "download": download_speed,
        "upload": upload_speed,
        "ping": ping
    }

    return results

if __name__ == "__main__":
    connection_speed()