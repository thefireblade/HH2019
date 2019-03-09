import flask
import requests
import json
from flask import request, jsonify, Blueprint
from routes0 import getLatestMenu

app = Blueprint('route1',__name__, template_folder='templates')

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

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
menuItems = [
        {
            "name": "pizza",
            "rounded_nutrition_info": {
                "calories": 230.0,
                "g_carbs": 41.0,
                "g_fiber": 6.0,
                "mg_vitamin_d": 0.0,
                "mg_potassium": "null",
                "mg_calcium": 42.3,
                "iu_vitamin_a": "null",
                "g_added_sugar": "null",
                "mg_cholesterol": 0.0,
                "mg_iron": 2.6,
                "mg_sodium": 15.0,
                "mg_vitamin_c": 0.0,
                "g_trans_fat": "null",
                "re_vitamin_a": "null",
                "g_protein": 8.0,
                "g_sugar": 1.0,
                "g_saturated_fat": 0.5,
                "g_fat": 4.0
            },
            "location_name": "eastdining",
            "menu_type": "kosher",
            "meal_type":
                ["Breakfast", "Lunch", "Dinner"],
            "price": 5.33
        },
        {
            "name": "bread",
            "rounded_nutrition_info": {
                "calories": 100.0,
                "g_carbs": 23.0,
                "g_fiber": 77.0,
                "mg_vitamin_d": 3.0,
                "mg_potassium": "null",
                "mg_calcium": 23.0,
                "iu_vitamin_a": "null",
                "g_added_sugar": "null",
                "mg_cholesterol": 0.1,
                "mg_iron": 5.0,
                "mg_sodium": 11.0,
                "mg_vitamin_c": 0.2,
                "g_trans_fat": "null",
                "re_vitamin_a": "null",
                "g_protein": 16.0,
                "g_sugar": 5.0,
                "g_saturated_fat": 0.7,
                "g_fat": 7.0
            },
            "location_name": "westdining",
            "menu_type": "kosher",
            "meal_type":
                ["Breakfast", "Lunch", "Dinner"],
            "price": 0.0
        }
]

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
        if menuItem["rounded_nutrition_info"]["calories"] is None:
            print(menuItem)
            menuItems.remove(menuItem)
            continue
        if type(menuItem["rounded_nutrition_info"][nutritionFields.get(field)]) is not float:
            print(menuItem)
            menuItems.remove(menuItem)
            continue
        if isinstance(menuItem["rounded_nutrition_info"][nutritionFields.get(field)], type(None)):
            print(menuItem)
            menuItems.remove(menuItem)

def sort(menuItems, field):
    menuItems = cleanList(menuItems)
    if field == "calories":
        removeAllNone(menuItems, field)
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["calories"])
        return newlist
    elif field == "carbs":
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_carbs"])
        return newlist
    elif field == "protein":
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_protein"])
        return newlist
    elif field == "saturated fat":
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_saturated_fat"])
        return newlist
    elif field == "fat":
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_fat"])
        return newlist
    elif field == "sugar":
        newlist = sorted(menuItems, key=lambda k: k["rounded_nutrition_info"]["g_sugar"])
        return newlist
    elif field == "name":
        newlist = sorted(menuItems, key=lambda k: k["name"])
        return newlist
    elif field == "location_name":
        newlist = sorted(menuItems, key=lambda k: k["location_name"])
        return newlist
    elif field == "meal_type":
        newlist = sorted(menuItems, key=lambda k: k["meal_type"])
        return newlist
    elif field == "price":
        newlist = sorted(menuItems, key=lambda k: k["price"])
        return newlist

def sortByLessThan(menuItems, field, amount):
    rawList = sort(menuItems, field)
    updatedList = []
    for i in rawList:
        if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] <= amount:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList

@app.route('/api/sort/all/calories', methods=['GET'])
def getCalories(field="calories"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/carbs', methods=['GET'])
def getCarbs(field="carbs"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/protein', methods=['GET'])
def getProtein(field="protein"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/saturatedfat', methods=['GET'])
def getSaturatedFat(field="saturated fat"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/fat', methods=['GET'])
def getFat(field="fat"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/sugar', methods=['GET'])
def getSugar(field="sugar"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/name', methods=['GET'])
def getName(field="name"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/all/price', methods=['GET'])
def getPrice(field="price"):
    menuItems = getLatestMenu()
    list = sort(menuItems, field)
    return list

@app.route('/api/sort/lessthanequalto/calories/<int:amount>', methods=['GET'])
def getCaloriesLessThanEqualTo(amount, field="calories"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/carbs/<int:amount>', methods=['GET'])
def getCarbsLessThanEqualTo(amount, field="carbs"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/protein/<int:amount>', methods=['GET'])
def getProteinLessThanEqualTo(amount, field="protein"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/saturatedfat/<int:amount>', methods=['GET'])
def getSaturatedFatLessThanEqualTo(amount, field="saturated fat"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/fat/<int:amount>', methods=['GET'])
def getFatLessThanEqualTo(amount, field="fat"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/sugar/<int:amount>', methods=['GET'])
def getSugarLessThanEqualTo(amount, field="sugar"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

@app.route('/api/sort/lessthanequalto/price/<int:amount>', methods=['GET'])
def getPriceLessThanEqualTo(amount, field="price"):
    menuItems = getLatestMenu()
    updated = sortByLessThan(menuItems, field, amount)
    return updated

def sortByGreaterThan(menuItems, field, amount):
    rawList = sort(menuItems, field)
    updatedList = []
    for i in rawList:
        if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] >= amount:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList

@app.route('/api/sort/greaterthan/calories/<int:amount>', methods=['GET'])
def getCaloriesGreaterThan(amount, fields="calories"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/carbs/<int:amount>', methods=['GET'])
def getCarbsGreaterThan(amount, fields="carbs"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/protein/<int:amount>', methods=['GET'])
def getProteinGreaterThan(amount, fields="protein"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/saturatedfat/<int:amount>', methods=['GET'])
def getSaturatedFatGreaterThan(amount, fields="saturated fat"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/fat/<int:amount>', methods=['GET'])
def getFatGreaterThan(amount, fields="fat"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/sugar/<int:amount>', methods=['GET'])
def getSugarGreaterThan(amount, fields="sugar"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/sort/greaterthan/price/<int:amount>', methods=['GET'])
def getPriceGreaterThan(amount, fields="price"):
    menuItems = getLatestMenu()
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('/api/search/name/', methods=['GET'])
def searchByName(name):
    menuItems = getLatestMenu()
    menuItems = sort(menuItems, nutritionFields.get("name"))
    list = []
    for i in menuItems:
        if i["name"] == name:
            list.append(i)
    return list

@app.route('/api/search/location/', methods=['GET'])
def searchByLocation(field):
    menuItems = getLatestMenu()
    rawList = sort(menuItems, "location_name")
    updatedList = []
    for i in rawList:
        if i["location_name"] == field:
            updatedList.append(i)
    #print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList

@app.route('/api/search/mealtype/', methods=['GET'])
def searchByType(field):
    menuItems = getLatestMenu()
    rawList = sort(menuItems, "meal_type")
    updatedList = []
    for i in rawList:
        for j in i["meal_type"]:
            if j == field:
                updatedList.append(i)
    #print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList
