from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list


class RecipeListResource(Resource):
    # get all public recipes
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    # post method to create a recipe
    def post(self):

        # get json data back from request
        data = request.get_json()

        # define recipe from json data
        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        # add recipe to recipe_list
        recipe_list.append(recipe)

        # return json data that was written
        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resource):

    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data = request.get_json()

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description'],
        recipe.num_of_servings = data['num_of_servings'],
        recipe.cook_time = data['cook_time'],
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK

    def delete(self, recipe_id):

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe_list.remove(recipe)

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
