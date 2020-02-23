import os
import pymongo
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "SimaRecipes"
COLLECTION_NAME = "recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        #print("Mongo is Connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a Recipe")
    print("2. Find a Recipe by name")
    print("3. Edit a Recipe")
    print("4. Delete a Recipe")
    print("5. Exit")
    
    option = input("Choose option: ")
    return option

def get_record():
    print("")
    name = input("Enter Recipe Name: ")
    
    try:
        recip = coll.find_one({'name': name.lower()})
    except:
        print("Error accessing the Database")
    if not recip:
        print("")
        print("Error! No Recipe found.")
    return recip

def add_record():
    print("")
    name = input("Enter Recipe Name: ")
    requirement = input("Enter required ingredients: ")
    method = input("Enter Method of Cooking: ")
    doc = input("Enter date of Creation: ")
    
    new_recipe = {'name': name.lower(), 'requirement': requirement, 'method': method, 'doc': doc}
    
    try:
        coll.insert(new_recipe)
        print("")
        print("Recipe Inserted")
    except:
        print("Error accessing the Database")
        
def find_recipe():
    recip = get_record()
    if recip:
        print("")
        for k, v in recip.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
def edit_recipe():
    recip = get_record()
    if recip:
        update_recip={}
        print("")
        for k, v in recip.items():
            if k != "_id":
                update_recip[k] = input(k.capitalize() + " [" + v + "]: ")
                if update_recip[k] == "":
                    update_recip[k] = v
        
        try:
            coll.update_one(recip,{'$set': update_recip})
            print("")
            print("Document Updated")
        except:
            print("Erroe accessing th database")
                
def delete_recipe():
    recip = get_record()
    if recip:
        print("")
        for k, v in recip.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
        
        print("")
        confirmation = input("Is this the RECIPE you like to Remove (Y/N): ")
        print("")
        if confirmation.lower() == "y":
            try:
                coll.remove(recip)
                print("Recipe Removed")
            except:
                print("Error accessing the Database")
        else:
            print("Recipe not Removed")


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            #print("You have selected option 1")
            add_record()
        elif option == '2':
            find_recipe()
        elif option == '3':
            edit_recipe()
        elif option == '4':
            delete_recipe()
        elif option == '5':
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
    

#new_recipe = {'name': 'Moroccan Lamb', 'requirement': '500g lamb, neck fillets, cut into bite-size pieces, 2 tsp paprika, 3 tsp ground cinnamon, 2 x 400g/14oz cans chopped tomato with olive oil and garlic, 1 tbsp finely chopped parsley, plus extra to serve', 'method': 'Heat a large, non-stick frying pan. Cook the lamb well on all sides without adding extra oil. Tip in the spices, then fry for 1 min more until aromatic, Pour in the chopped tomatoes and parsley, bring to the boil, then simmer gently, with a lid on, for 30 mins or until the lamb is tender. Serve sprinkled with more parsley.', 'doc': '08/02/2020'}

#coll.remove({'name': 'Moroccan Lamb'})
#coll.insert(new_recipe)

#recipes = coll.find()

#for recipe in recipes:
#    print(recipe)