from quizapp.types.objects_graphql import StoreObject
from flask_graphql_auth.decorators import query_header_jwt_required
from quizapp.types.protected_store import ProtectedStore
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from quizapp.types.users import Users
from quizapp.types.quizs import Quizs
from quizapp.models.quiz import Quiz as QuizModel
from quizapp.models.store import Store as StoreModel


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    all_quizs = SQLAlchemyConnectionField(Quizs)
    all_users = SQLAlchemyConnectionField(Users)
    get_store = graphene.Field(
        type=ProtectedStore, token=graphene.String(), id=graphene.Int())

    @ query_header_jwt_required
    def resolve_get_store(self, info, id):
        store_qry = StoreObject.get_query(info)
        storeval = store_qry.filter(StoreModel.id.contains(id)).first()
        return storeval

    quizs_by_name = graphene.List(Quizs, name=graphene.String())

    # ユーザーIDからクイズを抜き出し
    @ staticmethod
    def resolve_quizs_by_name(parent, info, **args):
        q = args.get('name')

        quizs_query = Quizs.get_query(info)

        return quizs_query.filter(QuizModel.username.contains(q)).all()
