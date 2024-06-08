from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUp(self):
        Recipe.objects.create(name="Pancakes", description="Delicious pancakes", ingredients="Flour, Milk, Eggs", instructions="Mix ingredients and cook on a hot pan")

    def test_recipe_content(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = f'{recipe.name}'
        self.assertEqual(expected_object_name, 'Pancakes')
        self.assertEqual(recipe.description, "Delicious pancakes")
        self.assertEqual(recipe.ingredients, "Flour, Milk, Eggs")
        self.assertEqual(recipe.instructions, "Mix ingredients and cook on a hot pan")
