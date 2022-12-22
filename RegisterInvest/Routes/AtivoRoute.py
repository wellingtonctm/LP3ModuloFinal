from flask import Blueprint

from Controllers.AtivoController import getAll, create, get, update, delete

ativoRoute = Blueprint('AtivoRoute', __name__)

ativoRoute.route('/', methods=['GET'])(getAll)
ativoRoute.route('/Criar', methods=['POST'])(create)
ativoRoute.route('/<int:ativo_id>', methods=['GET'])(get)
ativoRoute.route('/<int:ativo_id>/Editar', methods=['POST'])(update)
ativoRoute.route('/<int:ativo_id>', methods=['DELETE'])(delete)