import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from quizapp.models.user import User as UserModel


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class UserAttribute:
    username = graphene.String()
    password = graphene.String()


class CreateUserInput(graphene.InputObjectType, UserAttribute):
    pass
