from flask import Blueprint

from Controllers.AtivoController import getAll, create, delete

ativoRoute = Blueprint('AtivoRoute', __name__)

ativoRoute.route('/', methods=['GET'])(getAll)
ativoRoute.route('/Criar', methods=['POST'])(create)
ativoRoute.route('/Excluir', methods=['POST'])(delete)