class Shark():
    def swim(self):
        print('I\'m a Shark and I\'m swiming')

class Goldfish():
    def swim(self):
        print('I\'m a Goldfish and I\'m floating' )

def this_fish_gonna_swim(fish):
    fish.swim()

memo = Shark()
this_fish_gonna_swim(memo)

memo = Goldfish()
this_fish_gonna_swim(memo)
