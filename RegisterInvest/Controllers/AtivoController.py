from Data.DbContext import db
from Models.Ativo import Ativo
from flask import render_template, request, session, redirect, url_for

def getAll():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('UsuarioRoute.login'))
    
    erro = request.args['erro'] if 'erro' in request.args else None
    ativos = []
    
    try:
        ativos = db.session.query(Ativo).order_by(Ativo.id).all()
    except Exception as ex:
        erro = ex
        
    return render_template('Ativo/Listar.html', erro = erro, ativos = ativos)


def create():
    erro = None
    
    try:
        if request.form['codigo'] == None or request.form['codigo'].strip() == '':
            raise Exception('Tiker não informado!')

        if request.form['tipo'] == None or request.form['tipo'].strip() == '':
            raise Exception('Tipo não informado!')

        if request.form['tipo'] not in ['FII', 'ACAO']:
            raise Exception('Tipo inválido!')

        if request.form['descricao'] == None or request.form['descricao'].strip() == '':
            raise Exception('Descrição não informada!')

        repetido = Ativo.query.filter(Ativo.codigo == request.form['codigo']).first()

        if repetido != None:
            raise Exception('Tiker já cadastrado!')
        
        ativo = Ativo()
        ativo.codigo = request.form['codigo']
        ativo.tipo = request.form['tipo']
        ativo.descricao = request.form['descricao']

        db.session.add(ativo)
        db.session.commit()
    except Exception as ex:
        erro = ex
        
    return redirect(url_for('AtivoRoute.getAll', erro=erro))


def delete():
    erro = None
    
    try:
        if request.form['id'] == None or request.form['id'].strip() == '':
            raise Exception('Id não informado!')
        
        ativo = db.session.query(Ativo).get(request.form['id'])
        
        if ativo == None:
            raise Exception('Ativo não encontrado!')
        
        db.session.delete(ativo)
        db.session.commit()
    except Exception as ex:
        erro = ex
    
    return redirect(url_for('AtivoRoute.getAll', erro=erro))