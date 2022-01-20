class Pet:
    def __init__(self,name,typePet,tricks,noise):
        self.name = name
        self.type = typePet
        self.tricks = tricks
        self.health = 100 
        self.energy = 50 
        self.noise = noise
        
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 15
        return self
    
    def noise(self):
        print(self.noise)
        return self
        
class Ninja:
    def __init__(self,firstName,lastName,pet,treats,petFood):
        self.firstName = firstName
        self.lastName = lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood
        
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        if len(self.petFood) > 0:
            food = self.petFood.pop()
            print(f"Feeding {self.pet.name} {food} now.")
            self.pet.eat()
        else:
            print(f"We need to get you more food, don't we, {self.pet.name}?")
        return self
    
    def bathe(self):
        print(f"As {self.lastName} gives {self.pet.name} a bath, {self.pet.name} whispers {self.pet.noise}.")
        return self
        
    def petStats(self):
        print(f"{self.pet.name}'s current Health is {self.pet.health}!")
        health = self.pet.health
        print(f"{self.pet.name}'s current Energy is {self.pet.energy}!")
        energy = self.pet.energy
        if health and energy in range(80,100) or health and energy >= 100:
            print(f"{self.pet.name} is very healthy and happy! Keep up the good work!")
        else:
            print(f"{self.pet.name} says {self.pet.noise}, NOW GIVE ME LOVE!")
            return self
        
treats = ['cake','tacos', 'sour patch kids']
petFood = ['sushi', 'mac&cheese','coffee']

Tom = Pet("Tomallama","Llama",['assassin','gamer','spits far','cooler than you'],"...i am batman...")
K = Ninja("BL0D","-X_X-R3INA",Tom,treats,petFood)

print(f"Congratulations {K.firstName}{K.lastName}! You have a new pet: a(n) {Tom.type} named {Tom.name}! {Tom.name}'s skills are {Tom.tricks}!")
K.petStats().feed().walk().bathe().feed().feed().bathe()
Tom.sleep().eat().sleep().sleep()
K.petStats()