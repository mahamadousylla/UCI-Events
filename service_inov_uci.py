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
##    print(info);
    #streets
    street = tree.xpath('//*[@id="post-1138"]/div[1]/div/div/div/address/span/span[1]/text()')[0]

    #location
    uci_loc = tree.xpath('//*[@id="post-1138"]/div[1]/div/div/div/address/span/span[1]/text()')[0]

    #the cover
    cover = tree.xpath('//*[@id="post-1138"]/div[1]/div/div/div/text()')[0]

    #city 
    city = tree.xpath('//*[@id="post-1138"]/div[1]/div/div/div/address/span/span[2]/text()')[0]

    #state
    state = tree.xpath('//*[@id="post-1138"]/div[1]/div/div/div/address/span/abbr/text()')[0]

    #zip code
    zip_code = tree.xpath('///*[@id="post-1138"]/div[1]/div/div/div/address/span/span[3]/text()')[0]


    address = cover.strip() + ", " + street.strip() + ", " +  city.strip() + " "  + state.strip() + " " +  zip_code.strip();

    master_list = [];

    for i in range(len(titles)):
        obj = {
            "title": titles[i].strip(),
            "date": dates[i].strip(),
            "location": address.strip(),
            "eventInfo": info[i].strip()
            }
        master_list.append(obj);

    return jsonify(data = master_list);

if __name__ == "__main__":
    app.run(debug=True);
    run_app();    
