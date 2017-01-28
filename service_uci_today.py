from WebCrawler import Spider
import csv
import datetime
from calendar import monthrange

#Events for the whole month
titles = [];
time = [];
descriptions = [];
location = [];
date = [];
now = datetime.datetime.now();

def FixEntries():
    for i in range(len(titles)):
        if titles[i] == 'Striking a Balance: Conservation and...':
            time.insert(i, 'x');

def list_update(update_list, crawler, path):
    crawler.parse(path);
    update_list += crawler.get_info();
    

#iterate from current day to the last day of the Month
for i in range(now.day, monthrange(now.year, now.month)[1]):
    url = 'https://today.uci.edu/calendar/day/2017/'+ str(now.month) + '/' + str(i);
    crawler = Spider(url)
    
    #Titles
    crawler.parse('//h3/a/text()');
    titles += crawler.get_info()[1:];
    
    #Locations
    list_update(location, crawler, '//*[@id]/div/div[3]/div[1]/div[2]/a/text()');

    #time
    list_update(time, crawler, '//*[@id]/div/div[3]/div[1]/div[1]/abbr/text()');

    #Event Description
    list_update(descriptions, crawler, '//*[@id]/div/h4/text()');

    #Date
    for k in range(len(crawler.get_info())):
        date.append(now.strftime('%B') + " {}, {}".format(i, now.year));
    
#Fix incomplete entries
FixEntries();

##print(len(location), len(titles), len(time), len(descriptions));
lowest = min(len(location), len(titles), len(time), len(descriptions));

##Write outputs to CSV file for Database
file = open("ucitoday.csv", 'w+', encoding = 'utf-8');
writer = csv.DictWriter(file, fieldnames = ['Titles', 'Locations', 'Date', 'Time', 'Description']);
writer.writeheader();
for i in range(lowest):
    writer.writerow({'Titles': titles[i], 'Locations': location[i], 'Time': time[i], 'Date': date[i], 'Description': descriptions[i]})
print("Writing output to CSV....");
print("Closing File....");
file.close();