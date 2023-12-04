class FoodItem:
    def __init__(self, food, amount):
        self.__food = food
        self.__amount = amount
        self.__standard_price = 0.0
        self.__calculated_price = 0.0
        self.__price_list()

    def __price_list(self):
        if self.__food == 'Dry Cured Iberian Ham':
            self.__standard_price = 177.80
        elif self.__food == 'Wagyu Steaks':
            self.__standard_price = 450.00
        # Add other items
        else:
            self.__standard_price = 0.00

    def calculate_cost(self):
        self.__calculated_price = self.__amount * self.__standard_price
        return self.__calculated_price

    def get_food(self):
        return self.__food

    def get_amount(self):
        return self.__amount

    def get_standard_price(self):
        return self.__standard_price

    def __str__(self):
        return f"Item: {self.__food}\nAmount ordered: {self.__amount} pounds\nPrice per pound: ${self.__standard_price:.2f}\nPrice of order: ${self.__calculated_price:.2f}"