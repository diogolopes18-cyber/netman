#!/usr/bin/env python3

import platform
import os
import subprocess

def check_os() -> str:

    operating_system = platform.system()

    if(operating_system == "Linux"):
        #Check distribution
        return platform.linux_distribution()
    
    elif(operating_system == "Windows"):
        return platform.release()
    
    elif(operating_system == "MacOS"):
        return platform.release()

def restart_interface():
    dist = check_os()

    if(dist[0] == "Ubuntu" or dist[0] == "Debian"):
        subprocess.call("./shell/restart_interface.sh", shell=True)
    
    elif(dist == "Windows"):
        print("In test")