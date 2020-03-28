# activity-tracker

### To Install
```
git clone https://github.com/danitamm/activity-tracker.git
cd activity-tracker
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

### To Use
1. `python tracker.py` to begin tracking session

2. Work!

3. <kbd>Ctrl</kbd>+<kbd>C</kbd> while Terminal is selected to end tracking session
4. `python report.py` to see the data

### Website Time Use Metrics
1. Time with website open in broswer. The downside of this metric is that it assigns high weights to websites that a user has open all day but does not use. For example, if one leaves a tab with their nytimes.com open all day (say, 8 hours), this website will be at least tied for the highest value of this metric *regardless of whether the user interacts with it*. Further, if one visits stackoverflow.com/ 10 times, closing the tab after 6 minutes each time, then by this metric stackoverflow will have 1/8 of the value of the nytimes page *that the user never actually used*.
2. Number of times a webpage on the domain was opened, including duplicates. A better measure of *active usage* because it avoids the problem described in the previous point. 
3. Time with website as active window. The best metric of the three, but active window tracking is not currently supported by this program. 

We will use metric 2.

### Data Report
The data storage was designed to be used in a wide variety of ways. Currently, it shows a a bar chart for both use metrics. It prints the time spent on each domain. For each domain, it prints the title of the web page on which the user spent the most time, and the amount of time spent. 

### Data Storage
The data is stored with .json format in nested dictionaries with depth 3. 

Each web domain's data (root dictionary):
```domain_dictionary = {domain : (path_dictionary, time_intervals)}```

Each path's data dictionary:
```path_dictionary = {path : (entry_dictionary, time_intervals)}```

Data dictionary (leaf dictionary):
```entry_dictionary = {'title' : <webpage title>, 'time' : <time first opened>, 'domain' : <web domain>, 'path' : <web path>}```

Time intervals' structures:  `time_interval = [[<first time opened>, <first time closed>], [<second time opened>, <second time closed>], ...]`

### Troubleshooting
When Firefox is running it stores the current session's information a lz4 compressed json file. The program contained in this repo relies entirely on the data contained in this file. In the program, the Firefox filepath was written with regex matching (shown below) to take into account the fact that the filepath can vary slightly between machines. 

If the regex matching is unsuccessful you'll receive a 'Firefox file not found' AssertionError, and you'll have to find the filepath and enter it in the Tracker class `__init__` method yourself. To find the filepath, look through your files while keeping in mind that it should approximately match the regex pattern. If you can't find the filepath, this likely means you have an earlier version of Firefox that is not compatible with this program. 

> Filepath regex: '~/.mozilla/firefox/\*default/''sessionstore-backups/recovery.json\*'

So far I've only run this on my laptop. I have a 64-bit Ubuntu 18.04 and Firefox 70.0.

### Notes
Firefox writes to the json file with a delay of up to 5 seconds, so this function may miss tabs that were opened and closed within that time span. 

### TODO
  * Introduce a concurrent active window tracking function. 
  * Create more detailed reports. 
