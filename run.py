import os
import json
import pymysql
import pymongo
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, session, url_for, abort
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson import json_util
from bson.json_util import dumps
import re
import bcrypt


app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "recipechat")


# Connection with MongoDB
app.config["MONGO_DBNAME"] = "SimaRecipes"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")


# Variable to connected MongoDB database
recipe = PyMongo(app)


def mongo_connect(url):
    """MongoDB connection"""
    try:
        conn = pymongo.MongoClient(url)
        #print("Mongo is Connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Empty array to store messages
messages = []


# for CHAT messages (chat.html)
def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    #messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append({"timestamp": now, "from": username, "message": message})
    

# dashboard (index.html)
@app.route("/")
def index():
    return render_template("index.html", 
    recipe_chicken = recipe.db.recipes.find(), # Variable to count Chicken recipes in database
    recipe_veg = recipe.db.recipes.find(), # Variable to count Vegetable recipes in database
    recipe_lamb = recipe.db.recipes.find(), # Variable to count Lamb recipes in database
    recipe_seafood = recipe.db.recipes.find(), # Variable to count Sea Food recipes in database
    recipe_beef = recipe.db.recipes.find(), # Variable to count Beef recipes in database
    recipe_healthy = recipe.db.recipes.find(), # Variable to count Healthy recipes in database
    recipe_vegan = recipe.db.recipes.find(), # Variable to count Vegan recipes in database
    recipe_pork = recipe.db.recipes.find(), # Variable to count Pork recipes in database
    recipe_25 = recipe.db.recipes.find(), # Variable to count recipes which can be ready under 30 mins in database
    recipe_35 = recipe.db.recipes.find(), # Variable to count recipes which takes over 30 mins to ready in database
    recipe_amc = recipe.db.recipes.find(), # Variable to count American Cuisine recipes in database
    recipe_auc = recipe.db.recipes.find(), # Variable to count Australian Cuisine recipes in database
    recipe_cdc = recipe.db.recipes.find(), # Variable to count Canadian Cuisine recipes in database
    recipe_cnc = recipe.db.recipes.find(), # Variable to count Chinese Cuisine recipes in database
    recipe_euc = recipe.db.recipes.find(), # Variable to count European Cuisine recipes in database
    recipe_fec = recipe.db.recipes.find(), # Variable to count Far Eastern Cuisine recipes in database
    recipe_mdc = recipe.db.recipes.find(), # Variable to count Meditarrenean Cuisine recipes in database
    recipe_mec = recipe.db.recipes.find(), # Variable to count Middle Eastern Cuisine recipes in database
    recipe_nac = recipe.db.recipes.find(), # Variable to count North African Cuisine recipes in database
    recipe_safc = recipe.db.recipes.find(), # Variable to count South African Cuisine recipes in database
    recipe_samc = recipe.db.recipes.find(), # Variable to count South American Cuisine recipes in database
    recipe_sasc = recipe.db.recipes.find()) # Variable to count South Asian Cuisine recipes in database
    

