from flask import request
from flask_restful import Resource
import flask_jwt_extended
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus
import json

from models.recipe import Recipe


class RecipeListResource(Resource):
    # get all public recipes
    def get(self):
        recipes = Recipe.get_all_published()

        data = []

        for recipe in recipes:
            data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    # post method to create a recipe (only after logged in - jwt_required)
    @jwt_required()
    def post(self):
        # get json data back from request
        json_data = request.get_json()
        current_user = get_jwt_identity()

        # define recipe from json data
        recipe = Recipe(name=json_data['name'],
                        description=json_data['description'],
                        num_of_servings=json_data['num_of_servings'],
                        cook_time=json_data['cook_time'],
                        directions=json_data['directions'],
                        user_id=current_user)

        # add recipe to recipe_list
        recipe.save()

        # return json data that was written
        return recipe.data(), HTTPStatus.CREATED


class RecipeResource(Resource):
    @jwt_required(optional=True)
    def get(self, recipe_id):
        recipe = Recipe.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if recipe.is_publish == False and recipe.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return recipe.data(), HTTPStatus.OK

    @jwt_required
    def put(self, recipe_id):
        json_data = request.get_json()

        recipe = Recipe.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        recipe.name = json_data['name']
        recipe.description = json_data['description'],
        recipe.num_of_servings = json_data['num_of_servings'],
        recipe.cook_time = json_data['cook_time'],
        recipe.directions = json_data['directions']

        recipe.save()

        return recipe.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, recipe_id):

        recipe = Recipe.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        recipe.delete()

        return {}, HTTPStatus.NO_CONTENT


class RecipePublishResource(Resource):

    # Method to locate recipe using passed in 'recipe_id' then update 'is_publish' to true, then returns NO_CONTENT to
    # show recipe has been published
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, recipe_id):

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
