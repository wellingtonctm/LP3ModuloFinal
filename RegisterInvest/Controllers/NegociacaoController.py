from Data.DbContext import db
from Models.Negociacao import Negociacao
from Models.Usuario import Usuario
from Models.Ativo import Ativo
from flask import render_template, request, session, redirect, url_for

def getAll():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('UsuarioRoute.login'))
    
    erro = request.args['erro'] if 'erro' in request.args else None
    negociacoes = []
    
    try:
        negociacoes = db.session.query(Negociacao).order_by(Negociacao.id).all()
        negociacoesDTO = []

        for neg in negociacoes:
            negociacoesDTO.append({
                'id': neg.id,
                'usuario': Usuario.query.get(neg.usuarioId).email,
                'tiker': Ativo.query.get(neg.ativoId).codigo,
                'tipo': neg.tipo,
                'lote': neg.tamanhoLote,
                'quantidade': neg.quantidade,
                'valor': neg.valor
            });

    except Exception as ex:
        erro = ex
        
    return render_template(
        'Negociacao/Listar.html',
        erro = erro,
        negociacoes = negociacoesDTO,
        ativos = Ativo.query.order_by(Ativo.id).all()
    )


def create():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('UsuarioRoute.login'))

    erro = None
    
    try:
        usuario = Usuario.query.filter(Usuario.email == session['usuario']).first()

        if usuario == None:
            raise Exception("Usuário não encontrado!");

        if request.form['ativoId'] == None or request.form['ativoId'].strip() == '':
            raise Exception('Tiker não informado!')

        ativo = Ativo.query.get(request.form['ativoId'])

        if ativo == None:
            raise Exception('Ativo não encontrado!')

        if request.form['tipo'] == None or request.form['tipo'].strip() == '':
            raise Exception('Tipo não informado!')

        if request.form['tipo'] not in ["COMPRA", "VENDA"]:
            raise Exception('Tipo inválido!')

        print(request.form)

        if request.form['tamanhoLote'] == None or request.form['tamanhoLote'].strip() == '':
            raise Exception('Tamanho de Lote não informado!')

        if int(request.form['tamanhoLote']) < 1:
            raise Exception('Tamanho inválido!')

        if request.form['quantidade'] == None or request.form['quantidade'].strip() == '':
            raise Exception('Quantidade não informada!')

        if int(request.form['quantidade']) < 1:
            raise Exception('Quantidade inválida!')

        if request.form['valor'] == None or request.form['valor'].strip() == '':
            raise Exception('Valor não informado!')

        if float(request.form['valor']) < 0:
            raise Exception('Valor inválido!')

        negociacao = Negociacao()

        negociacao.usuarioId = usuario.id
        negociacao.ativoId = ativo.id
        negociacao.tipo = request.form['tipo']
        negociacao.tamanhoLote = request.form['tamanhoLote']
        negociacao.quantidade = request.form['quantidade']
        negociacao.valor = request.form['valor']

        db.session.add(negociacao)
        db.session.commit()
    except Exception as ex:
        erro = ex
        
    return redirect(url_for('NegociacaoRoute.getAll', erro=erro))


def delete():
    erro = None
    
    try:
        if request.form['id'] == None or request.form['id'].strip() == '':
            raise Exception('Id não informado!')
        
        negociacao = db.session.query(Negociacao).get(request.form['id'])
        
        if negociacao == None:
            raise Exception('Negociacao não encontrado!')
        
        db.session.delete(negociacao)
        db.session.commit()
    except Exception as ex:
        erro = ex
    
    return redirect(url_for('NegociacaoRoute.getAll', erro=erro))