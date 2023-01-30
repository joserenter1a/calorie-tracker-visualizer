"""
Calorie Tracker and Visualizer
Author: Jose Renteria

Sources:
NeuralNine on YouTube
- https://www.youtube.com/watch?v=2Iid9rAo6sE

"""
from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3000  # kcal
PROTEIN_GOAL = 160  # grams
FAT_GOAL = 80  # grams
CARBS_GOAL = 300  # grams

today = []


@dataclass  # this decorator examines the class to find a given field s
class Food:
    name: str
    proteins: int
    carbs: int
    fats: int


done = False

while not done:
    print("""
    (1) Add a new food
    (2) Visualize data
    (Q) Quit
    """)

    choice = input("Select an option: \n")

    if choice == '1': # Add a new food to today
        print("Adding a new food!")
        name = input("Name: ")
        proteins = int(input("Protein: "))
        carbs = int(input("Carbohydrates: "))
        fats = int(input("Fat: "))
        food = Food(name, proteins, carbs, fats)
        today.append(food)
        print("Successfully added!")
    elif choice == '2':

        protein_sum = sum(food.proteins for food in today)  # sum of all of today's protein
        fats_sum = sum(food.fats for food in today)  # sum of all of today's fat
        carb_sum = sum(food.carbs for food in today)  # sum of all of today's carbs

        fig, axis = plt.subplots(2, 2)

        # Pie chart
        axis[0, 0].pie([protein_sum, fats_sum, carb_sum], labels=["Protein", "Fat", "Carbohydrates"], autopct="%1.1f%%")
        axis[0, 0].set_title("Macronutrient Distribution")

        # Bar chart
        axis[0, 1].bar([0, 1, 2], [protein_sum, carb_sum, fats_sum], width=0.4)
        axis[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width = 0.4)
        axis[0, 1].set_title("Macronutrients Progress")

        calories_from_macros = (food.proteins * 4) + (food.carbs * 4) + (food.fats * 9) # calculates calories given the macronutrients
        kcal_sum = sum(calories_from_macros for food in today)  # sum of all of today's calories


        # Pie chart, bottom left
        axis[1, 0].pie([kcal_sum, CALORIE_GOAL_LIMIT - kcal_sum], labels = ["Calories", "Remaining"], autopct="%1.f%%")
        axis[1, 0].set_title("Calorie Goal Progress")

        # Bar chart, bottom right
        axis[1, 1].plot(list(range(len(today))), np.cumsum([calories_from_macros for food in today]), label = "Calories Consumed")
        axis[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label = "Calorie Goal")
        axis[1, 1].legend()
        axis[1, 1].set_title("Calories goal over time")

        fig.tight_layout()
        plt.show()
    elif choice == 'Q':
        done = True
    else:
        print("Invalid choice")