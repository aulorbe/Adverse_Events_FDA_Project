from flask import render_template
# from flask import Flask
# from dash_package.models import Listing
from dash_package import server
import pdb
from dash_package.models import *


# @server.route('/')
# def render_apartments():
#     brand = Brands.query.first()
#     return brand.name

@server.route('/'):
def test():
    return db.session.query(Brands).all()

    # return render_template('index.html', apartments = apartments)


# if __name__ == '__main__':
#     app.run(debug=True)
