from app import app
import os
# from flaskblog import create_app

# app = create_app()

if __name__ == '__main__':
    app.run(port=8080, debug = True)