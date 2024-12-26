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
        return f"{self.name}"

class Rock_Climb:

    def __init__(self, name, difficulty = 20):
        self.name = name
        self.difficulty = difficulty

    def __repr__(self):
        return f"{self.name}"
        

## Test Climber
rico = Climber("Enrico", "balls-limic", 7, 7, 9, 8)
#print(rico)
#print(rico.str)

## Test Rock_Climb
v_zero = Rock_Climb("Testy")
#print(v_zero)
#print(v_zero.difficulty)

## Test Climber on Climb -- if stats don't sum up to/ greater than difficulty .. climber falls and dies

## Have to figure out how to automatically pull each stat. 
def attempting_climb(climber, climb):
    total_stats = climber.str + climber.pow + climber.end + climber.powend
    # return total_stats
    if total_stats >= climb.difficulty:
        print(f"{climber} successfully climb {climb}, and didn't die")
    else:
        print(f"{climber} died climbing {climb}")


attempting_climb(rico, v_zero)



## Make sure to:
# git init
# git add
# git commit -m " "
# git push
