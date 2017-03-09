import requests
import urllib.request
import json
import pymysql as ms
from service_inov_uci import *
from service_uci_today import *
from service_uci_sports import *
from service_asuci_events import *
import service_inov_uci as uci_inov
import service_uci_sports as uci_sports
import service_uci_today as uci_today
import service_asuci_events as asuci
import time


def fill_sports(sportjson, tablename ):
	for i in range(len(sportjson)):
		cursor.execute("INSERT INTO {}(eventDate, location, opponent, score, eventTime) VALUES(%s, %s, %s, %s, %s)".format(tablename), (sportjson[i]["date"], sportjson[i]["location"], sportjson[i]["opponent"], sportjson[i]["score"], sportjson[i]["time"]));

start_time = time.time();
con = ms.connect(host = 'masisnguyen.com',user = 'masisng2_randy',passwd = '43351454',db = 'masisng2_randy_db')
cursor = con.cursor()
#creates a json obj list of dictionaries
innov_json = json.loads(innovate());
ucitoday_json = json.loads(process());
m_baskbl = json.loads(uci_sports.get_sport_schedules('m-baskbl'));
w_baskbl = json.loads(get_sport_schedules('w-baskbl'));
m_basebl = json.loads(get_sport_schedules('m-basebl'));
w_track = json.loads(get_sport_schedules('w-track'));
asuci_json = json.loads(asuci.get_asuci_events());

cursor.execute("DROP TABLE UCIToday");
cursor.execute("DROP TABLE Innovate");
cursor.execute("DROP TABLE m_baskl")
cursor.execute("DROP TABLE w_baskl")
cursor.execute("DROP TABLE m_baseball")
cursor.execute("DROP TABLE w_track")
cursor.execute("DROP TABLE asuci")
cursor.execute("CREATE TABLE IF NOT EXISTS m_baskl(eventDate TEXT(500), location TEXT(500), opponent TEXT(500), score TEXT(50), eventTime TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS w_baskl(eventDate TEXT(500), location TEXT(500), opponent TEXT(500), score TEXT(50), eventTime TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS m_baseball(eventDate TEXT(500), location TEXT(500), opponent TEXT(500), score TEXT(50), eventTime TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS w_track(eventDate TEXT(500), location TEXT(500), opponent TEXT(500), score TEXT(50), eventTime TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS asuci(eventDate TEXT(500), link TEXT(500), location TEXT(500), eventTime TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS Innovate(info TEXT(500), eventDate TEXT(500), location TEXT(500), title TEXT(500));");
cursor.execute("CREATE TABLE IF NOT EXISTS UCIToday(title TEXT(500), EventDate TEXT(500),  EventTime TEXT(500), location TEXT(500), info TEXT(500));");

for i in range(len(ucitoday_json)):
	cursor.execute("INSERT INTO UCIToday(title, EventDate, EventTime, location, info) VALUES(%s, %s, %s, %s, %s)", (ucitoday_json[i]['title'], ucitoday_json[i]['date'], ucitoday_json[i]['time'], ucitoday_json[i]['location'], ucitoday_json[i]['info']));

for i in range(len(innov_json)):
	cursor.execute("INSERT INTO Innovate(info, eventDate, location, title) VALUES(%s, %s, %s, %s)", (innov_json[i]['info'], innov_json[i]['date'], innov_json[i]['location'], innov_json[i]['title']));

fill_sports(m_baskbl, "m_baskl");
fill_sports(w_baskbl, "w_baskl");
fill_sports(m_basebl, "m_baseball");
fill_sports(w_track, "w_track");
for i in range(len(asuci_json)):
	cursor.execute("INSERT INTO asuci(eventDate, link, location, eventTime) VALUES( %s, %s, %s, %s)", (asuci_json[i]["date"], asuci_json[i]["link"], asuci_json[i]["location"], asuci_json[i]["time"]))

# cursor.execute("ALTER TABLE m_baskl MODIFY eventDate date");
# cursor.execute("ALTER TABLE asuci MODIFY eventDate date");
# cursor.execute("ALTER TABLE UCIToday MODIFY eventDate date");
# cursor.execute("ALTER TABLE Innovate MODIFY eventDate date");
# cursor.execute("ALTER TABLE w_baskl MODIFY eventDate date");
# cursor.execute("ALTER TABLE w_track MODIFY eventDate date");
# cursor.execute("ALTER TABLE m_baseball MODIFY eventDate date");



con.commit();
end_time = time.time() - start_time;
print("Time to update: {} seconds".format(end_time));
con.close()
