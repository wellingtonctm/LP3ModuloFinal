from Data.DbContext import db

class Negociacao(db.Model):
    __tablename__ = 'negociacoes'

    id = db.Column(db.Integer, primary_key=True)
    usuarioId = db.Column(db.Integer, ForeignKey=('usuarios.id'))
    ativoId = db.Column(db.Integer)
    tipo = db.Column(db.String)
    tipoMercado = db.Column(db.String)
    tamanhoLote = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'ativoId': self.ativoId,
            'tipo': self.tipo,
            'tipoMercado': self.tipoMercado,
            'tamanhoLote': self.tamanhoLote,
            'quantidade': self.quantidade,
            'valor': self.valor
        }