from flask import Blueprint

main = Blueprint('main', __name__)

# import views using blueprint
from . import routes