@app.route("/SimaRecipes/recipes")
def simasrecipe_project():
    projects = recipe.find(projection = recipe.FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    
    return render_template("index.html", json_projects=json_projects)
        

# Recipes page (recipes.html)    
@app.route("/recipes")
def recipes():
    
    return render_template("recipes.html", 
    page_title="Recipes", 
    recipes_veg = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Vegetable Recipes in database
    recipes_chick = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Chicken Recipes in database
    recipes_lamb = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Lamb Recipes in database
    recipes_seafood = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Sea Food Recipes in database
    recipes_beef = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Beef Recipes in database
    recipes_healthy = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Healthy Recipes in database
    recipes_vegan = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Vegan Recipes in database
    recipes_pork = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Pork Recipes in database
    recipes_amc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all American Cuisine Recipes in database
    recipes_auc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Australian Cuisine Recipes in database
    recipes_cdc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Canadian Cuisine Recipes in database
    recipes_cnc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Chinese Cuisine Recipes in database
    recipes_euc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all European Cuisine Recipes in database
    recipes_fec = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Far Eastern Cuisine Recipes in database
    recipes_mdc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Mediterranean Cuisine Recipes in database
    recipes_mec = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Middle Eastern Cuisine Recipes in database
    recipes_nac = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all North African Cuisine Recipes in database
    recipes_safc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all South African Cuisine Recipes in database
    recipes_samc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all South American Cuisine Recipes in database
    recipes_sasc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all South Asian Cuisine Recipes in database
    check_veg = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Vegetable Recipes in database
    check_chick = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Chicken Recipes in database
    check_lamb = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Lamb Recipes in database
    check_seafood = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Sea Food Recipes in database
    check_beef = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Beef Recipes in database
    check_healthy = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Healthy Recipes in database
    check_vegan = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Vegan Recipes in database
    check_pork = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Pork Recipes in database
    check_amc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all American Cuisine Recipes in database
    check_auc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Australian Cuisine Recipes in database
    check_cdc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Canadian Cuisine Recipes in database
    check_cnc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Chinese Cuisine Recipes in database
    check_euc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all European Cuisine Recipes in database
    check_fec = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Far Eastern Cuisine Recipes in database
    check_mdc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Mediterranean Cuisine Recipes in database
    check_mec = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Middle Eastern Cuisine Recipes in database
    check_nac = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all North African Cuisine Recipes in database
    check_safc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all South African Cuisine Recipes in database
    check_samc = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all South American Cuisine Recipes in database
    check_sasc = recipe.db.recipes.find().sort('recipe_name')) # Variable to list all South Asian Cuisine Recipes in database


# Contact Us page (contact.html)
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        
        # to display a verification message for sent email
        flash("Thanks {}, we have received your message!".format(
            request.form["name"]
        ))
        #print(request.form["name"])
    return render_template("contact.html", page_title="Contact")


# chat page (chat.html)
@app.route("/chat", methods = ["GET", "POST"])
def chat():
    if request.method == "POST":
        
        # To verify username in exiting session
        session["username"] = request.form["chatname"]
        
    if "username" in session:
        #return redirect (session["username"])
        # redirect to chat page
        return redirect (url_for("user", username = session["username"]))
        
    return render_template("chat.html")


# Username input (chat.html)    
@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    
    # Display chat Messages
    if request.method == "POST":
        username = session["username"] # Add username into variable
        message = request.form["chatmessage"] # store message(s) into variable
        add_messages(username, message) # stored username and message output
        #return redirect(session["username"])
        return redirect (url_for("user", username = session["username"]))
        
    return render_template("chat.html", username = username, chat_messages = messages)


@app.route('/newuser')
def newuser():
    return render_template('newuser.html')


# Intermediate page between Login and admin
@app.route('/loginuser')
def loginuser():
    '''return render_template("login.html")'''
    if not session.get('logged_in'): # check whether someone id logged in or not
        return render_template('login.html') # redirect to login page
    else:
        return redirect(url_for('admin')) # redirect to admin page


# Login page (login.html)
@app.route('/login', methods=['POST'])
def login():
    users = recipe.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        session['username'] = request.form['username']
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('admin'))        
        return redirect(url_for('admin'))
    return 'Invalid username/password combination'


# Logout route (Logout button on top of the Admin page)
@app.route("/logout")
def logout():
    session['logged_in'] = False # make session deactive and logout the user
    return redirect(url_for('loginuser')) # redirect to intermediate page/route


# Admin page (admin.html)
@app.route("/admin")
def admin():
    
    if 'username' in session:
        return render_template("admin.html", page_title ="Admin",
        categories = recipe.db.categories.find(), # Variable to list all Categories in the Database for combo box for adding new recipes 
        recipes = recipe.db.recipes.find().sort('recipe_name'), # Variable to list all Recipes in the Database for Admin page
        category = recipe.db.categories.find().sort('category_name'), # Variable to list all Categories in the Database for EDIT or DELETE on Admin page
        images = recipe.db.images.find().sort('recipe_image'), # Variable to list all Images in the Database for combo box for adding new recipes 
        cuisines = recipe.db.cuisines.find().sort('cuisine_name'), # Variable to list all Cuisines in the Database for combo box for adding new recipes 
        cuisines_list = recipe.db.cuisines.find().sort('cuisine_name'), # Variable to list all Cuisines in the Database for EDIT or DELETE on Admin page
        username = session["username"])
    
    return render_template('login.html')
    
    
# Insert user to database (admin.html)
@app.route("/insert_user", methods=["POST","GET"])
def insert_user():
    if request.method == 'POST':
        users = recipe.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'email' : request.form['useremail'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for("admin"))
        
        return 'Username Already Exists'
    
    return render_template('newuser.html')


# Insert recipe to Database (admin.html)
@app.route("/insert_recipe", methods=["POST"])
def insert_recipe():
    addrecipes = recipe.db.recipes
    addrecipes.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))
  
  
# Insert category to database (admin.html)
@app.route("/insert_category", methods=["POST"])
def insert_category():
    addcategory = recipe.db.categories
    addcategory.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))
    

# Insert Cuisine to database (admin.html)
@app.route("/insert_cuisine", methods=["POST"])
def insert_cuisine():
    addcuisine = recipe.db.cuisines
    addcuisine.insert_one(request.form.to_dict())
    return redirect(url_for("admin"))


