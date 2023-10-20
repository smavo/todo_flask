from flask import Blueprint, render_template

from .models import Todo, User
from todor import db

from .models import Todo
from todor import db

bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('/list')
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos=todos)


