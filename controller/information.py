__author__ = 'Administrator'
import json
from flask.ext.restful import Resource
from flask import request
from model.column import Information
from model.db import ini_db
from flask_restful_swagger import swagger
from datetime import datetime
from util.response import rep

db = ini_db()

def to_dict(item):
    return dict(id = item.id, article = item.article, introduction = item.introduction, picture = item.picture, title = item.title, create_time = str(item.create_time), update_time = str(item.update_time))

class Informations(Resource):
    @swagger.operation(
        notes = 'Get all/an information',
        parameters=[
            {
                "name": "id",
                "description": "An information id, put 0 can get all information",
                "required": False,
                "allowMultiple": False,
                "dataType": int.__name__,
                "paramType": "path"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Request success"
            },
            {
                "code": 500,
                "message": "Request Error"
            }
        ]
    )
    def get(self, id):
        if id == 0:
            try:
                information = db.session.query(Information).order_by(Information.id.desc()).all()
                information = [to_dict(item) for item in information]
            except Exception as ex:
                return rep(500, ex.message), 500
        else:
            try:
                information = db.session.query(Information).get(id)
                information = to_dict(information)
            except Exception as ex:
                return rep(404, u'not fount : %s' % ex.message), 404


        return information



    @swagger.operation(
        notes = 'delete an information',
        parameters=[
            {
                "name": "id",
                "description": "An information id",
                "required": True,
                "allowMultiple": False,
                "dataType": int.__name__,
                "paramType": "path"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Request success"
            },
            {
                "code": 500,
                "message": "Request Error"
            }
        ]
    )
    def delete(self, id):
        information = db.session.query(Information).get(id)
        if information is None:
            return rep(404, u'not found'), 404

        try:
            db.session.delete(information)
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500

        return rep(200, u'delete information success')

    @swagger.operation(
        notes='Update a new information',
        parameters=[
            {
                "name": "id",
                "description": "An information id",
                "required": True,
                "allowMultiple": False,
                "dataType": int.__name__,
                "paramType": "path"
            },
            {
                "name": "body",
                "description": "An information item",
                "required": True,
                "allowMultiple": False,
                "dataType": Information.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Request success"
            },
            {
                "code": 500,
                "message": "Request Error"
            }
        ])
    def put(self, id):
        request_data = json.loads(request.data)

        try:
            information = db.session.query(Information).get(id)
        except Exception as ex:
             return rep(500, ex.message), 500

        if information is None:
            return rep(404, u'not found'), 404

        information.article = request_data['article']
        information.introduction = request_data['introduction']
        information.picture = request_data['picture']
        information.title = request_data['title']
        information.update_time = datetime.now()

        try:
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500

        return rep(200, u'update information success')


class InformationPages(Resource):
    @swagger.operation(
        notes = 'Get information for pages',
        nickname='get',
        parameters=[
            {
                "name": "page",
                "description": "information page number",
                "required": True,
                "allowMultiple": False,
                "dataType": 'string',
                "paramType": "path"
            },
            {
                "name": "size",
                "description": "information page size",
                "required": True,
                "allowMultiple": False,
                "dataType": 'string',
                "paramType": "path"
            }
        ],
        responseMessages=[
            {
              "code": 200,
              "message": "Request success"
            },
            {
              "code": 500,
              "message": "Request Error"
            }
        ]
    )
    def get(self, page, size):
        offset = page * size
        try:
            information_page = db.session.query(Information).order_by(Information.create_time.desc()).offset(offset).limit(size)
            information_page = [to_dict(item) for item in information_page]
        except Exception as ex:
            return rep(500, ex.message), 500

        return information_page


class InformationAdd(Resource):
    @swagger.operation(
        notes='Add a new information',
        parameters=[
            {
                "name": "body",
                "description": "An information item",
                "required": True,
                "allowMultiple": False,
                "dataType": Information.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Request success"
            },
            {
                "code": 500,
                "message": "Request Error"
            }
        ])
    def post(self):
        request_data = json.loads(request.data)
        information = Information(request_data['article'], request_data['introduction'], request_data['picture'], request_data['title'])

        try:
            db.session.add(information)
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500

        return rep(200, u'add information success')