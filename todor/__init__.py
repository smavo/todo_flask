from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    # Configuración del poyecto
    app.config.from_mapping(
        DEBUG=False,
        SECRET_KEY='smavodev',
    )

    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

