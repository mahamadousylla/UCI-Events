from lxml import html
import requests

# page = requests.get('http://www.ucirvinesports.com/sports/m-baskbl/2016-17/schedule')
# page = requests.get('http://www.ucirvinesports.com/sports/m-basebl/2016-17/schedule')
# page = requests.get('http://www.ucirvinesports.com/sports/m-soccer/2016-17/schedule')

# page = requests.get('http://www.ucirvinesports.com/sports/w-baskbl/2016-17/schedule')
# page = requests.get('http://www.ucirvinesports.com/sports/w-track/2016-17/schedule')
page = requests.get('http://www.ucirvinesports.com/sports/w-soccer/2016-17/schedule')


tree = html.fromstring(page.content)


dates = tree.xpath('//td[@colspan="6" or @class="e_date"]/text()')
opponents = tree.xpath('//span[@class="e_teamname e_opponent_name e_home" or @class="e_teamname e_opponent_name"]/text()')
locations = tree.xpath('//td[@class="e_notes"]/text()')
scores = tree.xpath('//td[@class="e_result"]/text()')
times = tree.xpath('//td[@class="e_status"]/text()')


for i in dates:
    if i == "\xa0":
        dates.remove(i)

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

list_of_games = []
current_month = ""
for i in range(len(opponents)):
    if dates[i].lower() in months:
        current_month = dates[i]
        dates = dates[0:i] + dates[i+1:]

    dict = {

        "month": current_month,
        "date": dates[i].strip(),
        "opponent": opponents[i],
        "location": locations[i],
        "score": scores[i].strip(),
        "time": times[i].strip()
    }  
    print(dict)
 
# print ('Dates: ', len(dates), dates)
# print ('Opponent: ', len(opponents), opponents)
# print ('Location: ', len(locations), locations)
# print ('Scores: ', len(scores), scores)
# print ('Time: ', len(times), times)