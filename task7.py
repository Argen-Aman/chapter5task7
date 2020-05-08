class House:

    def __init__(self, household_type, area, furniture):
        self.household_type = household_type
        self.area = area
        self.free_area = area
        self.furniture_name_list = []
        self.furniture = furniture
        self.furniture_area()

    def __str__(self):
        return f'Household_type: {self.household_type} \nTotal area: {self.area} \nRemaining area: {self.free_area} \nFurniture:{self.furniture_name_list}'

    def furniture_area(self):
        for i in self.furniture.keys():
            self.furniture_name_list.append(i)

        for i in self.furniture.values():
            self.free_area -= i

my_house = House('Private house', 100, {'bed':4, 'wardrobe':2, 'table':1.5})

print(my_house)
