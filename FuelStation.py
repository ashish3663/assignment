class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.total_slots = {'diesel': diesel, 'petrol': petrol, 'electric': electric}
        self.car_type = {'diesel': diesel, 'petrol': petrol, 'electric': electric}
        print("total slots available------",self.total_slots)

    def fuel_vehicle(self, fuel_type):
        print("fule_type for filling-----",fuel_type)
        if self.car_type[fuel_type] > 0:
            self.car_type[fuel_type] -= 1
            print("type left----",self.car_type)
            return True
        else:
            return False

    def open_fuel_slot(self, fuel_type):
        print("fule_type for open----",fuel_type)
        if self.car_type[fuel_type] >= 0:
            if self.car_type[fuel_type] < self.total_slots[fuel_type]:
                self.car_type[fuel_type] += 1
            elif self.car_type[fuel_type] == self.total_slots[fuel_type]:
                return False
            print("new_type_left---",self.car_type)
            return True
        else:
            return False

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
output = [
    fuel_station.fuel_vehicle("diesel"),  # True
    fuel_station.fuel_vehicle("petrol"),  # True
    fuel_station.fuel_vehicle("diesel"),  # True
    fuel_station.fuel_vehicle("electric"),  # True
    fuel_station.fuel_vehicle("diesel"),  # False
    fuel_station.open_fuel_slot("diesel"),  # True 
    fuel_station.fuel_vehicle("diesel"),  # True
    fuel_station.open_fuel_slot("electric"),  # True
    fuel_station.open_fuel_slot("electric"),  # False
]
print(output)