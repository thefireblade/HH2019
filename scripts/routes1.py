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
    "calories": "calories",
    "carbs": "g_carbs",

}

# Valid fields are: calories, carbs, protein, fat, saturated fat, sugar, name
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

def sortByLessThan(menuItems, field, amount):
    rawList = sort(menuItems, field)
    updatedList = []
