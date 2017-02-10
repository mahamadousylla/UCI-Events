from flask import *
from flask_restful import Resource, Api
import service_inov_uci as uci_inov
import service_uci_sports as uci_sports
import service_uci_today as uci_today

app = Flask(__name__);
api = Api(app)


class Master(Resource):
    def get(self):
        innovate = uci_inov.run_app();
        ucitoday = uci_today.process();
        return jsonify(UCI_Innovaion = innovate, UCI_Today = ucitoday);


api.add_resource(Master, '/');

if __name__ == '__main__':
    app.run()
