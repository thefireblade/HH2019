import flask
import requests
import json
from flask import request, jsonify, Blueprint
from routes0 import getTempMenu, updateMenu

app = Blueprint('route1',__name__, template_folder='templates')
# r = requests.get(url = "", )
# data = r.json()

nutritionFields = {
    "nutrition": "rounded_nutrition_info",
    "calories": "calories",
    "carbs": "g_carbs",
    "protein": "g_protein",
    "fat": "g_fat",
    "saturated fat": "g_saturated_fat",
    "sugar": "g_sugar",
    "name": "name",
    "price": "price"
}

def cleanList(menuItems):
    for menuItem in menuItems:
        if menuItem["price"] == 0.0:
            menuItems.remove(menuItem)
            continue
        if menuItem["rounded_nutrition_info"]["calories"] is None:
            menuItem["rounded_nutrition_info"]["calories"] = 0.0
        if menuItem["rounded_nutrition_info"]["g_carbs"] == "null":
            menuItem["rounded_nutrition_info"]["g_carbs"] = 0.0
        if menuItem["rounded_nutrition_info"]["g_fiber"] == "null":
            menuItem["rounded_nutrition_info"]["g_fiber"] = 0.0
        if menuItem["rounded_nutrition_info"]["mg_vitamin_d"] == "null":
            menuItem["rounded_nutrition_info"]["mg_vitamin_d"] = 0.0
        if menuItem["rounded_nutrition_info"]["mg_potassium"] == "null":
            menuItem["rounded_nutrition_info"]["mg_potassium"] = 0.0
        if menuItem["rounded_nutrition_info"]["mg_calcium"] == "null":
            menuItem["rounded_nutrition_info"]["mg_calcium"] = 0.0
        if menuItem["rounded_nutrition_info"]["iu_vitamin_a"] == "null":
            menuItem["rounded_nutrition_info"]["iu_vitamin_a"] = 0.0
        if menuItem["rounded_nutrition_info"]["g_added_sugar"] == "null":
            menuItem["rounded_nutrition_info"]["g_added_sugar"] = 0.0
        if menuItem["rounded_nutrition_info"]["mg_cholesterol"] == "null":
            menuItem["rounded_nutrition_info"]["mg_cholesterol"] = 0.0
        if menuItem["rounded_nutrition_info"]["mg_iron"] == "null":
            menuItem["rounded_nutrition_info"]["mg_iron"] = 0
        if menuItem["rounded_nutrition_info"]["mg_sodium"] == "null":
            menuItem["rounded_nutrition_info"]["mg_sodium"] = 0
        if menuItem["rounded_nutrition_info"]["mg_vitamin_c"] == "null":
            menuItem["rounded_nutrition_info"]["mg_vitamin_c"] = 0
        if menuItem["rounded_nutrition_info"]["g_trans_fat"] == "null":
            menuItem["rounded_nutrition_info"]["g_trans_fat"] = 0
        if menuItem["rounded_nutrition_info"]["re_vitamin_a"] == "null":
            menuItem["rounded_nutrition_info"]["re_vitamin_a"] = 0
        if menuItem["rounded_nutrition_info"]["g_protein"] == "null":
            menuItem["rounded_nutrition_info"]["g_protein"] = 0
        if menuItem["rounded_nutrition_info"]["g_sugar"] == "null":
            menuItem["rounded_nutrition_info"]["g_sugar"] = 0
        if menuItem["rounded_nutrition_info"]["g_saturated_fat"] == "null":
            menuItem["rounded_nutrition_info"]["g_saturated_fat"] = 0
        if menuItem["rounded_nutrition_info"]["g_fat"] == "null":
            menuItem["rounded_nutrition_info"]["g_fat"] = 0
    return menuItems

# Valid fields are: calories, carbs, protein, fat, saturated fat, sugar, name, price
def removeAllNone(menuItems, field):
    for menuItem in menuItems:
        if menuItem["rounded_nutrition_info"][field] is None:
            menuItem["rounded_nutrition_info"][field] = 0
            continue
        if type(menuItem["rounded_nutrition_info"][field]) is not float:
            menuItem["rounded_nutrition_info"][field] = 0
            continue
        if isinstance(menuItem["rounded_nutrition_info"][field], type(None)):
            menuItem["rounded_nutrition_info"][field] = 0

def removeAllForElse(menuItems, field):
    for menuItem in menuItems:
        if menuItem[field] is None:
            menuItem[field] = 0
            continue
        if type(menuItem[field]) is not float:
            menuItem[field] = 0
            continue
        if isinstance(menuItem[field], type(None)):
            menuItem[field] = 0

