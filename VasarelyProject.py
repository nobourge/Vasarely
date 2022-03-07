"""
auteur: Bourgeois Noé
date: 16/10/2019ap.J.-C.
Programme produisant des tableaux d’art optique représentant des pavages hexagonaux, vus d’en haut,
formés avec des losanges de couleurs différentes, déformés par une boule.
"""

# import des modules externes:

from math import pi, sin, cos, sqrt
import turtle
from deformation import deformation

# définitions des constantes globales: none

# définitions des fonctions (25 lignes max):

def hexagone(point, longueur, col, centre, rayon):
    """Peint un hexagone déformé selon la fonction deformation.
        Entrées:
            point: triple donnant la valeur des trois coordonnées, du point avant déformation où l’hexagone doit être peint
            longueur: distance entre le centre et n’importe quel coin de l’hexagone
            col: tuple contenant les trois couleurs qui vont être utilisées pour dessiner les hexagones
            centre: point sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation
            rayon: rayon de la sphère de déformation
        Sortie:
            peinture de l'hexagone
    """
    milieu = deformation((point[0], point[1], point[2]), centre, rayon)                                                 #coordonnées du milieu de l'hexagone
    turtle.up()
    turtle.goto(milieu[0], milieu[1])
    turtle.down()
    for i in range(3):                                                                                                  #peinture de l'hexagone
        turtle.color(col[i])
        turtle.begin_fill()
        for j in range(3):                                                                                              #déplace turtle aux coordonnées des coins de l'hexagone
            coin = deformation((point[0] + longueur * cos(j*(pi/3)+2*i*(pi/3)), point[1] + longueur * sin(j*(pi/3)+2*i*(pi/3)), point[2]), centre, rayon)
            turtle.goto(coin[0], coin[1])
        turtle.goto(milieu[0] , milieu[1])
        turtle.end_fill()

def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """Peint les hexagones déformés dont les centres, avant déformation, se trouvent dans la fenêtre (les bords inclus)
    avec l’hexagone en bas à gauche, avant déformation, centré sur le point (inf_gauche,inf_gauche).
    Pour cela, elle utilise la fonction hexagone.
    Entrées:
        inf_gauche, sup_droit : valeurs entières donnant une fenêtre dont
                                le coin inférieur gauche est (inf_gauche, inf_gauche),
                                le coin supérieur droit est (sup_droit, sup_droit)
        longueur: longueur entre le centre et n’importe quel coin de chaque hexagone avant déformation
        col : couleurs
        centre : centre de la déformation utile pour la fonction deformation
        rayon : rayon de la sphère de déformation
    Sortie:
        peinture du pavage d'hexagones
    """
    inf_gauche_x = inf_gauche                                                                                           #coordonnées des coins de la fenêtre d'affichage
    inf_gauche_y = inf_gauche
    sup_droit_x = sup_droit
    sup_droit_y = sup_droit

    turtle.tracer(0, 0)
    i = 0
    depart_x = inf_gauche_x
    turtle.up()
    while inf_gauche_y < sup_droit_y:                                                                                   #peinture du pavage
        inf_gauche_x = depart_x
        while inf_gauche_x < sup_droit_x:                                                                               #peinture d'une ligne d'hexagones
            inf_gauche_x += longueur * 3
            turtle.down()
            hexagone(((inf_gauche_x + (i % 2*(1.5*longueur))), inf_gauche_y, 0), longueur, col, centre, rayon)          #calcul des coordonnées en x des hexagones compte tenu du décalage une ligne sur deux
            turtle.up()
        i += 1
        turtle.update()
        inf_gauche_y += sqrt((longueur**2)-(longueur/2)**2)                                                             #calcul des coordonnées en y des hexagones

# code global:

inf_gauche = int(input('veuillez introduire les coordonnées du bord inférieur gauche de la fenêtre de visualisation: ')) #demande des inputs à l'utilisateur
sup_droit = int(input('veuillez introduire les coordonnées du bord supérieur droit de la fenêtre de visualisation: '))
longueur = int(input('veuillez introduire la longueur de segment des pavés: '))
col1 = str(input('veuillez introduire la première couleur des pavés: '))
col2 = str(input('veuillez introduire la deuxième couleur des pavés: '))
col3 = str(input('veuillez introduire la troisième couleur des pavés: '))
x_c = int(input('veuillez introduire la coordonnée en x du centre de la sphère déformante: '))
y_c = int(input('veuillez introduire la coordonnée en y du centre de la sphère déformante: '))
z_c = int(input('veuillez introduire la coordonnée en z du centre de la sphère déformante: '))
rayon = int(input('veuillez introduire le rayon de la sphère déformante: '))

col = (col1, col2, col3)
centre = (x_c, y_c, z_c)

pavage(inf_gauche, sup_droit, longueur, (col1, col2, col3), (x_c, y_c, z_c), rayon)                                     # execution du pavage avec déformation
turtle.done()