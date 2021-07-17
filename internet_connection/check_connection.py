#!/usr/bin/env python3

import socket

cloudflare_dns = "1.1.1.1"
conn = socket.socket()

def internet_conn():
    try:
        conn.connect((cloudflare_dns, 80))
        conn.close()
        return True

    except Exception as conn_error:
        print("There is no valid connection, please check your adaptor")
        return False