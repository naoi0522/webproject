from quizapp.types.objects_graphql import StoreObject
from flask_graphql_auth.decorators import query_header_jwt_required
from quizapp.types.protected_store import ProtectedStore
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
import random

from quizapp.types.users import Users
from quizapp.types.quizs import Quizs
from quizapp.models.quiz import Quiz as QuizModel
from quizapp.models.user import User as UserModel
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

    quizs_by_username = graphene.List(Quizs, username=graphene.String())
    # ユーザーネームからクイズを抜き出し

    @ staticmethod
    def resolve_quizs_by_username(parent, info, **args):
        q = args.get('username')

        quizs_query = Quizs.get_query(info)

        return quizs_query.join(UserModel, QuizModel.user_id == UserModel.user_id).filter(UserModel.username == q).all()

    user_by_name = graphene.List(Users, name=graphene.String())

    # ユーザーネームからユーザーを抜き出し
    @ staticmethod
    def resolve_user_by_name(parent, info, **args):
        q = args.get('name')

        users_query = Users.get_query(info)

        return users_query.filter(UserModel.username == q)

    quiz_by_quiz_id = graphene.List(Quizs, quiz_id=graphene.Int())

    # クイズIDからクイズを抜き出し
    @ staticmethod
    def resolve_quiz_by_quiz_id(parent, info, **args):
        q = args.get('quiz_id')

        quizs_query = Quizs.get_query(info)

        return quizs_query.filter(QuizModel.quiz_id == q)

    quiz_by_random = graphene.List(Quizs)

    # ランダムにクイズを１問抜き出し
    @ staticmethod
    def resolve_quiz_by_random(parent, info):
        quizs_query = Quizs.get_query(info)
        random_item = [random.choice(quizs_query.all())]

        return random_item

    # TODO: １０問一気に抜き出しも考慮
