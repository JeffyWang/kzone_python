__author__ = 'Administrator'

from db import ini_db
from datetime import datetime
from flask_restful_swagger import swagger

db = ini_db()

class Area(db.Model):
    __tablename__ = 'k_area'

    id = db.Column(db.Integer, primary_key=True)
    area_id = db.Column(db.String(16))
    area_name = db.Column(db.String(16))
    reference = db.Column(db.String(16))

class City(db.Model):
    __tablename__ = 'k_city'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.String(16))
    city_name = db.Column(db.String(16))
    reference = db.Column(db.String(16))

class Comment(db.Model):
    __tablename = 'k_comment'

    id = db.Column(db.Integer, primary_key=True)
    ktv_id = db.Column(db.String(16))
    comment = db.Column(db.String(20480))
    create_time = db.Column(db.TIME)
    environment_score = db.Column(db.String(32))
    score = db.Column(db.String(32))
    service_score = db.Column(db.String(32))
    sound_effects_score = db.Column(db.String(32))
    user_id = db.Column(db.String(16))
    user_name = db.Column(db.String(16))

    def __init__(self, ktv_id, comment, environment_score, score, service_score, sound_effects_score, user_id, user_name):
        self.ktv_id = ktv_id
        self.comment = comment
        self.environment_score = environment_score
        self.score = score
        self.service_score = service_score
        self.sound_effects_score = sound_effects_score
        self.user_id = user_id
        self.user_name = user_name
        self.create_time = datetime.now()

class Game(db.Model):
    __tablename = 'k_game'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.TIME)
    game = db.Column(db.TEXT)
    introduction = db.Column(db.TEXT)
    name = db.Column(db.String(128))
    picture = db.Column(db.String(256))
    update_time = db.Column(db.TIME)

    def __init__(self, game, introduction, name, picture):
        self.game = game
        self.introduction = introduction
        self.name = name
        self.picture = picture
        self.create_time = datetime.now
        self.update_time = datetime.now()

@swagger.model
class Information(db.Model):
    __tablename__ = 'k_information'

    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.TEXT)
    create_time = db.Column(db.DateTime)
    introduction = db.Column(db.TEXT)
    picture = db.Column(db.String(256))
    title = db.Column(db.String(128))
    update_time = db.Column(db.DateTime)

    def __init__(self, article, introduction, picture, title):
        self.article = article
        self.create_time = datetime.now()
        self.introduction = introduction
        self.picture = picture
        self.title = title
        self.update_time = datetime.now()

class Ktv(db.Model):
     __tablename__ = 'k_ktv'

     id = db.Column(db.Integer, primary_key=True)
     address = db.Column()
     average_price = db.Column()
     business_area = db.Column()
     business_id = db.Column()
     create_time = db.Column()
     district_id = db.Column()
     introduction = db.Column()
     latitude = db.Column()
     longitude = db.Column()
     name = db.Column()
     phone_number = db.Column()
     pictures = db.Column()
     price = db.Column()
     score = db.Column()
     update_time = db.Column()

class Province():
    __tablename__ = 'k_province'

    id = db.Column(db.Integer, primary_key=True)
    province_id = db.Column(db.String(16))
    province_name = db.Column(db.String(16))

class Statistics():
    __tablename__ = 'k_statistics'

    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(128))
    app_version = db.Column(db.String(128))
    create_time = db.Column(db.TIME)
    os_type = db.Column(db.String(128))
    os_version = db.Column(db.String(128))
    token = db.Column(db.String(128))
    user_id = db.Column(db.Integer)

    def __init__(self, app_name, app_version, os_type, os_version, token, user_id):
        self.app_name = app_name
        self.app_version = app_version
        self.os_type = os_type
        self.os_version = os_version
        self.token = token
        self.user_id = user_id
        self.create_time = datetime.now()

class User(db.Model):
    __tablename__ = 'k_user'

    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime)
    device_id = db.Column(db.String(16))
    favorite = db.Column(db.String(128))
    password = db.Column(db.String(32))
    phone_number = db.Column(db.String(256))
    update_time = db.Column(db.DateTime)
    user_name = db.Column(db.String(16))
    uuid = db.Column(db.String(100))
    picture = db.Column(db.String(256))

