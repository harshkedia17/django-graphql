import re
from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Questions, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):

    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Questions.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


# for creating a new categpry
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)
    

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls,root,info,name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

#for updating a category
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls,root,info,name,id):
#         category = Category.objects.get(id=id)
#         category.name = name;
#         category.save()
#         return CategoryMutation(category=category)


class CategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id):
        category = Category.objects.get(id=id)
        category.delete()
        return

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()





schema = graphene.Schema(query=Query, mutation=Mutation) 