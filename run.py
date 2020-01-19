import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1,2,3])
    
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        flash("Thanks {}, we have received your message!".format(
            request.form["name"]
        ))
        #print(request.form["name"])
    return render_template("contact.html", page_title="Contact")
    
@app.route("/recipes")
def recipes():
    data=[]
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipes.html", page_title="Recipes", recipes=data)
    
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
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)