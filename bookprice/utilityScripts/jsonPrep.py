import json
import sys
from collections import OrderedDict
import csv
import os

# convert jsonlines to csv
# def jsonlines_to_csv(json_file, csv_file):
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#     with open(csv_file, 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(data[0].keys())
#         for row in data:
#             writer.writerow(row.values())







def clean_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


json_file = 'E:/books/bookprice/rawdata_TBC.json'
clean_json(json_file)

# jsonlines_to_csv('E:/books/bookprice/rawdata_TBC.json', 'E:/books/bookprice/csvFiles/tbcdata.csv')