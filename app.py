from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask("myapp")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"
mongo = PyMongo(app)
customer_collection = mongo.db.customers


@app.route("/read")
def read_data():
    customer = (customer_collection.find())
    return render_template('index.html', customer=customer)


@app.route("/form")
def form():

    return render_template('form.html')


@app.route("/data", methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("x")
        phone = request.args.get("y")
        loc = request.args.get("z")
        if name != "" and phone != "" and loc != "":
            customer = customer_collection.insert_one(
                {"name": name, "phone": phone, "location": loc})
            return ("data added to the database")
        else:
            return ("Kindly fill the form")


@app.route("/delete")
def delete():
    customer_collection.remove({})
    return "All data deleted"


app.run(debug=True)
