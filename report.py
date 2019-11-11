import sys
import os
import subprocess
import re
import time
from datetime import datetime, date, timedelta
import json

import matplotlib.pyplot as plt

def process_intervals(time_intervals):
	'''
	Closes open intervals and converts strings to datetime objects
	Returns sum of the intervals
	'''
	total_time = ZERO_TIME
	for interval in time_intervals:
		for i, time_str in enumerate(interval):
			if time_str is None:
				interval[i] = CUR_TIME
			elif isinstance(time_str, str):
				interval[i] = datetime.strptime(time_str, TIME_FORMAT)
		total_time += interval[1] - interval[0]
	return total_time

def process_paths_dict(paths_dict):
	max_entry_dict = None
	max_time_spent = ZERO_TIME
	for entry_dict, time_intervals in paths_dict.values():
		time_spent = process_intervals(time_intervals)
		if time_spent > max_time_spent:
			max_time_spent = time_spent
			max_entry_dict = entry_dict
	return max_entry_dict, max_time_spent

# CONSTANTS
todays_folder = os.path.join('data', str(date.today()))
record_filename = os.path.join(todays_folder, 'record.json')
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
CUR_TIME = datetime.now().replace(microsecond=0)
ZERO_TIME = CUR_TIME - CUR_TIME

with open(record_filename) as f:
	domains_dict = json.load(f)

labels = []
times = []

for domain, (paths_dict, domain_time_intervals) in domains_dict.items():
	time_spent = process_intervals(domain_time_intervals)
	print('Spent {} on {}.'.format(time_spent, domain))
	max_entry_dict, max_time_spent = process_paths_dict(paths_dict)
	print('Most time, {}, spent on page title | {}.'
		  '\n'.format(max_time_spent, max_entry_dict['title']))
	labels.append(domain)
	times.append(time_spent.total_seconds())

plt.pie(times, labels=labels)
plt.show()