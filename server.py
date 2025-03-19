from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def sakums():
    gads= datetime.datetime.now().year
    rand_skaitlis = random.randint (1, 10)
    return render_template('index.html', skaitlis=rand_skaitlis, gads=gads)
    
@app.route("/minejums/<vards>")
def minejums(vards):
    saite = f"https://api.genderize.io?name={vards}"
    atbilde = requests.get(saite).json()
    dzim = atbilde["gender"]
    # if vards[-1] == "a" or vards[-1] == "e":
    #     dzim = "sieviete"
    # if vards[-1] == "s" or vards[-1]== "o": 
    #     dzim = "vīrietis"
    saite_age = f"https://api.agify.io?name={vards}"
    atbilde_age = requests.get(saite_age).json()
    pers_age = atbilde_age["age"]
    return render_template ('minejums.html', pers_vards=vards, dzimums = dzim, age = pers_age )

@app.route("/blogs")
def blogs():
      saite_blogs = f"https://api.npoint.io/c790b4d5cab58020d391"
      atbilde_blogs = requests.get(saite_blogs).json()
      return render_template ('blogs.html', ieraksti=atbilde_blogs)

if __name__ == "__main__":
    app.run(debug = True)