def main():
    print(ingredients_for_the_pizza_crust())
    print(cook_recipe())


#Function that prints the steps to boil water
def ingredients_for_the_pizza_crust():
    print("1 cup of warm water")
    print("1 teaspoon of brown suger")
    print("1 teaspoon of salt")
    print("1 teaspoon instant dry yeast")
    print("1 tablespoon olive oil")
    print("2 cups of flour")


# Function that prints a welcome message for the recipe
def welcome_message():
    print("Welcome to Python's Virtual Kitchen recipes!")
    print("Today, we’ll learn how to make delicious recipes using functions.")

def list_ingredients(main_ingredient, side_dish):
    print(f"Main Ingredient: {main_ingredient}")
    print(f"Side Dish: {side_dish}")

def make_dish(ingredient1, ingredient2):
    return f"{ingredient1} and {ingredient2} Pizza!"

def add_spice(dish, spice="pizza spice"):
    print(f"Adding a dash of {spice} to the {dish}. Yum!")

def cook_recipe():
    welcome_message()
    ingredients_for_the_pizza_crust()
    list_ingredients("tomato sauce", "salad")
    dish = make_dish("mozzarella", "mushrooms")
    print("Dish created:", dish)
    add_spice(dish)

if __name__ == "__main__":
    main()
