from scripts import routes1

def searchByLocation(menuItems, field):
    rawList = sort(menuItems, "location_name")
    updatedList = []
    for i in rawList:
        if i["location_name"] == field:
            updatedList.append(i)
    print(json.dumps(updatedList, indent=4, sort_keys=False))
    return updatedList