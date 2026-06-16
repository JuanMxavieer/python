from . import db
from .base import ModeloBase


class Sessao(ModeloBase):
    __tablename__ = "sessoes"

    # TODO ALUNO: FK filme_id → filmes.id
    filmes_id = db.Column(db.Integer, db.ForeingKey("filmes_id"))
    # TODO ALUNO: FK sala_id → salas.id
    salas_id = db.Column(db.Integer, db.ForeingKey("salas_id"))
    data_hora = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    # TODO ALUNO: relationship filme, sala, ingressos

    filme = db.relationship("filme", back_populates="sessoes", lazy=True)
    sala = db.relationship("sala", back_populates="sessoes", lazy=True)
    ingressos = db.relationship("ingressos", back_populates="sessoes", lazy=True)

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_hora.desc()).all()
