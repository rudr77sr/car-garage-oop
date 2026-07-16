# Car Garage — OOP Practice Project

A small Python project practicing core OOP concepts: classes, inheritance, 
property decorators with validation, dunder methods, and JSON persistence.

## Features
- `Car` class with a validated `mileage` property (no negative values allowed)
- `ElecCar` subclass demonstrating inheritance
- `Garage` class managing a collection of cars
- Save/load cars to and from a JSON file

## What I practiced
- Classes and instance vs class variables
- Inheritance with `super()`
- `@property` and `@x.setter` for validated attributes
- `__str__` dunder method
- Serializing Python objects to JSON and back

## How to run
```bash
python garage.py
```

## Next steps
Building on this foundation to learn FastAPI and connect similar logic 
to a real database (PostgreSQL).