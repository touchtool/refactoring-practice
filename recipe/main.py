from recipe import Recipe

# replace redundant code with a creational method
def create_recipe(name, chocolate=0, coffee=0, milk=0, sugar=0, price=0.0):
    recipe = Recipe(name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    return recipe


if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", 0, 4, 0, 2, 30.0)
    # recipe1.coffee = 4
    # recipe1.sugar = 2
    # recipe1.milk = 0
    # recipe1.price = 30.0
    print(recipe1)

    recipe2 = create_recipe("Latte", 0, 3, 1, 2, 40.0)
    # recipe2.coffee = 3
    # recipe2.sugar = 2
    # recipe2.milk = 1
    # recipe2.price = 40.0
    print(recipe2)

    recipe3 = create_recipe("Hot Chocolate", 3, 0, 4, 2, 30.0)
    # recipe3.coffee = 0
    # recipe3.chocolate = 3
    # recipe3.sugar = 2
    # recipe3.milk = 4
    # recipe3.price = 30.0
    print(recipe3)

