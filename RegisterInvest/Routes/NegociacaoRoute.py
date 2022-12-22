from flask import Blueprint

from Controllers.NegociacaoController import getAll, create, get, update, delete

negociacaoRoute = Blueprint('NegociacaoRoute', __name__)

negociacaoRoute.route('/', methods=['GET'])(getAll)
negociacaoRoute.route('/Criar', methods=['POST'])(create)
negociacaoRoute.route('/<int:negociacao_id>', methods=['GET'])(get)
negociacaoRoute.route('/<int:negociacao_id>/Editar', methods=['POST'])(update)
negociacaoRoute.route('/<int:negociacao_id>', methods=['DELETE'])(delete)