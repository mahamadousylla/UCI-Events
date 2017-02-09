from lxml import html
import requests
from lxml import html
from flask import Flask
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)



#Service Innovation UCI
@app.route("/", methods=['GET'])
def run_app():
    url = 'http://innovation.uci.edu/events/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    #date
    dates = tree.xpath('//*[@id]/h1/div/span/text()');
    dates = list(map(str.strip, dates));
    dates = [x for x in dates if x != '']
##    print(dates);
##    print(dates);


    #event titles
    titles = tree.xpath('//*[@id]/div[1]/h2/a/text()')
    titles = [s.encode('ascii', errors = 'ignore') for s in titles];
    titles = [s.decode() for s in titles];


    #Descriptions
    info = tree.xpath('//*[@id]/div[2]/div/text()')
    info = list(map(str.strip, info));
    info = (filter(None, info));
    info = [ s.encode('ascii' , errors = 'ignore') for s in info];
    info = [s.decode() for s in info];

    


    address = "The Cove @ UCI 5141 California Ave Irvine, CA 92617"

    master_list = [];

    for i in range(len(titles)):
        obj = {
            "title": titles[i].strip(),
            "date": dates[i].strip(),
            "location": address.strip(),
            "Info": info[i].strip()
            }
        master_list.append(obj);

    return jsonify(data = master_list);

if __name__ == "__main__":

    app.run(debug=True);
       
