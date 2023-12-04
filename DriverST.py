from ProgramExerciseST  import FoodItem

def create_food_list():

    food_list = []
    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))
    for i in range(num_items):
        food = input(f"Item #{i + 1} - Enter food: ")
        amount = float(input(f"Enter amount of pounds: "))
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input(f"Enter amount of pounds: "))
        food_list.append(FoodItem(food, amount))
    return food_list


def display_food_list(food_list):
    for food in food_list:
        print(food)
        print()


def calculate_total_cost(food_list):
    total_cost = 0.0
    for food in food_list:
        total_cost += food.calculate_cost()
    return total_cost


def main():
    foods = create_food_list()
    display_food_list(foods)
    total = calculate_total_cost(foods)
    print(f"Total cost: ${total:.2f}")


if __name__ == "__main__":
    main()