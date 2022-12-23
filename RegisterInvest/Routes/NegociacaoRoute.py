from flask import Blueprint

from Controllers.NegociacaoController import getAll, create, delete

negociacaoRoute = Blueprint('NegociacaoRoute', __name__)

negociacaoRoute.route('/', methods=['GET'])(getAll)
negociacaoRoute.route('/Criar', methods=['POST'])(create)
negociacaoRoute.route('/Excluir', methods=['POST'])(delete)