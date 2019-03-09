from scripts import routes1

def sortByGreaterThan(menuItems, field, amount):
    rawList = routes1.sort(menuItems, field)
    updatedList = []
    for i in rawList:
        if i[nutritionFields.get("nutrition")][nutritionFields.get(field)] >= amount:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))

# sortByGreaterThan(menuItems, "carbs", 20)