from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Routes.AtivoRoute import ativoRoute
from Routes.NegociacaoRoute import negociacaoRoute
from Routes.UsuarioRoute import usuarioRoute

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(ativoRoute, url_prefix='/Ativos')
app.register_blueprint(negociacaoRoute, url_prefix='/Negociacoes')
app.register_blueprint(usuarioRoute, url_prefix='/Usuarios')

@app.route('/')
def index():
    return render_template('Usuario/Login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
