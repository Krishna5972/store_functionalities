from flask import Flask, render_template, request
import json


app = Flask(__name__)

from modules.functions import make_sum

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/adjust", methods=["POST"])
def adjust():
    hundreds = int(request.form["hundreds"])
    fifties = int(request.form["fifties"])
    twenties = int(request.form["twenties"])
    twenties = int(request.form["twenties"])
    tens = int(request.form["tens"])
    fives = int(request.form["fives"])
    ones = int(request.form["ones"])
    quarters = int(request.form["quarters"])
    dimes = int(request.form["dimes"])
    twos = int(request.form["twos"])


    initial_sum,safe_drop_sum,remaining_counter,currency = make_sum(hundreds,fifties,twenties,tens,fives,twos,ones,quarters,dimes)
    
    return render_template("adjust.html", initial_sum=initial_sum,safe_drop_sum=safe_drop_sum,remaining_counter=remaining_counter,currency=currency)

if __name__ == "__main__":
    app.run()
