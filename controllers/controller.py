from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return "Hello"

@app.route('/orders')
def get_orders():
    return render_template('orders_all.html', title='Orders', orders=orders)

@app.route('/orders/<index>')
def get_specific_order(index):
    order_index = int(index) - 1
    return render_template('orders_specific.html', title=f'Order', order=orders[order_index])
