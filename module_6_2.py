# Задача "Изменять нельзя получать"
class Vehicle:

    # допустимые цвета для выбора:
    __COLOR_VARIANTS = ['beige', 'green_and_blue', 'bright_yellow', 'wet_asphalt', 'dark_purple']

    def __init__(self, owner = None, __model = None, __color = None, __engine_power = None):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

# Методы для объектов класса Vehicle:
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на новый {new_color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# объект класса Sedan(Vehicle)
vehicle_1 = Sedan('Fedos', 'Toyota Mark II', 'beige', 500)
# Изначальные свойства
vehicle_1.print_info()
# Меняем свойства
vehicle_1.set_color('Pink')
vehicle_1.set_color('BRIGHT_YELLOW')
vehicle_1.owner = 'Vasyok'

# Проверяем, что поменялось
vehicle_1.print_info()