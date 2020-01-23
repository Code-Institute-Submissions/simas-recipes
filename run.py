import os
import json
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "recipechat")

messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    #messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append({"timestamp": now, "from": username, "message": message})

#def get_all_messages():
#    """Get all the messages and separate them with 'br'"""
#    return "<br>".join(messages)

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

"""@app.route("/<username>/<message>")
def send_message(username, message):
    add_messages(username, message)
    return redirect("/" + username)
"""

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
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=False)