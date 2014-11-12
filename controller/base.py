__author__ = 'Administrator'
import json
from flask.ext.restful import Resource
from flask import request
from model.db import ini_db
from util.response import rep

db = ini_db()

class Base(Resource):
    name = '1'
    def __init__(self, model):
        self.model = model;

    def to_dict(self, item):
        pass

    def update(self, model, request_data):
        pass

    def insert(self, request_data):
        pass

class Bases(Base):
    def get(self, id):
        if id == 0:
            try:
                model = db.session.query(self.model).order_by(self.model.id.desc()).all()
                model = [self.to_dict(item) for item in model]
            except Exception as ex:
                return rep(500, ex.message), 500
            finally:
                db.session.rollback()
        else:
            try:
                model = db.session.query(self.model).get(id)
                model = self.to_dict(model)
            except Exception as ex:
                return rep(404, u'not fount : %s' % ex.message), 404
            finally:
                db.session.rollback()

        return model

    def delete(self, id):
        model = db.session.query(self.model).get(id)
        if model is None:
            return rep(404, u'not found'), 404

        try:
            db.session.delete(model)
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500
        finally:
            db.session.rollback()

        return rep(200, u'delete %s success' % self.model.__name__)

    def put(self, id):
        request_data = json.loads(request.data)

        try:
            model = db.session.query(self.model).get(id)
        except Exception as ex:
             return rep(500, ex.message), 500
        finally:
            db.session.rollback()

        if model is None:
            return rep(404, u'not found'), 404

        self.update(model, request_data)

        try:
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500
        finally:
            db.session.rollback()

        return rep(200, u'update %s success' % self.model.__name__)


class BasePage(Base):
    def get(self, page, size):
        offset = page * size
        try:
            model_page = db.session.query(self.model).order_by(self.model.create_time.desc()).offset(offset).limit(size)
            model_page = [self.to_dict(item) for item in model_page]
        except Exception as ex:
            return rep(500, ex.message), 500
        finally:
            db.session.rollback()

        return model_page


class BaseAdd(Base):
    def post(self):
        request_data = json.loads(request.data)
        try:
            model = self.insert(request_data)
        except Exception as ex:
            print ex

        try:
            db.session.add(model)
            db.session.commit()
        except Exception as ex:
            return rep(500, ex.message), 500
        finally:
            db.session.rollback()

        return rep(200, u'add %s success' % self.model.__name__)