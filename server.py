#from itertools import product
from flask import Flask, request
from about import me
from data import mock_data
import random
import json
#from config import db   #

app=Flask('server')

@app.get("/")
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a simple test"

@app.get("/about")
def about_me():
    return "Guillermo Prieto"

############################################
######### API ENDPOINTS = PRODUCTS #########
############################################

@app.get("/api/version")
def version():
    return "1.0"

@app.get("/api/about")
def about_json():
    #return me["first"] + " " + me["last"]
    #return f'{me["first"]} {me["last"]}'
    return json.dumps(me) # parse the dict into a json string

@app.get("/api/products")
def get_products():
    return json.dumps(mock_data)

@app.post("/api/products")
def save_product():
    product=request.get_json() # get an dictionary or a list
    # add product to the catalog
    mock_data.append(product)
    # assign an id to the product
    product["id"]=random.randint(1, 893214789)
    # return the product as json
    return json.dumps(product)

    

@app.get("/api/products/<id>")
def get_product_by_id(id):
    
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)

    return "NOT FOUND"

@app.get("/api/products_category/<category>")
def get_prods_category(category):
    # print("your category: ", category)
    results = []
    category=category.lower()
    for prod in mock_data:
        if prod["category"].lower() == category:
            results.append(prod)

    return json.dumps(results)

# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest():
    solution=mock_data[0]
    for prod in mock_data:
        if prod["price"]<solution["price"]:
            solution=prod

    return json.dumps(solution)

@app.get("/api/categories")
def get_categories():
    categories = []
    for product in mock_data:
        cat= product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)

# getreturn the number of prods in the catalog (mock_data)
# /api/count_products

@app.get("/api/count_products")
def get_products_count():
    count=len(mock_data)

    return json.dumps({"countn": count})

# get /api/search/<text>
# return all prods whose title contains text
@app.get("/api/search/<text>")
def search_products(text):
    results=[]

    # do the magic here
    text=text.lower()
    for prod in mock_data:
       if text in prod["title"].lower():
            results.append(prod) 

    return json.dumps(results)

app.run(debug=True)