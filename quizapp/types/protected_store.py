import graphene
from flask_graphql_auth import AuthInfoField
from quizapp.types.objects_graphql import StoreObject


class ProtectedStore(graphene.Union):
    class Meta:
        types = (StoreObject, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)
