# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Base
class Vehicle:
        pass

class GroundVehicle(Vehicle):
        super().__init__()
        pass

class Car(GroundVehicle):
        super().__init__()
        pass
    
class Motorcycle(GroundVehicle):
        super().__init__()
        pass
#Base
class FlightVehicle:
        pass

class Airplane(FlightVehicle):
        super().__init__()
        pass
#Base
class Starship:
        pass