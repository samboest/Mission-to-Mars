from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#required flask syntax

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#defining the route

    #This route, @app.route("/"), tells Flask what to display when we're looking at the home page, 
    # index.html (index.html is the default HTML file that we'll use to display the content we've 
    # scraped). This means that when we visit our web app's HTML page, we will see the home page.

@app.route("/")
def index():
   mars_app = mongo.db.mars_app.find_one()
   return render_template("index.html", mars_app=mars_app)

   # next rought and function

@app.route("/scrape")
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars_app
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()

