#!/usr/bin/env python3

import nitro-python

class net_auth():
    def __init__(self):
        self.user = ""
        self.password = ""
    
    def connect_netscaler(self)
        #Specify the NetScaler appliance IP address and protocol
        ns_session = nitro_service("http://","http")

        #Specify the login credentials
        ns_session.login(self.user, self.password, 3600)