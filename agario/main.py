import core
from agario.partie import Partie


def setup():
    print("start setup")
    core.WINDOW_SIZE = [800,600]
    core.fps = 60

    core.memory("partie",Partie())

    core.memory("partie").addPlayer
    core.memory("partie").addBot()

    print("End setup")



def run():
    core.cleanScreen()
    core.memory("partie").show()



core.main(setup,run)
