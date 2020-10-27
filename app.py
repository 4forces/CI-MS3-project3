from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random
from flask_pymongo import PyMongo
from bson.objectid import ObjectId



# for env.py set up
if os.path.exists("env.py"):
    import env
# bson.json converts the mongo format to json for workability
from bson.json_util import dumps, loads
app = Flask(__name__)

# to set the DB and the URI
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print(os.environ.get("MONGO_URI"))
# to set the mongo object
mongo = PyMongo(app)


# initialise Items dtabase
app = Flask(__name__)
itemsdb = {}
with open('items.json') as fp:
    itemsdb = json.load(fp)


# Secret key for flash messages
app = Flask(__name__)
app.secret_key = b'laksdfoi323d'


# function to save items
def save_items():
    with open('items.json', 'w') as fp:
        json.dump(itemsdb, fp)


@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/register')
def register():
    return render_template('register.template.html')


@app.route('/login')
def login():
    return render_template('login.template.html')


# display all items list - vistor view
@app.route('/items/browse')
def browse_items():
    items = list(mongo.db.items.find())
    return render_template('browse_items.template.html', items_stored=items)

# display all items list - login view
@app.route('/items/listings')
def item_list():
    items = list(mongo.db.items.find())
    return render_template('item_listings.template.html', all_items=items)


# view item details
@app.route('/items/<item_id>')
def view_item_details(item_id):
    print(request.form)
    selected_item = None
    items = list(mongo.db.items.find())
    for each_item in items:
        if each_item["_id"] == item_id:
            selected_item = each_item
            break

    if selected_item:
        return render_template('item_details.template.html', item=selected_item)
    else:
        return render_template('item_notfound.template.html', item_id=item_id)


# add item - with ['POST']
@app.route('/items/post')
def show_post_item():
    return render_template('post_item.template.html')

@app.route('/items/post', methods=['POST'])
def process_post_item():
    print(request.form)
    item = {
        'name': request.form.get('item_name'),
        'description': request.form.get('description'),
        'age': request.form.get('age'),
        'condition': request.form.get('condition'),
        'delete': request.form.get('delete_after')
    }
    mongo.db.items.insert_one(item)
    flash("Item Successfully Added") # Error - Does not show
    return redirect(url_for('show_post_item'))


# edit item - with ['POST']
@app.route('/items/<item_id>/edit')
def show_edit_items(item_id):
    print(request.form)
    selected_item = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            selected_item = each_item
            break

    if selected_item:
        return render_template('edit_item.template.html', item=selected_item)

    else:
        return render_template('item_notfound.template.html',
                               item_id=item_id)



@app.route('/items/<int:item_id>/edit', methods=['POST'])
def process_edit_item(item_id):
    print(request.form)
    selected_item = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            selected_item = each_item
            break

    if selected_item:
        selected_item["name"] = request.form.get('item_name')
        selected_item["description"] = request.form.get('description')
        selected_item["age"] = request.form.get('age')
        selected_item["condition"] = request.form.get('condition')
        selected_item["delete"] = request.form.get('delete_after')
        save_items()
        flash(
            f"Item {selected_item['name']}"
            f"  has been edited successfully.")
        return redirect(url_for('item_list'))

    else:
        return render_template('item_notfound.template.html',
                               item_id=item_id)


# delete item - with ['POST']
@app.route('/items/<int:item_id>/delete')
def show_delete_items(item_id):
    print(request.form)
    selected_item = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            selected_item = each_item
            break

    if selected_item:
        return render_template('show_delete_item.template.html',
                               item=selected_item)

    else:
        return render_template('item_notfound.template.html',
                               item_id=item_id)


@app.route('/items/<int:item_id>/delete', methods=['POST'])
def process_show_delete_item(item_id):
    selected_item = None
    for each_item in itemsdb:
        if each_item['id'] == item_id:
            selected_item = each_item['id']
            break

    if selected_item:
        itemsdb.remove(each_item)
        save_items()
        return redirect(url_for('item_list'))

    else:
        return render_template('item_notfound.template.html', item_id=item_id)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port, 
            # therefore flask gives error 
            # if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
