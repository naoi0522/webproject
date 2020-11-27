from flask_graphql_auth.decorators import mutation_jwt_refresh_token_required, mutation_jwt_required
from flask_graphql_auth.util import get_jwt_identity
from quizapp.types.protected_store import ProtectedStore
import graphene
from quizapp.types.quizs import Quizs, CreateQuizInput
from quizapp.types.users import Users, CreateUserInput
from quizapp.models.quiz import Quiz as QuizModel
from quizapp.models.user import User as UserModel
from quizapp.models.store import Store as StoreModel
from quizapp.database import db
from quizapp.utils.input_to_dictionary import input_to_dictionary
from flask_graphql_auth import create_access_token, create_refresh_token


class CreateQuiz(graphene.Mutation):
    quiz = graphene.Field(lambda: Quizs)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateQuizInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        data = input  # input_to_dictionary(input)
        quiz = QuizModel(**data)
        db.session.add(quiz)
        db.session.commit()
        ok = True
        return CreateQuiz(quiz=quiz, ok=ok)


class CreateUser(graphene.Mutation):
    user = graphene.Field(lambda: Users)
    ok = graphene.Boolean()

    class Arguments:
        input = CreateUserInput(required=True)

    @staticmethod
    def mutate(self, info, input):
        data = input_to_dictionary(input)
        temp_user = UserModel(**data)
        user = UserModel.query.filter_by(username=temp_user.username).first()
        ok = True
        if user:
            return CreateUser(user=user, ok=ok)
        user = temp_user
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user, ok=ok)


class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    @staticmethod
    def mutate(self, info, username, password):
        user = UserModel.query.filter_by(
            username=username, password=password).first()
        print(user)
        if not user:
            raise Exception('Authentication Failure: User is not registered')
        return AuthMutation(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username)
        )


class CreateStore(graphene.Mutation):
    store = graphene.Field(ProtectedStore)

    class Arguments:
        name = graphene.String(required=True)
        user_id = graphene.Int(required=True)
        token = graphene.String()

    @mutation_jwt_required
    def mutate(self, info, name, user_id):
        store = StoreModel(name=name, user_id=user_id)
        print(store)
        if store:
            db.session.add(store)
            db.session.commit()
        return CreateStore(store=store)


class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))


class Mutation(graphene.ObjectType):
    createQuiz = CreateQuiz.Field()
    createUser = CreateUser.Field()
    auth = AuthMutation.Field()
    protected_create_store = CreateStore.Field()
    refresh = RefreshMutation.Field()
