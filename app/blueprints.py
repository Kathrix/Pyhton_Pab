from flask import Blueprint, make_response, render_template

bp = Blueprint("App", __name__)

@bp.route('/')
@bp.route('/home')
def homepage():
    return make_response(
        render_template("home.html"),
        200
    )
