__author__ = 'Administrator'
from datetime import datetime
from base import *
from model.column import User
from flask_restful_swagger import swagger

class UserBase(Base):
    def __init__(self):
        Base.__init__(self, User)

    def to_dict(self, user):
        return dict(id = user.id, device_id = user.device_id, favorite = user.favorite, password = user.password, phone_number = user.phone_number, \
                    create_time = str(user.create_time), update_time = str(user.update_time), user_name = user.user_name, uuid = user.uuid,\
                 picture = user.picture)

    def update(self, user, request_data):
        user.favorite = request_data['favorite']
        user.password = request_data['password']
        user.picture = request_data['picture']
        user.update_time = datetime.now()

    def insert(self, request_data):
        user = User(request_data['device_id'], request_data['favorite'], request_data['password'], request_data['phone_number'], \
                    request_data['user_name'], request_data['uuid'] ,request_data['picture'])
        return user


class Users(UserBase, Bases):
    @swagger.operation(
        notes = 'Get all/an user',
        parameters=[
            {
                "name": "id",
                "description": "An user id, put 0 can get all user",
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
        return Bases.get(self,id)

    @swagger.operation(
        notes = 'delete an user',
        parameters=[
            {
                "name": "id",
                "description": "An user id",
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
        notes='Update a user',
        parameters=[
            {
                "name": "id",
                "description": "An user id",
                "required": True,
                "allowMultiple": False,
                "dataType": int.__name__,
                "paramType": "path"
            },
            {
                "name": "body",
                "description": "An user item",
                "required": True,
                "allowMultiple": False,
                "dataType": User.__name__,
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
        ]
    )
    def put(self, id):
        return Bases.put(self, id)


class UserPages(UserBase, BasePage):
    @swagger.operation(
        notes = 'Get user for pages',
        nickname='get',
        parameters=[
            {
                "name": "page",
                "description": "user page number",
                "required": True,
                "allowMultiple": False,
                "dataType": 'string',
                "paramType": "path"
            },
            {
                "name": "size",
                "description": "user page size",
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


class UserAdd(UserBase, BaseAdd):
    @swagger.operation(
        notes='Add a new user',
        parameters=[
            {
                "name": "body",
                "description": "An user item",
                "required": True,
                "allowMultiple": False,
                "dataType": User.__name__,
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
        ]
    )
    def post(self):
        return BaseAdd.post(self)