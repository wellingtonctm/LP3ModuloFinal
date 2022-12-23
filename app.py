import os

from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate

from Data.DbContext import db

from Routes.AtivoRoute import ativoRoute
from Routes.NegociacaoRoute import negociacaoRoute
from Routes.UsuarioRoute import usuarioRoute

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Data', "myBase.db")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(ativoRoute, url_prefix='/Ativos')
app.register_blueprint(negociacaoRoute, url_prefix='/Negociacoes')
app.register_blueprint(usuarioRoute, url_prefix='/Usuarios')

@app.route('/')
def index():
    return redirect(url_for('UsuarioRoute.login'))

if __name__ == '__main__':
    app.debug = True
    app.run()