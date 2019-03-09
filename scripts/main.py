from routes0 import app as route0
from routes1 import app as route1
import pymongo
from flask import request, jsonify, Blueprint

import routes0 as methods0
import flask
#import mysql.connector
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="hh2019",
    passwd="hh2019",
    database="hh2019"
)
'''
mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = mongoClient['hh2019']

print("connected to our mysql server successfully")
app = flask.Flask(__name__)
app.config["DEBUG"] = False
app.register_blueprint(route0)
app.register_blueprint(route1)
#
#
# if reset:
#     print('Getting all menu items')
#     all_menu_items = methods0.getAllMenuItems()
#     print('Got all menu items')
#     reset = False
#
# @app.route('/api/sort/all/price', methods=['GET'])
# def returnSortedByPrice():
#     return jsonify(methods0.sortByPrice(all_menu_items))

app.run(host='0.0.0.0')