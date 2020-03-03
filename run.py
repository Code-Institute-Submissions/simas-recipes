import os
import json
import pymysql
import pymongo
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, request, session, url_for, abort
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson import json_util
from bson.json_util import dumps
import re

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "recipechat")

app.config["MONGO_DBNAME"] = "SimaRecipes"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")

recipe = PyMongo(app)

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        #print("Mongo is Connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    #messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append({"timestamp": now, "from": username, "message": message})
    

@app.route("/")
def index():
    return render_template("index.html", 
    recipe_chicken = recipe.db.recipes.find(),
    recipe_veg = recipe.db.recipes.find(),
    recipe_lamb = recipe.db.recipes.find(),
    recipe_seafood = recipe.db.recipes.find(),
    recipe_beef = recipe.db.recipes.find(),
    recipe_healthy = recipe.db.recipes.find(),
    recipe_vegan = recipe.db.recipes.find(),
    recipe_pork = recipe.db.recipes.find(),
    recipe_25 = recipe.db.recipes.find(),
    recipe_35 = recipe.db.recipes.find(),
    recipe_amc = recipe.db.recipes.find(),
    recipe_auc = recipe.db.recipes.find(),
    recipe_cdc = recipe.db.recipes.find(),
    recipe_cnc = recipe.db.recipes.find(),
    recipe_euc = recipe.db.recipes.find(),
    recipe_fec = recipe.db.recipes.find(),
    recipe_mdc = recipe.db.recipes.find(),
    recipe_mec = recipe.db.recipes.find(),
    recipe_nac = recipe.db.recipes.find(),
    recipe_safc = recipe.db.recipes.find(),
    recipe_samc = recipe.db.recipes.find(),
    recipe_sasc = recipe.db.recipes.find())
    

