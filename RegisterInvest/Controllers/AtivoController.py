from Data.DbContext import db
from Models.Ativo import Ativo
from flask import render_template, request, session, redirect, url_for

def getAll():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('UsuarioRoute.login'))
    
    erro = request.args['erro'] if 'erro' in request.args else None
    usuarios = []
    
    try:
        usuarios = db.session.query(Ativo).order_by(Ativo.id).all()
    except Exception as ex:
        erro = ex
        
    return render_template('Ativo/Listar.html', erro = erro, usuarios = usuarios)

def create():
    ...

def get(ativoId):
    ...

def update(ativoId):
    ...

def delete(ativoId):
    ...