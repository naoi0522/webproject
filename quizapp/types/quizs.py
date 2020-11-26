# Types
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from ..models.quiz import Quiz as QuizModel


class Quizs(SQLAlchemyObjectType):
    class Meta:
        model = QuizModel
        interfaces = (graphene.relay.Node,)


class QuizAttribute:
    content = graphene.String()
    correct = graphene.Boolean()
    user_id = graphene.Int()


class CreateQuizInput(graphene.InputObjectType, QuizAttribute):
    pass
