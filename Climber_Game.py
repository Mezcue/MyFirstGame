## Climbing Game -- Fun Project
## One player type of game, kind of exploring projects..
## If a move fails, the climber dies
## There is a climber, a project with moves
## takes climbers levels (endurace, pwoer, sterngth, and PE)
## Climber is tested on the climbs requirments


#climbers_name = input("What is your name: ")
#print(climbers_name)

class Climber:

    def __init__(self, name, style, str, pow, end, powend):
        self.name = name
        self.style = style
        self.str = str
        self.pow = pow
        self.end = end
        self.powend = powend

    def __repr__(self):
        return f"Climber {self.name} style is {self.style}, and stats of: Strength = {self.str}; Power = {self.pow}; Endurance = {self.end}; Power Endurance = {self.powend}"
    

class Rock_Climb:
    pass


## Test Climber
rico = Climber("Enrico", "balls-limic", 7, 7, 9, 8)
print(rico)


## Make sure to:
# git init
# git add
# git commit -m " "
# git push
