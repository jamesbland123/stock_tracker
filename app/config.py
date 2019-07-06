import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# mysql connection string: 'mysql+pymysql://username:password@localhost/db_name'
mysql_uri = 'mysql+pymysql://' + os.environ["DB_USER"] + ':' + \
    os.environ["DB_PASSWORD"] + '@' + os.environ["DB_HOST"] + \
    '/stock_tracker'

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'stock_tracker.db')
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)