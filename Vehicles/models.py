from django.db import models

# Create your models here.
class Vehicle():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def vehicle_info(self):
        return f"Brand: {self.brand} costs {self.price}"
        
class Car(Vehicle):
    def __init__(self,brand, price, door):
        super().__init__(brand, price)
        self.door = door
        
    def vehicle_info(self):
        return f"{self.brand} with {self.door} doors costs {self.price}"

class Motorcycle(Vehicle):
    def __init__(self, brand, price, helmet_included):
        super().__init__(brand, price)
        self.helmet_included = helmet_included

    def vehicle_info(self):
        if self.helmet_included:
            return f"{self.brand} with helmet included costs {self.price}"
        return f"{self.brand} without helmet included costs {self.price}"