# Edit recipe (admin.html)
@app.route("/edit_recipe/<task_id>")
def edit_recipe(task_id):
    the_recipe = recipe.db.recipes.find_one({"_id": ObjectId(task_id)}) # fetch data from database with help of unique ID
    all_categories = recipe.db.categories.find() # Variable to list all categories in th databse
    all_images = recipe.db.images.find() # Variable to list all images in th databse
    all_cuisines = recipe.db.cuisines.find().sort('cuisine_name')  # Variable to list all cuisines in th databse
    return render_template("editrecipe.html", page_title="Edit Recipe", 
    recipe = the_recipe, # variable to store all fetched recipes 
    categories = all_categories,  # variable to store all fetched categories  
    images = all_images,  # variable to store all fetched images 
    cuisines = all_cuisines) # variable to store all fetched cuisines 
    
# Edit Category (admin.html)
@app.route("/edit_category/<cat_id>")
def edit_category(cat_id):
    return render_template("editcategory.html", 
    page_title="Edit Category", 
    category = recipe.db.categories.find_one({'_id': ObjectId(cat_id)})) # Variable to fetch and store particular category base on uniquie ID
    
# Edit Cuisine (admin.html)
@app.route("/edit_cuisine/<cus_id>")
def edit_cuisine(cus_id):
    return render_template("editcuisine.html", 
    page_title="Edit Cuisine", 
    cuisines = recipe.db.cuisines.find_one({'_id': ObjectId(cus_id)})) # Variable to fetch and store particular cuisine base on uniquie ID


