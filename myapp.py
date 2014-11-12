from flask import Flask
from flask.ext.restful import Api
from controller.information import *
from controller.user import *
from flask_restful_swagger import swagger

app = Flask(__name__, static_folder='static')

###################################
api = swagger.docs(Api(app), apiVersion='0.1',
                   basePath='http://localhost:5000',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/api/spec',
                   description='K_Zone API')
###################################

api.add_resource(Informations, '/info/<int:id>')
api.add_resource(InformationPages, '/info/<int:page>/<int:size>')
api.add_resource(InformationAdd, '/info')

api.add_resource(Users, '/user/<int:id>')
api.add_resource(UserPages, '/user/<int:page>/<int:size>')
api.add_resource(UserAdd, '/user')

if __name__ == '__main__':
    app.run()