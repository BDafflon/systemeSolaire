
import core
from planete import Planete
from systeme import Systeme


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("systemeSolaire", Systeme())

    core.memory("nbPlanete",5)

    for i in range(0,core.memory("nbPlanete")):
        core.memory("systemeSolaire").ajout(Planete())


    print("Setup END-----------")


def run():
    core.cleanScreen()
    core.memory("systemeSolaire").afficher(core.screen)

    core.memory("systemeSolaire").update()

core.main(setup, run)