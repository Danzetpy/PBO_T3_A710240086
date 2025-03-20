class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter untuk name
    def get_name(self):
        return self.__name

    # Setter untuk name
    def set_name(self, name):
        self.__name = name

    # Getter untuk age
    def get_age(self):
        return self.__age

    # Setter untuk age
    def set_age(self, age):
        if age > 0:  # Validasi agar usia tidak negatif
            self.__age = age
        else:
            print("Usia tidak valid!")

# Membuat objek baru
person1 = Person("Pradana", 19)

# Mengakses variabel private menggunakan getter
print("Nama:", person1.get_name())
print("Usia:", person1.get_age())

# Mengubah variabel private menggunakan setter
person1.set_name("Budi")
person1.set_age(19)

# Menampilkan hasil setelah perubahan
print("Nama baru:", person1.get_name())
print("Usia baru:", person1.get_age())
