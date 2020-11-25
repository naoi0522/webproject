import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from quizapp.models.store import Store as StoreModel


class StoreObject(SQLAlchemyObjectType):
    class Meta:
        model = StoreModel
        interfaces = (graphene.relay.Node,)
