'''
Created on Mar 22, 2016

@author: msim
'''

'''
Provides a REST API that returns a JSON
representation of log file records.
'''

from pyramid.view import view_config, view_defaults
from configparser import ConfigParser
import os

@view_defaults(renderer='json', route_name='log')
class LogView:
    
    def __init__(self, request):
        self.request = request
        config = ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), '../hydroconfig.ini'))
        logfile = config.get('logging', 'logfile')
        self.logfile = os.path.join(os.path.dirname(__file__), '../logs/', logfile)
        self.record_cnt = request.matchdict['record_cnt']

    @view_config(request_method='GET')
    def read_log(self):
        # Should check to see if logfile actually exists before trying to open it
        print('LogView.read_log: Reading data from file', self.logfile)
        with open(self.logfile, 'r') as infile:
            # put code to read record_cnt lines from the file here
            the_data = infile.readlines()
            return {'the_data': the_data}