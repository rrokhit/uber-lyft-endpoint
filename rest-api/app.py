import UbervLyft
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class uberVLyft(Resource):
    def get(self,pickup,destination):
        return{'data':UbervLyft.combined(pickup,destination)}

api.add_resource(uberVLyft, '/getfareprices/<pickup>/<destination>')

if __name__ == '__main__':
    app.run()
