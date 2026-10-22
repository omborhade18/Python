"""Practical 5 - Object-oriented Python: inheritance and polymorphism."""


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):  # overrides Animal.sound
        print("Dog barks")


class Cat(Animal):
    def sound(self):  # overrides Animal.sound
        print("Cat meows")


def main():
    obj1 = Dog()
    obj2 = Cat()
    obj1.sound()
    obj2.sound()

    # Polymorphism: the same call behaves differently per object type.
    print("--- polymorphism ---")
    for animal in (Animal(), Dog(), Cat()):
        animal.sound()


if __name__ == "__main__":
    main()
