__author__ = 'Administrator'
import json
from flask.ext.restful import Resource
from model.db import ini_db
from util.response import rep

db = ini_db()

class Base(Resource):
    def __init__(self, model):
        self.model = model;

    def to_dict(self, item):
        pass

class Bases(Base):
    def get(self, id):
        if id == 0:
            try:
                model = db.session.query(self.model).order_by(self.model.id.desc()).all()
                model = [self.to_dict(item) for item in model]
            except Exception as ex:
                return rep(500, ex.message), 500
        else:
            try:
                model = db.session.query(self.model).get(id)
                model = self.to_dict(model)
            except Exception as ex:
                return rep(404, u'not fount : %s' % ex.message), 404

        return model

    def delete(self, id):
        pass

    def put(self, id):
        pass


class BasePage(Base):
    def get(self, page, size):
        offset = page * size
        try:
            model_page = db.session.query(self.model).order_by(self.model.create_time.desc()).offset(offset).limit(size)
            model_page = [self.to_dict(item) for item in model_page]
        except Exception as ex:
            return rep(500, ex.message), 500

        return model_page


class BaseAdd(Resource):
    def post(self):
        pass