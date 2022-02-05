from flask import Flask

from .blueprints import bp

app = Flask(__name__)
app.register_blueprint(bp)

