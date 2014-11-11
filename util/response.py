__author__ = 'Administrator'
import json
from flask import jsonify

def rep(c, m):
    return json.loads(json.dumps(dict(code=c, message=m)))