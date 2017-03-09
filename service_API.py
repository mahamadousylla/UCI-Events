from flask import *
from flask_restful import *
import service_inov_uci as uci_inov
import service_uci_sports as uci_sports
import service_uci_today as uci_today

app = Flask(__name__);
api = Api(app)


class Master(Resource):
	def __init__(self):
		innovate = uci_inov.run_app();
		ucitoday = uci_today.process();

    def get_innovate(self):
        #This Format
        return jsonify(UCI_Innovaion = innovate);

    def get_ucitoday(self):
    	return jsonify(UCI_Today = ucitoday);

api.add_resource(Master, '/');

if __name__ == '__main__':
    app.run()