def sort(menuItems, field):
    #menuItems = cleanList(menuItems)
    if field == "calories":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["calories"])
        return newlist
    elif field == "carbs":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_carbs"])
        return newlist
    elif field == "protein":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_protein"])
        return newlist
    elif field == "saturated fat":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_saturated_fat"])
        return newlist
    elif field == "fat":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_fat"])
        return newlist
    elif field == "sugar":
        removeAllNone(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_sugar"])
        return newlist
    elif field == "name":
        #removeAllForElse(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["name"])
        return newlist
    elif field == "location_name":
        #removeAllForElse(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["location_name"])
        return newlist
    elif field == "meal_type":
        #removeAllForElse(menuItems, nutritionFields.get(field))
        #newlist = sorted(menuItems, key=lambda k: k["meal_type"])
        #return newlist
        return menuItems
    elif field == "price":
        removeAllForElse(menuItems, nutritionFields.get(field))
        newlist = sorted(menuItems, key=lambda k: k["price"])
        return newlist

def sortByLessThan(menuItems, field, amount):
    rawList = sort(menuItems, field)
    updatedList = []
    if field == "price":
        for i in rawList:
            if i[nutritionFields.get(field)] * 1.0 > amount * 1.0:
                updatedList.append(i)
    else:
        for i in rawList:
            if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] * 1.0 <= amount * 1.0:
                updatedList.append(i)
    return updatedList

@app.route('/api/sort/all/calories', methods=['GET'])
def getCalories(field="calories"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/carbs', methods=['GET'])
def getCarbs(field="carbs"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/protein', methods=['GET'])
def getProtein(field="protein"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/saturatedfat', methods=['GET'])
def getSaturatedFat(field="saturated fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/fat', methods=['GET'])
def getFat(field="fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/sugar', methods=['GET'])
def getSugar(field="sugar"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/name', methods=['GET'])
def getName(field="name"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/all/price', methods=['GET'])
def getPrice(field="price"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sort(menuItems, field)))

@app.route('/api/sort/lessthanequalto/calories/<float:amount>', methods=['GET'])
def getCaloriesLessThanEqualTo(amount, field="calories"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/carbs/<float:amount>', methods=['GET'])
def getCarbsLessThanEqualTo(amount, field="carbs"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/protein/<float:amount>', methods=['GET'])
def getProteinLessThanEqualTo(amount, field="protein"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/saturatedfat/<float:amount>', methods=['GET'])
def getSaturatedFatLessThanEqualTo(amount, field="saturated fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/fat/<float:amount>', methods=['GET'])
def getFatLessThanEqualTo(amount, field="fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/sugar/<float:amount>', methods=['GET'])
def getSugarLessThanEqualTo(amount, field="sugar"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

@app.route('/api/sort/lessthanequalto/price/<float:amount>', methods=['GET'])
def getPriceLessThanEqualTo(amount, field="price"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByLessThan(menuItems, field, amount)))

def sortByGreaterThan(menuItems, field, amount):
    rawList = sort(menuItems, field)
    updatedList = []
    if field == "price":
        for i in rawList:
            if i[nutritionFields.get(field)] * 1.0 > amount * 1.0:
                updatedList.append(i)
    else:
        for i in rawList:
            if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] * 1.0 > amount * 1.0:
                updatedList.append(i)
    return updatedList

@app.route('/api/sort/greaterthan/calories/<float:amount>', methods=['GET'])
def getCaloriesGreaterThan(amount, fields="calories"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/carbs/<float:amount>', methods=['GET'])
def getCarbsGreaterThan(amount, fields="carbs"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/protein/<float:amount>', methods=['GET'])
def getProteinGreaterThan(amount, fields="protein"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/saturatedfat/<float:amount>', methods=['GET'])
def getSaturatedFatGreaterThan(amount, fields="saturated fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/fat/<float:amount>', methods=['GET'])
def getFatGreaterThan(amount, fields="fat"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/sugar/<float:amount>', methods=['GET'])
def getSugarGreaterThan(amount, fields="sugar"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/sort/greaterthan/price/<float:amount>', methods=['GET'])
def getPriceGreaterThan(amount, fields="price"):
    menuItems = getTempMenu()
    return jsonify(updateMenu(sortByGreaterThan(menuItems, fields, amount)))

@app.route('/api/search/name/<string:name>', methods=['GET'])
def searchByName(name):
    name = name.replace("%20", " ")
    menuItems = getTempMenu()
    menuItems = sort(menuItems, nutritionFields.get("name"))
    list = []
    for i in menuItems:
        if name.lower() in i["name"].lower():
            list.append(i)
    return jsonify(updateMenu(list))

@app.route('/api/search/location/<string:field>', methods=['GET'])
def searchByLocation(field):
    field = field.replace("%20", " ")
    menuItems = getTempMenu()
    rawList = sort(menuItems, "location_name")
    updatedList = []
    for i in rawList:
        if field.lower() in i["location_name"].lower():
            updatedList.append(i)
    #print(json.dumps(updatedList, indent=4, sort_keys=False))
    return jsonify(updateMenu(updatedList))

@app.route('/api/search/mealtype/<string:field>', methods=['GET'])
def searchByType(field):
    field = field.replace("%20", " ")
    menuItems = getTempMenu()
    rawList = sort(menuItems, "meal_type")
    updatedList = []
    for i in rawList:
        if i["meal_type"] is None:
            continue
        if field.lower() in i['meal_type'].lower():
            updatedList.append(i)
    #print(json.dumps(updatedList, indent=4, sort_keys=False))
    return jsonify(updateMenu(updatedList))
