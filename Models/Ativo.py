from Data.DbContext import db

class Ativo(db.Model):
    __tablename__ = 'ativos'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    tipo = db.Column(db.String)
    descricao = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'tipo': self.tipo,
            'descricao': self.descricao
        }