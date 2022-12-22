from flask import Blueprint

from Controllers.UsuarioController import getAll, login, create, delete, logout

usuarioRoute = Blueprint('UsuarioRoute', __name__)

usuarioRoute.route('/', methods=['GET'])(getAll)
usuarioRoute.route('/Login', methods=['GET', 'POST'])(login)
usuarioRoute.route('/Logout', methods=['GET', 'POST'])(logout)
usuarioRoute.route('/Criar', methods=['POST'])(create)
usuarioRoute.route('/Excluir', methods=['POST'])(delete)