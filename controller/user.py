__author__ = 'Administrator'
from base import Base,Bases, BasePage
from model.column import User

class UserBase(Base):
    def __init__(self):
        Base.__init__(self, User)

    def to_dict(self, item):
        return dict(id = item.id, device_id = item.device_id, favorite = item.favorite, password = item.password, phone_number = item.phone_number, \
                    create_time = str(item.create_time), update_time = str(item.update_time), user_name = item.user_name, uuid = item.uuid,\
                 picture = item.picture)

class Users(UserBase, Bases):
    pass


class UserPages(UserBase, BasePage):
    pass