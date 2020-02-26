import os
from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "SimaRecipes"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")

mongo = PyMongo(app)

def mongo_connect(url):
    try:
        conn = PyMongo.MongoClient(url)
        #print("Mongo is Connected!")
        return conn
    except PyMongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

@app.route('/description')
def index():
    return'''
        <form method="POST" action = "/create" encrypt="multipart.form-data">
            <input type="text" name = "username">
            <input type="file" name="profile_image">
            <input type="submit">
        </form>
    '''
    
@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name' : profile_image.filename})
        
    return 'Done'