# Update recipe (editrecipe.html)
@app.route("/update_recipe/<task_id>", methods=["POST"])
def update_recipe(task_id):
    updaterecipe = recipe.db.recipes
    updaterecipe.update({'_id': ObjectId(task_id)}, # Update data in the database based on uniq ID
    {
        'recipe_name': request.form.get('recipe_name'), # Fetch updated data from input field and store in the right field in the databse
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
 

# Update Category (editcategory.html)
@app.route("/update_category/<cat_id>", methods=["POST"])
def update_category(cat_id):
    updatecategory = recipe.db.categories
    updatecategory.update({'_id': ObjectId(cat_id)}, # Update data in the database based on uniq ID
    {
        'category_name' : request.form.get('category_name') # Fetch updates category from input field and store in the right field in the databse
    })
    return redirect(url_for('admin'))


# Update Cuisine (editcuisine.html)    
@app.route("/update_cuisine/<cus_id>", methods=["POST"])
def update_cuisine(cus_id):
    updatecuisine = recipe.db.cuisines
    updatecuisine.update({'_id': ObjectId(cus_id)}, # Update data in the database based on uniq ID
    {
        'cuisine_name' : request.form.get('cuisine_name') # Fetch updated cuisine from input field and store in the right field in the databse
    })
    return redirect(url_for('admin'))


# Delete Recipe (admin.html)
@app.route('/delete_recipe/<task_id>')
def delete_recipe(task_id):
    recipe.db.recipes.remove({'_id': ObjectId(task_id)}) # Delete perticular recipe from database based on uniq ID
    return redirect(url_for('admin'))
    
    
# Delete Category (admin.html)
@app.route('/delete_category/<cat_id>')
def delete_category(cat_id):
    recipe.db.categories.remove({'_id': ObjectId(cat_id)}) # Delete perticular category from database based on uniq ID
    return redirect(url_for('admin'))
    

# Delete Cuisine (admin.html)
@app.route('/delete_cuisine/<cus_id>')
def delete_cuisine(cus_id):
    recipe.db.cuisines.remove({'_id': ObjectId(cus_id)}) # Delete perticular cuisine from database based on uniq ID
    return redirect(url_for('admin'))


# Beef Recipe View (beef.html)
@app.route('/beef')
def beef():
    return render_template("beef.html",
    page_title = 'Beef Recipes', 
    beef_recipe = recipe.db.recipes.find().sort('recipe_name'),
    beef_check = recipe.db.recipes.find().sort('recipe_name'))


# Chicken Recipe View (chicken.html)
@app.route('/chicken')
def chicken():
    return render_template("chicken.html",
    page_title = 'Chicken Recipes', 
    chick_recipe = recipe.db.recipes.find().sort('recipe_name'),
    chick_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Healthy Recipe View (healthy.html)
@app.route('/healthy')
def healthy():
    return render_template("healthy.html",
    page_title = 'Healthy Recipes', 
    healthy_recipe = recipe.db.recipes.find().sort('recipe_name'),
    healthy_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Lamb Recipe View (lamb.html)
@app.route('/lamb')
def lamb():
    return render_template("lamb.html",
    page_title = 'Lamb Recipes', 
    lamb_recipe = recipe.db.recipes.find().sort('recipe_name'),
    lamb_check = recipe.db.recipes.find().sort('recipe_name'))


# Pork Recipe View (pork.html)
@app.route('/pork')
def pork():
    return render_template("pork.html",
    page_title = 'Pork Recipes', 
    pork_recipe = recipe.db.recipes.find().sort('recipe_name'),
    pork_check = recipe.db.recipes.find().sort('recipe_name'))    



# Sea Food Recipe View (seafood.html)
@app.route('/seafood')
def seafood():
    return render_template("seafood.html",
    page_title = 'Sea Food Recipes', 
    seafood_recipe = recipe.db.recipes.find().sort('recipe_name'),
    seafood_check = recipe.db.recipes.find().sort('recipe_name'))


# Vegan Recipe View (vegan.html)
@app.route('/vegan')
def vegan():
    return render_template("vegan.html",
    page_title = 'Vegan Recipes', 
    vegan_recipe = recipe.db.recipes.find().sort('recipe_name'),
    vegan_check = recipe.db.recipes.find().sort('recipe_name'))


# Vegetable Recipe View (veg.html)
@app.route('/veg')
def veg():
    return render_template("veg.html",
    page_title = 'Vegetable Recipes', 
    veg_recipe = recipe.db.recipes.find().sort('recipe_name'),
    veg_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Under 30 mins Recipe View (u30.html)
@app.route('/u30')
def u30():
    return render_template("u30.html",
    page_title = 'Recipes Under 30 Mins to Cook', 
    u30_recipe = recipe.db.recipes.find().sort('recipe_name'),
    u30_check = recipe.db.recipes.find().sort('recipe_name'))


# Over 30 mins Recipe View (o30.html)
@app.route('/o30')
def o30():
    return render_template("o30.html",
    page_title = 'Recipes Over 30 Mins to Cook', 
    o30_recipe = recipe.db.recipes.find().sort('recipe_name'),
    o30_check = recipe.db.recipes.find().sort('recipe_name'))    

    
# American Cuisine View (american.html)
@app.route('/american')
def american():
    return render_template("american.html",
    page_title = 'American Cuisines',
    amc_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    amc_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Australian Cuisine View (australian.html)    
@app.route('/australian')
def australian():
    return render_template("australian.html",
    page_title = 'Australian Cuisines',
    aus_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    aus_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Canadian Cuisine View (canadian.html)    
@app.route('/canadian')
def canadian():
    return render_template("canadian.html",
    page_title = 'Canadian Cuisines',
    cnd_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    cnd_check = recipe.db.recipes.find().sort('recipe_name'))
    
    
# Chinese Cuisine View (chinese.html)    
@app.route('/chinese')
def chinese():
    return render_template("chinese.html",
    page_title = 'Chinese Cuisines',
    cnc_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    cnc_check = recipe.db.recipes.find().sort('recipe_name'))
    
    
# European Cuisine View (earopean.html)
@app.route('/european')
def european():
    return render_template("european.html",
    page_title = 'European Cuisines',
    eur_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    eur_check = recipe.db.recipes.find().sort('recipe_name'))
    

# Far Eastern Cuisine View (fareastern.html)
@app.route('/fareastern')
def fareastern():
    return render_template("fareastern.html",
    page_title = 'Far Eastern Cuisines',
    fre_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    fre_check = recipe.db.recipes.find().sort('recipe_name'))


# Mediterranean Cuisine View (mediterranean.html)
@app.route('/mediterranean')
def mediterranean():
    return render_template("mediterranean.html",
    page_title = 'Mediterranean Cuisines',
    mdt_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    mdt_check = recipe.db.recipes.find().sort('recipe_name'))


# Middel Eastern Cuisine View (middleeastern.html)
@app.route('/middleeastern')
def middleeastern():
    return render_template("middleeastern.html",
    page_title = 'Middle Eastern Cuisines',
    mde_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    mde_check = recipe.db.recipes.find().sort('recipe_name'))


# North African Cuisine View (northafrican.html)
@app.route('/northafrican')
def northafrican():
    return render_template("northafrican.html",
    page_title = 'North African Cuisines',
    naf_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    naf_check = recipe.db.recipes.find().sort('recipe_name'))


# South African Cuisine View (southafrican.html)
@app.route('/southafrican')
def southafrican():
    return render_template("southafrican.html",
    page_title = 'South African Cuisines',
    saf_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    saf_check = recipe.db.recipes.find().sort('recipe_name'))


# South American Cuisine View (southamerican.html)
@app.route('/southamerican')
def southamerican():
    return render_template("southamerican.html",
    page_title = 'South American Cuisines',
    sam_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    sam_check = recipe.db.recipes.find().sort('recipe_name'))


# South Asian Cuisine View (southasian.html)
@app.route('/southasian')
def southasian():
    return render_template("southasian.html",
    page_title = 'South Asian Cuisines',
    sas_cuisine = recipe.db.recipes.find().sort('recipe_name'),
    sas_check = recipe.db.recipes.find().sort('recipe_name'))



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
            debug=False)