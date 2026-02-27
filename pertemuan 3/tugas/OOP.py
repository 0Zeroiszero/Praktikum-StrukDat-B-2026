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


# Properti Privat adalah konsep dalam pemrograman berorientasi objek (OOP)
# yang digunakan untuk menyembunyikan data
# atau atribut dari akses langsung oleh kode di luar kelas.
# Properti privat biasanya ditandai dengan menggunakan
# tanda underscore ganda (__) sebelum nama atribut.
# Ini adalah cara untuk menunjukkan bahwa atribut tersebut seharusnya
# tidak diakses langsung dari luar kelas, melainkan melalui metode atau
# fungsi yang disediakan oleh kelas itu sendiri.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


p1 = Person("Tobias", 25)
print(p1.get_age())  # Cara mengakses properti privat menggunakan getter

p1.set_age(26)
print(p1.get_age())  # Cara mengubah properti privat menggunakan setter
