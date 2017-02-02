from WebCrawler import Spider
import csv
from datetime import datetime as dt
from calendar import monthrange
from flask import jsonify
from json import dumps
import requests
from bottle import *

@get('/')
def process():
    print("starting...")
    titles = []
    time = []
    descriptions = []
    location = []
    date = []
    now = dt.now()
    #iterate from current day to the last day of the Month
    for i in range(now.day, now.day+2):
        url = 'https://today.uci.edu/calendar/day/2017/'+ str(now.month) + '/' + str(i)
        crawler = Spider(url)
        
        #Titles
        crawler.parse('//h3/a/text()')
        titles += crawler.get_info()[1:]
        
        #Locations
        crawler.parse('//*[@id]/div/div[3]/div[1]/div[2]/a/text()')
        location += crawler.get_info();
        

        #time
        crawler.parse('//*[@id]/div/div[3]/div[1]/div[1]/abbr/text()')
        time += crawler.get_info();

        #Event Description
        crawler.parse('//*[@id]/div/h4/text()')
        descriptions += crawler.get_info();

        #Date
        for k in range(len(crawler.get_info())):
            date.append(now.strftime('%B') + " {}, {}".format(i, now.year))

        for i in range(len(titles)):
            if titles[i] == 'Striking a Balance: Conservation and...':
                time.insert(i, 'x')
        
    master_list = list();
    ##print(len(location), len(titles), len(time), len(descriptions));
    lowest = min(len(location), len(titles), len(time), len(descriptions))

    for i in range(lowest):
        dicti = {
            "title": titles[i],
            "location": location[i],
            "time": time[i],
            "description": descriptions[i],
            "date": date[i]
            }
        master_list.append(dicti)
##    print(master_list)
    return '<pre>{}</pre>'.format(dumps(master_list, indent = 4, sort_keys = True))


if __name__ == '__main__':
    run(host = 'localhost', port = 8080);
##    app.run(debug=True)
