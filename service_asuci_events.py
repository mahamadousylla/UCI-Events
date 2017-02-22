from lxml import html
from flask import Flask
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_asuci_events():
    list_of_events = []
    
    url = 'http://www.asuci.uci.edu/'
    page = requests.get(url)
    
    
    tree = html.fromstring(page.content)
    

    dates = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/h3/text()')
    locations = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/h4/a/text()')
    times = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/span/text()')
    links = tree.xpath('//*[@id="post-13494"]/div/div/div/div[1]/div/ul/li/ul/li/h4/a/@href')
    
    print("dates", dates, len(dates))
    print("locations", locations, len(locations))
    print("times", times, len(locations))
    print("links", links)
       
    for i in range(len(dates)):     
        dict = {
     
            "date": dates[i].strip(),
            "location": locations[i],
            "time": times[i].strip(),
            "link": links[i].strip()
        }
         
        list_of_events.append(dict)

    return jsonify(data=list_of_events)


if __name__ == "__main__":
#     app.run(debug=True)
    app.run(host='0.0.0.0', port = 5000)