import core


def setup():
    print("start setup")
    core.WINDOW_SIZE = [800,600]
    core.fps = 60
    core.memory("etat",Etat.MENU)
    print('"End setup')


def afficherMenu():
    core.Draw.rect(255,0,0),(355,280,90,40)
    core.Draw.rect((255,255,255),"JOUER",(357,282),30)

    if core.getMouseLeftClick()
        position = core.getMouseLeftClick()
        rec = Rect(355,280,90,40)
        if rec.collidepoint(position)
            core.memory("etat",Etat.JEU)

def afficherJeu():
    core.Draw.circle((255,0,0),(100,222),10)

def afficherGameOver():
    print("GameOver")


def run():
    core.cleanScreen()

    if core.memory('etat') == Etat.MENU:
        afficherMenu()

    if core.memory('etat') == Etat.JEU:
        afficherJeu()

    if core.memory('etat') == Etat.GAMEOVER:
        afficherGameOver()


core.main(setup,run)





