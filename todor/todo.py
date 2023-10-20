from flask import Blueprint, render_template


bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/register')
def register():
    return render_template('auth/register.html')
