# 14-m
class GamePlayer:
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def res(self):
        if self.name >= 50:
            print(f"{self.name} yutdi")

        else:
            print(f"{self.name} yutqazdi")


g1 = GamePlayer("Ali", 100)
g1.res()

g2 = GamePlayer("Ali", 45)
g2.res()
