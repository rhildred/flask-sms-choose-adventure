class Welcoming:
    def __init__(self, outer):
        self.__outer = outer
    def takeTurn(self, sPhone, sInput):
        self.__outer.setState("stick")
        return ["Hi I'm spot (a dog). Oh look a stick. Do you play or keep on walking?"]

class Stick:
    def __init__(self, outer):
        self.__outer = outer
    def takeTurn(self, sPhone, sInput):
        if "play" in sInput.lower():
            self.__outer.setState("play")
            return ["Great my favourite game ... Here's the stick back. Do you throw it again?"]
        else:
            return ["Walking is my favourite. Oh look a stick! Do you play or keep on walking?"]

class Play:
    def __init__(self, outer):
        self.__outer = outer
    def takeTurn(self, sPhone, sInput):
        if "yes" in sInput.lower():
            return ["Here it is! I got it for you. Do you toss it again.... Please? "]
        else:
            self.__outer.setState("stick")
            return ["Walking is my favourite. Oh look a stick! Do you play or keep on walking?"]

class Game:
    def __init__(self):
        self.oStates = {
            "welcoming": Welcoming(self),
            "stick": Stick(self),
            "play": Play(self)
        }
        self.__sCurState = "welcoming"
    def setState(self, sNew):
        self.__sCurState = sNew
    def takeTurn(self, sPhone, sInput):
        return self.oStates[self.__sCurState].takeTurn(sPhone, sInput)

