from Data.DbContext import db
from Models.Usuario import Usuario
from flask import render_template, request, session, redirect, url_for

def login():
    if 'usuario' in session and session['usuario'] != None:
        return redirect(url_for('NegociacaoRoute.getAll'))
    
    if request.method == 'POST':
        try:
            if request.form['email'] == None or request.form['email'].strip() == '':
                raise Exception('E-mail não informado!')
            
            if request.form['senha'] == None or request.form['senha'] == '':
                raise Exception('Senha inválida!')
            
            usuario = Usuario.query.filter(Usuario.email == request.form['email'], Usuario.senha == request.form['senha']).first()
            
            if usuario == None:
                raise Exception("Usuário ou senha inválidos!");
            
            session['usuario'] = request.form['email']
            return redirect(url_for('NegociacaoRoute.getAll'))
        except Exception as ex:
            return render_template('Usuario/Login.html', erro = ex)
    else:
        return render_template('Usuario/Login.html')
    

def logout():
    session.pop('usuario', None)
    return redirect(url_for('UsuarioRoute.login'))


def getAll():    
    erro = request.args['erro'] if 'erro' in request.args else None
    usuarios = []
    
    try:
        usuarios = db.session.query(Usuario).order_by(Usuario.id).all()
    except Exception as ex:
        erro = ex
        
    return render_template('Usuario/Listar.html', erro = erro, usuarios = usuarios)


def create():
    erro = None
    
    try:
        if request.form['nome'] == None or request.form['nome'].strip() == '':
            raise Exception('Nome não informado!')
        
        if request.form['email'] == None or request.form['email'].strip() == '':
            raise Exception('E-mail não informado!')
        
        if request.form['senha'] == None or len(request.form['senha']) < 8:
            raise Exception('Senha inválida!')

        repetido = Usuario.query.filter(Usuario.email == request.form['email']).first()

        if repetido != None:
            raise Exception('Email já cadastrado!')
        
        usuario = Usuario()
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        usuario.senha = request.form['senha']
        
        db.session.add(usuario)
        db.session.commit()
    except Exception as ex:
        erro = ex
        
    return redirect(url_for('UsuarioRoute.getAll', erro=erro))


def delete():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('UsuarioRoute.login'))
    
    erro = None
    
    try:
        if request.form['id'] == None or request.form['id'].strip() == '':
            raise Exception('Id não informado!')
        
        usuario = db.session.query(Usuario).get(request.form['id'])
        
        if usuario == None:
            raise Exception('Usuário não encontrado!')
        
        db.session.delete(usuario)
        db.session.commit()
    except Exception as ex:
        erro = ex
    
    return redirect(url_for('UsuarioRoute.getAll', erro=erro))