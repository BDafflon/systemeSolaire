from soleil import Soleil


class Systeme:
    def __init__(self):
        self.soleil = Soleil()
        self.planetes = []
        self.nom = "systeme solaire"
        self.largeur = 400
        self.hauteur = 400

    def ajout(self,p):
        self.planetes.append(p)
        print(self.planetes)

    def update(self):
        for p in self.planetes:
            p.applyForce(self.soleil)
            p.deplacer()

    def afficher(self,screen):
        self.soleil.afficher(screen)

        for p in self.planetes:
            p.afficher(screen)