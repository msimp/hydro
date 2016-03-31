'''
Created on Mar 22, 2016

@author: msim
'''

from time import sleep, strftime
import random
from configparser import ConfigParser
import os

class DataLogger(object):
    
    def __init__(self):
        print('DataLogger: os.getcwd=', os.getcwd())
        config = ConfigParser()
        config.read('../hydroconfig.ini')
        self.logfile = '../logs/' + config.get('logging', 'logfile')
        print('DataLogger: logfile =', self.logfile)
        self.delaysecs = int(config.get('logging', 'delaysecs'))
        print('DataLogger: delaysecs =', self.delaysecs)
        
    def logdata(self):
        print('DataLogger: Writing data every', self.delaysecs, 'seconds to file', self.logfile)
        with open(self.logfile, 'w') as outfile:
            while True:
                now = str(strftime('%X'))
                rand = str(random.randint(1, 1000))
                line = now + ': ' + rand + '\n'
                print('.', end="", flush=True)
                outfile.write(line)
                outfile.flush()
                sleep(self.delaysecs)
                
if __name__ == '__main__':
    # DataLogger anonymous object instantiation
    DataLogger().logdata()
