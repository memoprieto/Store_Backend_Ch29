#from ast import Import #
from bson import ObjectId
from flask import Flask, request
from about import me
from data import mock_data
import random
import json
from config import db 

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

def fix_mongo_id(obj):
    # fix the _id
    obj["id"] = str(obj["_id"])  
    del obj["_id"]
    return obj

@app.get("/api/products")
def get_products(): #def get_products():   data_json():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)

@app.post("/api/products")
def save_product():
    product=request.get_json() # get an dictionary or a list

    # save the product
    db.products.insert_one(product) 
    fix_mongo_id(product)

    return json.dumps(product)




@app.get("/api/products/<id>")
def get_product_by_id(id):
    #db.products.find_one({"_id": ObjectId(id)})
    
    for prod in mock_data:
        if str(prod["id"]) == id:
            return json.dumps(prod)

    return "NOT FOUND"

@app.get("/api/products_category/<category>")
def get_prods_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)

# GET /api/product_cheapest
@app.get("/api/product_cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution=cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod

    fix_mongo_id(solution)
    return json.dumps(solution)

@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})
    for product in cursor:
        cat= product["category"]
        if not cat in categories:
            categories.append(cat)

    return json.dumps(categories)

# getreturn the number of prods in the catalog (mock_data)
# /api/count_products

@app.get("/api/count_products")
def get_products_count():
    cursor = db.products.find({})
    count = 0
    for prod in cursor:
        count += 1
    
    return json.dumps({"count": count})

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