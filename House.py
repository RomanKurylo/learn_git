class House:
    def __init__(self, temperature):
        self.temperature = temperature

    def air_conditioner(self, change_temp):
        self.temperature -= change_temp
        print(f'Вы охладили помещение на {change_temp} градусов')

    def heater(self, change_temp):
        self.temperature += change_temp
        print(f'Вы нагрели помещение на {change_temp} градусов')