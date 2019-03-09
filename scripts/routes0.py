from flask import request, jsonify, Blueprint
from datetime import datetime
from operator import itemgetter
import pymongo

import requests

app = Blueprint('route0',__name__, template_folder='templates')
#URL = blah blah

# data to be sent to api
'''data = {'api_dev_key':API_KEY,
        'api_option':'paste',
        'api_paste_code':source_code,
        'api_paste_format':'python'}
'''
#127.0.0.1:27017


# Gets all the menu items of all locations and attaches the locations to the menu items.
# Starts from the second item of the array  to avoid admin menu items:
# THIS FUNCTION IS ONLY MEANT TO BE RUN ONCE SINCE IT TAKES UP SO MUCH SPACE
def getAllMenuItems():
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = mongoClient['hh2019']
    document =  {}
    menuItems = []
    document['year'] =  datetime.now().year
    document['month'] = datetime.now().month
    document['day'] = datetime.now().day
    location_api = "https://stonybrook.nutrislice.com/menu/api/schools/?format=json"
    #r = requests.post(url = API_ENDPOINT, data = data)
    location_response = requests.get(url = location_api)
    locations = location_response.json()

    for location in locations:
        location_name = location['name']
        for menuTypes in location['active_menu_types']:
            menu_type = menuTypes['name']
            menu_url = "https://stonybrook.nutrislice.com" + menuTypes['urls']['full_menu_by_date_api_url_template']
            menu_url = menu_url.replace("{year}", str(datetime.now().year))
            menu_url = menu_url.replace("{month}", str(datetime.now().month))
            menu_url = menu_url.replace("{day}", str(datetime.now().day))
            menu_url = menu_url + "?format=json"
            menu = requests.get(url = menu_url).json()
            for menu_info in menu["days"]:
                meal_types = []
                for key in menu_info['menu_info']:
                    meal_type = menu_info['menu_info'][key]['section_options']['display_name']
                    meal_types.append(meal_type)
                if len(meal_types) == 0:
                    continue
                for menu_items in menu_info['menu_items']:
                    if menu_items['food'] is None:
                        continue
                    food_item = menu_items['food']
                    food_item['menu_type'] = menu_type
                    food_item['meal_type']  = meal_type
                    food_item['location_name'] = location_name
                    menuItems.append(food_item)
    document['menuItems'] = menuItems
    mydb['MenuItems'].insert_one(document)

#Retrieves the latest menu items from mongo
def getLatestMenu():
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = mongoClient['hh2019']
    myCol = mydb['MenuItems']
    try:
        MenuItems = myCol.find_one({'year': datetime.now().year, 'month': datetime.now().month, 'day': datetime.now().day})
        if MenuItems is None:
            getAllMenuItems()
        return MenuItems
    except:
        getAllMenuItems()
        MenuItems = myCol.find_one({'year': datetime.now().year, 'month': datetime.now().month, 'day': datetime.now().day})
        return MenuItems['menuItems']

def updateMenu(menuItems):
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = mongoClient['hh2019']
    myCol = mydb['MenuItems']
    myCol.update({'year': datetime.now().year, 'month': datetime.now().month, 'day': datetime.now().day}, {"$set": {'menuItems':menuItems}})
    return menuItems
'''
Takes  in  an array with a price field
'''
#test = [ {'price':3.00}, {'price':1.00}, {'price':1.5}, {'price':5.00}]
def sortByPrice(arr):
    newlist = sorted(arr, key=itemgetter('price'))
    return newlist
@app.route('/api/sort/all/price', methods=['GET'])
def returnSortedByPrice():
    menuItems = getLatestMenu()
    return jsonify(updateMenu(sortByPrice(menuItems)))
@app.route('/api/menu/update', methods=['GET'])
def updateMongoWithAllMenus():
    getAllMenuItems()
    return jsonify({'Success':True})
