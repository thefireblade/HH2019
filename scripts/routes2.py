from scripts import routes1

def sortByGreaterThan(menuItems, field, amount):
    rawList = routes1.sort(menuItems, field)
    updatedList = []
    for i in rawList:
        if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] >= amount:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList

# sortByGreaterThan(menuItems, "carbs", 20)


def cleanList(menuItems):
    for menuItem in menuItems:
        if menuItem["rounded_nutrition_info"]["calories"] is None:
            menuItem["rounded_nutrition_info"]["calories"] = 0
        if menuItem["rounded_nutrition_info"]["g_carbs"] is None:
            menuItem["rounded_nutrition_info"]["g_carbs"] = 0
        if menuItem["rounded_nutrition_info"]["g_fiber"] is None:
            menuItem["rounded_nutrition_info"]["g_fiber"] = 0
        if menuItem["rounded_nutrition_info"]["mg_vitamin"] is None:
            menuItem["rounded_nutrition_info"]["mg_vitamin"] = 0
        if menuItem["rounded_nutrition_info"]["mg_potassium"] is None:
            menuItem["rounded_nutrition_info"]["mg_potassium"] = 0
        if menuItem["rounded_nutrition_info"]["mg_calcium"] is None:
            menuItem["rounded_nutrition_info"]["mg_calcium"] = 0
        if menuItem["rounded_nutrition_info"]["iu_vitamin_a"] is None:
            menuItem["rounded_nutrition_info"]["iu_vitamin_a"] = 0
        if menuItem["rounded_nutrition_info"]["g_added_sugar"] is None:
            menuItem["rounded_nutrition_info"]["g_added_sugar"] = 0
        if menuItem["rounded_nutrition_info"]["mg_cholestrol"] is None:
            menuItem["rounded_nutrition_info"]["mg_cholestrol"] = 0
        if menuItem["rounded_nutrition_info"]["mg_iron"] is None:
            menuItem["rounded_nutrition_info"]["mg_iron"] = 0
        if menuItem["rounded_nutrition_info"]["mg_sodium"] is None:
            menuItem["rounded_nutrition_info"]["mg_sodium"] = 0
        if menuItem["rounded_nutrition_info"]["mg_vitamin_c"] is None:
            menuItem["rounded_nutrition_info"]["mg_vitamin_c"] = 0
        if menuItem["rounded_nutrition_info"]["g_trans_fat"] is None:
            menuItem["rounded_nutrition_info"]["g_trans_fat"] = 0
        if menuItem["rounded_nutrition_info"]["re_vitamin_a"] is None:
            menuItem["rounded_nutrition_info"]["re_vitamin_a"] = 0
        if menuItem["rounded_nutrition_info"]["g_protein"] is None:
            menuItem["rounded_nutrition_info"]["g_protein"] = 0
        if menuItem["rounded_nutrition_info"]["g_sugar"] is None:
            menuItem["rounded_nutrition_info"]["g_sugar"] = 0
        if menuItem["rounded_nutrition_info"]["g_saturated"] is None:
            menuItem["rounded_nutrition_info"]["g_saturated"] = 0
        if menuItem["rounded_nutrition_info"]["g_fat"] is None:
            menuItem["rounded_nutrition_info"]["g_fat"] = 0
    return menuItems

@app.route('./api/sort/greaterthan/calories/<int:amount>', methods=['GET'])
def getCaloriesGreaterThan(menuItems, amount, fields="calories"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/carbs/<int:amount>', methods=['GET'])
def getCarbsGreaterThan(menuItems, amount, fields="carbs"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/protein/<int:amount>', methods=['GET'])
def getProteinGreaterThan(menuItems, amount, fields="protein"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/saturatedfat/<int:amount>', methods=['GET'])
def getSaturatedFatGreaterThan(menuItems, amount, fields="saturated fat"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/fat/<int:amount>', methods=['GET'])
def getFatGreaterThan(menuItems, amount, fields="fat"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/sugar/<int:amount>', methods=['GET'])
def getSugarGreaterThan(menuItems, amount, fields="sugar"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList

@app.route('./api/sort/greaterthan/price/<int:amount>', methods=['GET'])
def getProteinGreaterThan(menuItems, amount, fields="price"):
    updatedList = sortByGreaterThan(menuItems, fields, amount)
    return updatedList
