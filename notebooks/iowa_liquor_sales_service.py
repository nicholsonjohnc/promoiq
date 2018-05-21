import os
from sodapy import Socrata

class IowaLiquorSalesService(object):
    
    def __init__(self):
        self.PREFIX = 'https://'
        self.DOMAIN = 'data.iowa.gov'
        self.DATASET_IDENTIFIER = 'spsw-4jax'
        self.APP_TOKEN = os.environ['APP_TOKEN']
        self.TIMEOUT = 60
        self.CONTENT_TYPE = 'csv'
        
    def query(self, query_string):
        '''
        Query Iowa Liquor Sales API.
        '''
        with Socrata(self.DOMAIN, self.APP_TOKEN, timeout=self.TIMEOUT) as client:
            return client.get(self.DATASET_IDENTIFIER, content_type=self.CONTENT_TYPE, query=query_string)
    
    def get_metadata(self):        
        with Socrata(self.DOMAIN, self.APP_TOKEN, timeout=self.TIMEOUT) as client:
            return client.get_metadata(self.DATASET_IDENTIFIER, content_type=self.CONTENT_TYPE)
