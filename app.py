from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json
import random


# initialise Users database
app = Flask(__name__)
usersdb = {}
with open('users.json') as fp:
    usersdb = json.load(fp)


# initialise Items dtabase
app = Flask(__name__)
itemsdb = {}
with open('items.json') as fp:
    itemsdb = json.load(fp)


# Secret key for flash messages
app = Flask(__name__)
app.secret_key = b'laksdfoi323d'

# function to save users
def save_users():
    with open('users.json', 'w') as fp:
        json.dump(usersdb, fp)

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

# browse items list
@app.route('/items/browse')
def browse_items():
    return render_template('browse_items.template.html', all_items=itemsdb)


# view single item details
@app.route('/items/<int:item_id>')
def view_item_details(item_id):
    item_to_view = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            item_to_view = each_item
            break

    if item_to_view:
        return render_template('item_details.template.html',
                                item=item_to_view)

    else:
        return render_template('item_notfound.template.html',
                                item=item_id)


@app.route('/items/post')
def show_post_item():
    return render_template('post_item.template.html')

@app.route('/items/post', methods = ['POST'])
def process_post_item():
    print(request.form)
    itemsdb.append({
        'id': random.randint(1000,9999),
        'name': request.form.get('item_name'),
        'description': request.form.get('description'),
        'age': request.form.get('age'),
        'condition': request.form.get('condition'),
        'delete': request.form.get('delete_after')
    })

    save_items()

    return redirect(url_for('item_list'))

@app.route('/items/listings')
def item_list():
    return render_template('item_listings.template.html', all_items=itemsdb)


@app.route('/items/<int:item_id>/edit')
def show_edit_items(item_id):
    item_to_edit = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            item_to_edit = each_item
            break

    if item_to_edit:
        return render_template('edit_item.template.html',
                                item=item_to_edit)

    else:
        return render_template('item_notfound.template.html',
                                item_id=item_id)



@app.route('/item/<int:item_id>/edit', methods=['POST'])
def process_edit_food(item_id):
    item_to_edit = None
    for each_item in itemsdb:
        if each_item["id"] == item_id:
            item_to_edit = each_item
            break

    if item_to_edit:
        item_to_edit["name"] = request.form.get('item_name')
        item_to_edit["description"] = request.form.get('description')
        item_to_edit["age"] = request.form.get('age')
        item_to_edit["condition"] = request.form.get('condition')
        item_to_edit["delete"] = request.form.get('delete_after')

        save_items()
       
        flash(
            f"The food {food_to_edit['name']}"
            f"  has been edited successfully")
        return redirect(url_for('item_list'))

    else: 
        return render_template('item_notfound.template.html',
                                item=item_id)


@app.route('/items/<int:item_id>/delete')
def show_delete_items(item_id):
    item_record = None
    #linear search
    for item_record in itemsdb:
        if item_record['id'] == item_id:
            item_to_delete = item_record
            break

    if item_record:
        return render_template('show_delete_item.template.html', item=item_to_delete)

# @app.route('/foods/<int:food_id>/delete', methods=['POST'])
# def process_show_delete_food(food_id):
#     # initialise food_to_delete to None as this will eventually be a dictionary
#     food_to_delete = None 

#     # linear search (search one by one)
#     for food_record in databsse:
#         if food_record['id'] == food_id:
#             food_to_delete = food_record['id']
#             break

#     if food_to_delete:
#         database.remove(food_to_delete)

#         with open('food.json', 'w') as fp:
#             json.dump(database, fp)

#         return redirect(url_for('show_food'))
    
#     else:
#         return f"The food record with the id of {food_id} is not found."

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # only one program can run on one port, therefore flask gives error if it is run 2nd time
            port=int(os.environ.get('PORT')),
            debug=True)
