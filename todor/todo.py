from flask import Blueprint, render_template
from .models import Todo
from todor import db
from todor.auth import login_required

bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos=todos)


