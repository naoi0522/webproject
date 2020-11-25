from quizapp.utils.input_to_dictionary import input_to_dictionary
import graphene
from quizapp.schema.mutation import Mutation
from quizapp.schema.query import Query

from quizapp.types.users import Users
from quizapp.types.quizs import Quizs


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Quizs, Users])

# TODO: flask_graphql_authによる認証
