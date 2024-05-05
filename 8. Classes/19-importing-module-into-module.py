# Imporitng module into a module

# Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.

# For example, let’s store the Car class in one module and the ElectricCar and Battery classes in a separate module. We’ll make a new module and copy just the Battery and ElectricCar classes into this file

# Then we can import from each module separately and create whatever kind of car we need

# This example is demonstrated inside the modules folder
