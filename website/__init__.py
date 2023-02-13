from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()

# Database file name
DB_TL_IL = "database.db"

def create_app():
    # Create Flask object
    app = Flask(__name__)
    
    # Set secret key for the application
    app.config['SECRET_KEY'] = 'Ilokano to Tagalog Machine Translation'
    
    # Set SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_TL_IL}'
    
    # Initialize SQLAlchemy with the Flask application
    db.init_app(app)
    
    # Import views module from the same package
    from .views import views
    
    # Register the views blueprint with the application
    app.register_blueprint(views, url_prefix='/')
    
    return app