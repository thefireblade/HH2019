import flask
import requests
import json
from flask import request, jsonify, Blueprint

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
                            "g_fat": 4.0}, "location_name": "eastdining", "menu_type": "kosher",
         "meal_type": ["Breakfast", "Lunch", "Dinner"]},
        {"name": "bread", "rounded_nutrition_info": {
                            "calories": 130.0,
                            "g_carbs": 14.0,
                            "g_fiber": 1.0,
                            "mg_vitamin_d": "null",
                            "mg_potassium": "null",
                            "mg_calcium": 26.2,
                            "iu_vitamin_a": "null",
                            "g_added_sugar": "null",
                            "mg_cholesterol": 35.0,
                            "mg_iron": 1.0,
                            "mg_sodium": 550.0,
                            "mg_vitamin_c": 2.5,
                            "g_trans_fat": "null",
                            "re_vitamin_a": "null",
                            "g_protein": 11.0,
                            "g_sugar": "null",
                            "g_saturated_fat": 0.5,
                            "g_fat": 3.5}, "location_name": "westdining", "menu_type": "kosher",
         "meal_type": ["Breakfast", "Lunch", "Dinner"]}]
# Valid fields are: calories, carbs, protein, fat, saturated fat, sugar, name, price
def sort(menuItems, field):
    if field == "calories":
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


sortByLessThan(menuItems, "carbs", 20)