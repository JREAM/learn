from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "blog"}
app.config["SECRET_KEY"] = "p00py"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from blog.views import posts
    from blog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
