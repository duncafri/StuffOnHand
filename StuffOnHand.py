# Author: Ricky Duncan
# SDEV140-11
# 06/21/2024
# Assignment: Module 03 Project Status Report
# Title: Module 03 Project Status Report
# Description: The purpose of Recipe Finder Pro is to help users discover recipes based on
# ingredients they have on hand and their current mood or cravings.

import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Recipe Finder Pro")

# Function to handle searching for recipes
def search_recipes():
    selected_ingredients = [ingredient for ingredient, var in ingredient_vars.items() if var.get() == 1]
    mood = mood_var.get()
    # Placeholder logic to match ingredients and mood to a recipe (to be replaced with actual search logic)
    recipe_name = get_matching_recipe(selected_ingredients, mood)
    # Display the recipe name in the result label
    if recipe_name:
        result_label.config(text=f"Recommended Recipe:\n{recipe_name}")
    else:
        result_label.config(text="No matching recipe found.")

# Placeholder function to match ingredients and mood to a recipe (to be implemented)
def get_matching_recipe(ingredients, mood):
    # Example matching logic (replace with actual matching logic)
    if "Chicken" in ingredients and mood == "Comfort Food":
        return "Chicken Alfredo"
    elif "Spinach" in ingredients and mood == "Healthy":
        return "Spinach Salad"
    elif "Pasta" in ingredients and mood == "Quick Meals":
        return "Pasta with Pesto"
    elif "Fish" in ingredients and mood == "International Cuisine":
        return "Fish Tacos"
    else:
        return None

# GUI Components
ingredients_label = tk.Label(root, text="Select ingredients:")
ingredient_vars = {}
# Placeholder for ingredients list (you can replace with actual ingredients)
ingredients_list = ["Chicken", "Beef", "Fish", "Pasta", "Rice", "Tomato", "Spinach", "Broccoli"]
# Create Checkbuttons for each ingredient
for i, ingredient in enumerate(ingredients_list):
    ingredient_vars[ingredient] = tk.IntVar()
    ingredient_button = tk.Checkbutton(root, text=ingredient, variable=ingredient_vars[ingredient])
    ingredient_button.grid(row=i//2, column=i%2, padx=10, pady=5, sticky="w")

mood_label = tk.Label(root, text="Select your mood or food type:")
mood_var = tk.StringVar()
mood_dropdown = tk.OptionMenu(root, mood_var, "Comfort Food", "Healthy", "Quick Meals", "International Cuisine")
search_button = tk.Button(root, text="Search Recipes", command=search_recipes)
result_label = tk.Label(root, text="")

# Layout using grid
ingredients_label.grid(row=len(ingredients_list)//2, column=0, columnspan=2, padx=10, pady=10)
mood_label.grid(row=len(ingredients_list)//2 + 1, column=0, padx=10, pady=10)
mood_dropdown.grid(row=len(ingredients_list)//2 + 1, column=1, padx=10, pady=10)
search_button.grid(row=len(ingredients_list)//2 + 2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=len(ingredients_list)//2 + 3, column=0, columnspan=2, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()