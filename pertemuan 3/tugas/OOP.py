# Membuat kelas


class MyClass:
    x = 5


# Membuat objek dari kelas
p1 = MyClass()
print(p1.x)

# Menghapus objek yang telah dibuat
del p1


# __init__() Function
class Person:
    def __init__(self, name, age):  # Self merujuk ke objek saat ini
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Emil", 36)
p1.greet()  # ini adalah method dari objek p1

print(p1.name)  # ini adalah properti dari objek p1
print(p1.age)  # ini adalah properti dari objek p1


class Student(Person):  # Ini adalah pewarisan dari class Person
    def __init__(self, fname, lname):
        super().__init__(
            fname, lname
        )  # Super memanggil fungsi __init__() dari class induk (Person)


# Polimorfisme adalah salah satu konsep fundamental
# dalam pemrograman berorientasi objek (OOP) yang memungkinkan
# beberapa kelas memiliki metode dengan nama yang sama
# namun berperilaku berbeda sesuai konteks penggunaannya.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()
