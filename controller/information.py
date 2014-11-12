__author__ = 'Administrator'
from datetime import datetime
from base import *
from model.column import Information
from flask_restful_swagger import swagger

class InformationBase(Base):
    def __init__(self):
        Base.__init__(self, Information)

    def to_dict(self, information):
        return dict(id = information.id, article = information.article, introduction = information.introduction, \
            picture = information.picture, title = information.title, create_time = str(information.create_time), \
            update_time = str(information.update_time))

    def update(self, information, request_data):
        information.article = request_data['article']
        information.introduction = request_data['introduction']
        information.picture = request_data['picture']
        information.title = request_data['title']
        information.update_time = datetime.now()

    def insert(self, request_data):
        information = Information(request_data['article'], request_data['introduction'], request_data['picture'], \
            request_data['title'])
        return information


class Informations(InformationBase, Bases):
    @swagger.operation(
        notes = 'Get all/an information',
        parameters=[
            {
                "name": "id",
                "description": "An information id, put 0 can get all information",
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
    def get(self, id):
        try:
            a = Bases.get(self,id)
        except Exception as ex:
            print ex
        return a


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
        return Bases.delete(self, id)

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
        return Bases.put(self, id)


class InformationPages(InformationBase, BasePage):
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
        return BasePage.get(self, page, size)


class InformationAdd(InformationBase, BaseAdd):
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
        return BaseAdd.post(self)