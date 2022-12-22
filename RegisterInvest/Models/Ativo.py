import app

db = app.db

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
            'nome': self.codigo,
            'email': self.tipo,
            'senha': self.descricao
        }