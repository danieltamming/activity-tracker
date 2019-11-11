# activity-tracker

### How It Works On My Machine (and Will It Work On Yours?)
When Firefox is running it stores the current session's information a lz4 compressed json file. This program relies entirely on its ability to process the data contained in this file. The program's filename was written with regex matching to take into account the fact the filepath can vary slightly between machines. If the regex matching is unsuccessful you'll receive a 'Firefox file not found' AssertionError, and you'll have to enter your filename in the Tracker class `__init__` method yourself. 

So far I've only run this on my laptop. I have a 64-bit Ubuntu 18.04 and Firefox 70.0.

### How To Run
1. Clone the repository and create a virtual environment with all the packages in requirements.txt installed.
2. `python tracker.py` to begin your daily tracking session.
3. Work!
4. <kbd>Ctrl</kbd>+<kbd>C</kbd> to safely end the day's tracking session. 
5. `python report.py` to display the information from that session. 

### Data Report
The data storage was designed to be used in a wide variety of ways. Currently, it shows a pie chart representing the time spent on each web domain. It prints the time spent on each domain. For each domain, it prints the title of the web page on which the user spent the most time, and the amount of time spent. 

### Data Storage
The data is stored in nested dictionaries with depth 3. 

Each web domain's data (root dictionary):
```domain_dictionary = {domain : (path_dictionary, time_intervals)}```

Each path's data dictionary:
```path_dictionary = {path : (entry_dictionary, time_intervals)}```

Data dictionary (leaf dictionary):
```entry_dictionary = {'title' : <webpage title>, 'time' : <time first opened>, 'domain' : <web domain>, 'path' : <web path>}```

Time intervals' structures:  `time_interval = [[<first time opened>, <first time closed>], [<second time opened>, <second time closed>], ...]`

### Notes
Firefox writes to the json file with a delay of up to 5 seconds, so this function may miss tabs that were opened and closed within that time span. 

### TODO
Introduce a concurrent active window tracking function. 
