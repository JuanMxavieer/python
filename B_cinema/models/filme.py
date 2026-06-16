from . import db
from .base import ModeloBase


class Filme(ModeloBase):
    __tablename__ = "filmes"

    titulo = db.Column(db.String(150), nullable=False)
    # TODO ALUNO: duracao_min (Integer), classificacao (String 5)
    # TODO ALUNO: relationship sessoes
    duracao_min = db.Column(db.Integer, nullable=False)
    classificacao = db.Column(db.String(5), nullable=False)
    sessoes = db.relationship("sessoes", back_populates="fimes", lazy=True)

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()
