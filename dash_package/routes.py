from flask import render_template, jsonify, json
# from flask import Flask
# from dash_package.models import Listing

from dash_package.__init__ import *
import pdb
from dash_package.models import *


# @server.route('/')
# def render_apartments():
#     brand = Brands.query.first()
#     return brand.name

@app.server.route('/dashboard')
def test():
    return Brands.query.all()




# if __name__ == '__main__':
#     app.run(debug=True)
