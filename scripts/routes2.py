from scripts import routes1

def searchByType(menuItems, field):
    rawList = sort(menuItems, "meal_type")
    updatedList = []
    for i in rawList:
        if i["meal_type"] == field:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList