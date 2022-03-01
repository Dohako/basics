

def main_func_1():
    name = 'John' # <- this stays in memory
    def inner_func():
        print(f"Hello, {name}") # <- this var is taken from outer scope

    return inner_func

a = main_func_1()
a() # <- Hello, John

def main_func_2(value):
    name = value # <- this stays in memory
    def inner_func():
        print(f"Hello, {name}") # <- this var is taken from outer scope

    return inner_func

a = main_func_2("Michael")
a() # <- Hello, Michael

b = main_func_2("Ann")
b() # <- Hello, Ann


def main_func_3(name):# <- this stays in memory
    def inner_func():
        print(f"Hello, {name}") # <- this var is taken from outer scope

    return inner_func

a = main_func_3("Julia")
a() # <- Hello, Julia

b = main_func_3("Theodor")
b() # <- Hello, Theodor


def adder(value):# <- this stays in memory
    def inner_func(another_value):
        print(value+another_value) # <- this var is taken from outer scope

    return inner_func

a2 = adder(2)
a2(5) # 7

a5 = adder(5)
a5(10) # 15