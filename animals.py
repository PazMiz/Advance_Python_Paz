from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

# Subclass (Derived class)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Subclass (Derived class)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Subclass (Derived class)
class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Subclass (Derived class)
class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# Subclass (Derived class)
class Predator(Animal):
    def make_sound(self):
        pass

# Predator subclasses
class Lion(Predator):
    def make_sound(self):
        return "Roar!"

class Tiger(Predator):
    def make_sound(self):
        return "Growl!"

# Partner class
class Partner:
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal

    def is_predator(self):
        return isinstance(self.animal, Predator)

# Create instances of the subclasses
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
cow1 = Cow("Molly")
bird1 = Bird("Tweety")

lion1 = Lion("Leo")
tiger1 = Tiger("Tony")

# Create instances of the Partner class with animals as partners
partner1 = Partner("John", dog1)
partner2 = Partner("Alice", cat1)
partner3 = Partner("Emma", cow1)
partner4 = Partner("Michael", bird1)
partner5 = Partner("Alex", lion1)
partner6 = Partner("Sophia", tiger1)

# Create a Kivy app
class PartnerApp(App):
    def build(self):
        self.animal_partners = [partner1, partner2, partner3, partner4]
        self.predator_partners = [partner5, partner6]
        self.show_animals = True  # Variable to store whether to show animals or predators

        layout = BoxLayout(orientation='vertical')
        self.list_label = Label(text="List of Partners:")
        self.partner_list = BoxLayout(orientation='vertical')
        self.animal_count_label = Label(text="Total Animals: 0")  # Label to show the count of animals

        self.update_partner_list()

        animal_button = Button(text="Show Animals", on_press=self.filter_animals)
        predator_button = Button(text="Show Predators", on_press=self.filter_predators)

        layout.add_widget(self.list_label)
        layout.add_widget(self.partner_list)
        layout.add_widget(animal_button)
        layout.add_widget(predator_button)
        layout.add_widget(self.animal_count_label)

        return layout

    def update_partner_list(self):
        self.partner_list.clear_widgets()

        partners = self.animal_partners if self.show_animals else self.predator_partners

        animal_count = 0
        for partner in partners:
            partner_label = Label(text=f"{partner.name} - {partner.animal.name} ({partner.animal.__class__.__name__})")

            if isinstance(partner.animal, Predator):
                partner_label.color = get_color_from_hex('#FF0000')  # Set red color for predators
            else:
                partner_label.color = get_color_from_hex('#FFFF00')  # Set yellow color for normal animals

            self.partner_list.add_widget(partner_label)
            animal_count += 1  # Increment animal count for each partner

        self.animal_count_label.text = f"Total Animals: {animal_count}"

    def filter_animals(self, instance):
        self.show_animals = True
        self.update_partner_list()

    def filter_predators(self, instance):
        self.show_animals = False
        self.update_partner_list()

if __name__ == '__main__':
    PartnerApp().run()

