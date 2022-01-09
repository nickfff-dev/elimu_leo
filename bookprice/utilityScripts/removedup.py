import json
import sys
from collections import OrderedDict
import csv
import os


with open('E:/books/bookprice/rawdata_TBC.json') as json_data:
    data = json.load(json_data)
    for element in data: 
        element.pop('image_urls', None)
        element.pop('images',   None)
    with open('E:/books/bookprice/rawdata_TBC_noimage.json', 'a') as outfile:
        json.dump(data, outfile, indent=4)
        
    

        # write clean data to new json file
        # with open('E:/books/bookprice/clean_TBC.json', 'a') as outfile:
        #     # add commas to separate new jsonvalues
        #     # remove lines with no data
        #     json.dump(element, outfile, indent=4, separators=(',', ': '))
        #     outfile.write('\n')