@app.route("/SimaRecipes/recipes")
def simasrecipe_project():
    projects = recipe.find(projection = recipe.FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    
    return render_template("index.html", json_projects=json_projects)
        

    
@app.route("/recipes")
def recipes():
    return render_template("recipes.html", 
    page_title="Recipes", 
    recipes = recipe.db.recipes.find().sort('recipe_name'))
    

@app.route("/search_recipe")
def search_recipe():
    return render_template("searchrecipe.html", page_title="Recipes", 
    recipes_veg = recipe.db.recipes.find().sort('recipe_name'),
    recipes_chick = recipe.db.recipes.find().sort('recipe_name'),
    recipes_lamb = recipe.db.recipes.find().sort('recipe_name'),
    recipes_seafood = recipe.db.recipes.find().sort('recipe_name'),
    recipes_beef = recipe.db.recipes.find().sort('recipe_name'),
    recipes_healthy = recipe.db.recipes.find().sort('recipe_name'),
    recipes_vegan = recipe.db.recipes.find().sort('recipe_name'),
    recipes_pork = recipe.db.recipes.find().sort('recipe_name'),
    recipes_amc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_auc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_cdc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_cnc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_euc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_fec = recipe.db.recipes.find().sort('recipe_name'),
    recipes_mdc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_mec = recipe.db.recipes.find().sort('recipe_name'),
    recipes_nac = recipe.db.recipes.find().sort('recipe_name'),
    recipes_safc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_samc = recipe.db.recipes.find().sort('recipe_name'),
    recipes_sasc = recipe.db.recipes.find().sort('recipe_name'))

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        flash("Thanks {}, we have received your message!".format(
            request.form["name"]
        ))
        #print(request.form["name"])
    return render_template("contact.html", page_title="Contact")

@app.route("/chat", methods = ["GET", "POST"])
def chat():
    if request.method == "POST":
        session["username"] = request.form["chatname"]
        
    if "username" in session:
        #return redirect (session["username"])
        return redirect (url_for("user", username = session["username"]))
        
    return render_template("chat.html")
    
@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Display chat Messages"""
    
    if request.method == "POST":
        username = session["username"]
        message = request.form["chatmessage"]
        add_messages(username, message)
        #return redirect(session["username"])
        return redirect (url_for("user", username = session["username"]))
        
    return render_template("chat.html", username = username, chat_messages = messages)

@app.route('/loginuser')
def loginuser():
    '''return render_template("login.html")'''
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect(url_for('admin'))

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return redirect(url_for('admin'))
    else:
        flash("Username or Password Mismatch!")
        return redirect(url_for('loginuser'))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('loginuser'))

@app.route("/admin")
def admin():
    return render_template("admin.html", page_title ="Admin",
    categories = recipe.db.categories.find(), 
    recipes = recipe.db.recipes.find().sort('recipe_name'),
    category = recipe.db.categories.find().sort('category_name'),
    images = recipe.db.images.find().sort('recipe_image'),
    cuisines = recipe.db.cuisines.find().sort('cuisine_name'),
    cuisines_list = recipe.db.cuisines.find().sort('cuisine_name'))
    
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    addrecipes = recipe.db.recipes
    addrecipes.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))
  
@app.route("/insert_category", methods=["POST"])
def insert_category():
    addcategory = recipe.db.categories
    addcategory.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))
    
@app.route("/insert_cuisine", methods=["POST"])
def insert_cuisine():
    addcuisine = recipe.db.cuisines
    addcuisine.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))

@app.route("/edit_recipe/<task_id>")
def edit_recipe(task_id):
    the_recipe = recipe.db.recipes.find_one({"_id": ObjectId(task_id)})
    all_categories = recipe.db.categories.find()
    all_images = recipe.db.images.find()
    all_cuisines = recipe.db.cuisines.find().sort('cuisine_name')
    return render_template("editrecipe.html", page_title="Edit Recipe", recipe = the_recipe, categories = all_categories, images = all_images, cuisines = all_cuisines)
    
@app.route("/edit_category/<cat_id>")
def edit_category(cat_id):
    return render_template("editcategory.html", 
    page_title="Edit Category", 
    category = recipe.db.categories.find_one({'_id': ObjectId(cat_id)}))
    
@app.route("/edit_cuisine/<cus_id>")
def edit_cuisine(cus_id):
    return render_template("editcuisine.html", 
    page_title="Edit Cuisine", 
    cuisines = recipe.db.cuisines.find_one({'_id': ObjectId(cus_id)}))
    
@app.route("/update_recipe/<task_id>", methods=["POST"])
def update_recipe(task_id):
    updaterecipe = recipe.db.recipes
    updaterecipe.update({'_id': ObjectId(task_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_type': request.form.get('recipe_type'),
        'recipe_image': request.form.get('recipe_image'),
        'recipe_cuisine': request.form.get('recipe_cuisine'),
        'ingredient_1': request.form.get('ingredient_1'),
        'ingredient_2': request.form.get('ingredient_2'),
        'ingredient_3': request.form.get('ingredient_3'),
        'ingredient_4': request.form.get('ingredient_4'),
        'ingredient_5': request.form.get('ingredient_5'),
        'ingredient_6': request.form.get('ingredient_6'),
        'ingredient_7': request.form.get('ingredient_7'),
        'ingredient_8': request.form.get('ingredient_8'),
        'ingredient_9': request.form.get('ingredient_9'),
        'method_1': request.form.get('method_1'),
        'method_2': request.form.get('method_2'),
        'method_3': request.form.get('method_3'),
        'method_4': request.form.get('method_4'),
        'method_5': request.form.get('method_5'),
        'method_6': request.form.get('method_6'),
        'method_7': request.form.get('method_7'),
        'method_8': request.form.get('method_8'),
        'method_9': request.form.get('method_9'),
        'create_on': request.form.get('create_on'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time')
    })
    return redirect(url_for("admin"))
 

@app.route("/update_category/<cat_id>", methods=["POST"])
def update_category(cat_id):
    updatecategory = recipe.db.categories
    updatecategory.update({'_id': ObjectId(cat_id)},
    {
        'category_name' : request.form.get('category_name')
    })
    return redirect(url_for('admin'))
    
@app.route("/update_cuisine/<cus_id>", methods=["POST"])
def update_cuisine(cus_id):
    updatecuisine = recipe.db.cuisines
    updatecuisine.update({'_id': ObjectId(cus_id)},
    {
        'cuisine_name' : request.form.get('cuisine_name')
    })
    return redirect(url_for('admin'))

@app.route('/delete_recipe/<task_id>')
def delete_recipe(task_id):
    recipe.db.recipes.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('admin'))
    
@app.route('/delete_category/<cat_id>')
def delete_category(cat_id):
    recipe.db.categories.remove({'_id': ObjectId(cat_id)})
    return redirect(url_for('admin'))
    
@app.route('/delete_cuisine/<cus_id>')
def delete_cuisine(cus_id):
    recipe.db.cuisines.remove({'_id': ObjectId(cus_id)})
    return redirect(url_for('admin'))

@app.route("/recipes/<recipe_name>")
def about_recipe(recipe_name):
    recipe={}
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                recipe = obj
    return render_template("description.html", recipe=recipe)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)