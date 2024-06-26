#!/usr/bin/env python3

from app import app, db
from models import User, Game, Review

# Ensure all models are imported for the interactive debugger to access them
from models import *

if __name__ == '__main__':
    # Use app_context to work within the Flask application context
    with app.app_context():
        # Initialize the database if necessary
        db.init_app(app)
        
        # Create all database tables if they do not exist
        db.create_all()

        # Insert any initialization data or debugging setup here
        # For example, you can create a user for testing purposes
        # user1 = User(name='John Doe', email='john.doe@example.com')
        # db.session.add(user1)
        # db.session.commit()

        # Start an interactive debugger session
        import ipdb; ipdb.set_trace()
