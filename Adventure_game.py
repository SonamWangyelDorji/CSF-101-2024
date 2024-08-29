class Character:
    # Encapsulation : The class (Character) encapsulates attributes like name, health and inventory, 
    # along with different methods/functions to interact the attributes such as describe, take_damage and pick_item.  . 
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
    
    def describe(self):
        # Describes the characters state.
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    def take_damage(self,amount):
        # Reduces health by the damage amount and if the health reaches zero,
        # it prints a message indicating the character has died and,
        # it prevents the health to go into negative. 
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print("You died")
        
    
    def pick_item(self,item):
        #Using this function, it adds item to the inventory.
        self.inventory.append(item)

class Adventure:
    # Encapsulation : The class encapsulates attributes like characters and scenes,
    # as well as methods/functions to interact with the attributes (add_scene and play_scene).
    def __init__(self):
        self.characters = []
        self.scenes = {}
    
    def add_scene(self, name, description):
    # Add scene with name and description.
        self.scenes[name] = description 

    def play_scene(self, name):
    # It plays the scene if it exists.
        if name in self.scenes:
            print(f"Scene: {name}")
            print(self.scenes[name])

        else:
            print(f"The scene {name} does not exist")

class Hero(Character):
    #Inheritance: The class (Hero) inherits from the Character class, allowing it to gain access
    #to its (Character Class) attributes and methods.
    def heal(self, amount):
        # Adds the health of the hero by the amount.
        self.health += amount

class Villain(Character):
    #Inheritance: The class (Villan) also inherits from the Character class however overrides 
    #the describe method to give different implementation.
    def describe(self):
        return (f"{self.name} is a fearsome villan with {self.health} health and has the following items: {self.inventory}")


#Abstraction: Creating an instance of Hero abstracts the complexity of its attributes and methods,
# allowing interaction with the object through a simple interface. 
hero = Hero("Archer")
villain = Villain("Goblin")  


adventure = Adventure()

adventure.add_scene("Forest", "You are in a dark forest. There's a shiny object on the ground.")

adventure.add_scene("Cave", "The cave is dark and you can hear growling.")


adventure.play_scene("Forest")

hero.pick_item("Shiny Sword")
print(f"{hero.name} picks up a Shiny Sword which was made out of titanium")

hero.describe()

adventure.play_scene("Cave")


print(f"The hero {hero.name} gets attacked by a {villain.name}")
hero.take_damage(20)

print(f"After {hero.name} gets attacked, he uses the sword and gives a strong blow to the {villain.name}, killing the monster with one strike")

#Polymorphism: Both the Hero and Villain classes have a describe method, but the method behaves differently depending on the class of the object calling it. 
hero.describe()
