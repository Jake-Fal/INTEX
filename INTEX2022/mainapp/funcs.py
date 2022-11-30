def searchAPI(queryValue):
    import requests
    nutrients = ['Protein', 'Sodium, Na', 'Potassium, K', 'Water', 'Phosphorus, P']
    foodInfo = []
    r = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=ZG2gfG4lRbZh0UXSFos1GvXbvUrvjsdYX7kYBdVI&query={queryValue}&pageSize=5')
    for i in r.json()['foods']:
        nuts = {}
        name = i['description'].lower()
        id = i['fdcId']
        for j in i['foodNutrients']:
            if j['nutrientName'] in nutrients:
                nuts[j['nutrientName']] = j['value']
        foodInfo.append({
            'id':id,
            'name':name,
            'nutrients': nuts
        })
    return foodInfo