from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from marshmallow import Schema, fields, pprint
from datetime import datetime
import sys
import os


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, supports_credentials=True)

# Init app
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
ma = Marshmallow(app)


# sanity check route
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# * Models

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username,
        self.password = password


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(150))
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, nullable=False)
    date_due = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey(
        'customers.id'), nullable=False)
    customer = db.relationship("Customer", backref="customer")
    total = db.Column(db.Float)

    def __init__(self, date_created, date_due, notes, customer_id, total):
        self.date_created = date_created
        self.date_due = date_due
        self.notes = notes
        self.customer_id = customer_id
        self.total = total


class Transaction(db.Model):
    __tablename__ = 'Transactions'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, unique=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey(
        'invoices.id'), nullable=False)
    invoice = db.relationship("Invoice", backref="invoices")    
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    product = db.relationship("Product", backref="transactions")

    def __init__(self, date_created, quantity, invoice_id, product):
        self.date_created = date_created
        self.quantity = quantity
        self.invoice_id = invoice_id
        self.product_id = product


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, unique=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class ProductSchema(Schema):
    class Meta:
        model = Product


class TransactionSchema(Schema):
    class Meta:
        model = Transaction
    invoice = fields.Nested(lambda: InvoiceSchema(only=(None)))


class InvoiceSchema(Schema):
    id = fields.Int(dump_only=True)
    customer = fields.Nested(lambda: CustomerSchema(exclude=("customer",)))
    date_created = fields.DateTime(required=True)
    date_due = fields.DateTime(required=True)
    transactions = fields.List(fields.Nested(TransactionSchema(many=True,only=(None))))

class CustomerSchema(Schema):
    class Meta:
        model = Customer
    invoices = fields.List(fields.Nested(InvoiceSchema(many=True,only=(None))))




#* API methods ###################


# * Create Customer
@app.route('/api/customer', methods=['POST'])
def add_Customer():
    name = request.json['name']
    address = request.json['address']
    
    customer = Customer(name, address)
    db.session.add(customer)
    db.session.commit()

    return jsonify({'message': 'New Customer Created'})


# * Get All Customers
@app.route('/api/customer', methods=['GET'])
def get_products():
    customers = Customer.query.all()
    output = []

    for customer in customers:
        customer_data = {}
        customer_data['id'] = customer.id
        customer_data['name'] = customer.name
        customer_data['address'] = customer.address
        output.append(customer_data)

    return jsonify({'customers': output})


# * Get Customer
@app.route('/api/customer/<id>', methods=['GET'])
def get_Customer(id):
    customer = Customer.query.get(id)

    customer_data = {}

    customer_data['id'] = customer.id
    customer_data['name'] = customer.name
    customer_data['address'] = customer.address

    return jsonify({'customer': customer_data})


# * Update a Customer
@app.route('/api/customer/<id>', methods=['PUT'])
def update_Customer(id):
    customer = Customer.query.get(id)

    name = request.json['name']
    address = request.json['address']

    customer.name = name
    customer.address = address

    customer_data = {}
    customer_data['id'] = customer.id
    customer_data['name'] = customer.name
    customer_data['address'] = customer.address

    db.session.commit()

    return jsonify({'customer': 'Updated'})


# * Delete Customer
@app.route('/api/customer/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()

    return jsonify({'message': 'Deleted Customer'})

# * Products ***********************

# * Create Product
@app.route('/api/product', methods=['POST'])
def add_Product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    product = Product(name, description, price)
    db.session.add(product)
    db.session.commit()

    return jsonify({'product': 'New Product Created'})


# * Get All Products
@app.route('/api/product', methods=['GET'])
def get_Products():
    products = Product.query.all()
    output = []

    for product in products:
        product_data = {}
        product_data['id'] = product.id
        product_data['name'] = product.name
        product_data['description'] = product.description
        product_data['price'] = product.price
        output.append(product_data)

    return jsonify({'products': output})

    # * Get Product


@app.route('/api/product/<id>', methods=['GET'])
def get_Product(id):
    product = Product.query.get(id)

    product_data = {}

    product_data['id'] = product.id
    product_data['name'] = product.name
    product_data['description'] = product.description
    product_data['price'] = product.price

    return jsonify({'customer':  product_data})


# * Update a Product
@app.route('/api/product/<id>', methods=['PUT'])
def update_Product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    product.name = name
    product.description = description
    product.price = price
    
    product_data = {}
    product_data['id'] = product.id
    product_data['name'] = product.name
    product_data['description'] = product.description
    product_data['price'] = product.price

    db.session.commit()

    return jsonify({'customer': 'Updated'})


# * Delete Product
@app.route('/api/product/<id>', methods=['DELETE'])
def delete_Product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Deleted Product'})


#*Item API ###########################
@app.route('/api/transaction', methods=['POST'])
def add_Transaction():
    date_created = date.today()
    quantity = request.json['quantity']
    invoice_id = request.json['invoice_id']
    product_id = request.json['product_id']

    transaction = Transaction(date_created, quantity, invoice_id, product_id)
    db.session.add(transaction)
    db.session.commit()

    return jsonify({'transaction': 'New Transaction Created'})

#*Invoice ###########################


@app.route('/api/invoice', methods=['POST'])
def add_Invoice():
    date_created = request.json['date_created']
    date_due = request.json['date_due']
    notes = request.json['notes']
    customerId = request.json['customer_id']
    total = request.json['total']

    date1 = datetime.strptime(date_created, "%Y/%m/%d")
    date2 = date1 = datetime.strptime(date_due, "%Y/%m/%d")
    
    invoice = Invoice(date1, date2,notes, customerId, total)
    db.session.add(invoice)
    db.session.commit()

    return jsonify({'invoice': 'New Invoice Created'})


@app.route('/api/invoice', methods=['GET'])
def get_Invoices():
    invoices = Invoice.query.all()
    output = []

    for invoice in invoices:
        invoice_data = {}
        invoice_data['id'] = invoice.id
        invoice_data['date_created'] = invoice.date_created
        invoice_data['customer_id'] = invoice.customer_id
        invoice_data['total'] = invoice.total
        output.append(invoice_data)

    return jsonify({'invoices': output})


@app.route('/api/invoice/<id>', methods=['GET'])
def delete_Invoice(id):
    invoice = Invoice.query.get(id)
    db.session.delete(invoice)
    db.session.commit()

    return jsonify({'message': 'Deleted Invoice'})


# *END OF API****************
    # * Run Server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
    print("Server running")
