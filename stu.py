class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. My email is: {self.email}")

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old, Email: {self.email}"

    @staticmethod
    def is_adult(age):
        return age >= 18

# Create an instance of the Person class
person1 = Person("Paz", 30, "pazimvu@ad.com")
person2 = Person("Bob", 25, "bob@example.com")
person3 = Person("Eyal", 30, "eyal@example.com")
person4 = Person("Sol", 30, "sol@example.com")

# Call the say_hello() method for each person
person1.say_hello()
person2.say_hello()
person3.say_hello()
person4.say_hello()

# Call the str() function on each person
print(str(person1))
print(str(person2))
print(str(person3))
print(str(person4))

# Call the static method is_adult() directly on the class
print("Is Paz an adult?", Person.is_adult(person1.age))
print("Is Bob an adult?", Person.is_adult(person2.age))
