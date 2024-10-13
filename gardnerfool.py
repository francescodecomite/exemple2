TAILLE=500
pourcentage=0.05
from math import *

def decalage(c,percent=pourcentage):
    return "\"translate("+str(c*percent)+","+str(c*percent)+")\""

#grouper deux rectangles pour définir le cadre
def rectangle(c=TAILLE,percent=pourcentage,transform=""):
    s="<g> <rect x=\""+str(percent*c)+"\" y=\""+str(c*percent)+"\" width=\""+str(c)+"\" height=\""+str(c)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    print(s)
    sprime="<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"
    print(sprime)
    return s+"<rect x=\"0\" width=\""+str(c*(1+2*percent))+"\" height=\""+str(c*(1+2*percent))+"\" rx=\"25\" fill=\"none\" stroke=\"red\" transform="+transform+ "/></g>\n"

def simplerectangle(c=TAILLE,percent=pourcentage,transform=""):
    s="<rect x=\""+str(0)+"\" y=\""+str(0)+"\" width=\""+str(c)+"\" height=\""+str(c*percent)+"\" fill=\"none\" stroke=\"red\" transform="+transform+ "/>\n"
    return s

def ligne(debut,fin,transform=""):
     s="<line x1=\""+str(debut[0])+"\" y1=\""+str(debut[1])+"\" x2=\""+str(fin[0])+"\" y2=\""+str(fin[1])+"\" stroke=\"black\"   transform="+transform+" />\n"
     return s
    


    
def gardner(c=TAILLE,transform=""):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("gardner.svg","w")
    image.write(entete)
    alpha=atan(0.5)
    a=50
    largeur=a*(3*sin(alpha)+5*cos(alpha))
    largeur=a*(1+3*cos(alpha)+sqrt(5))

    hauteur=a*(3*sin(alpha)+4*cos(alpha))
    rapport=hauteur/largeur
##    image.write(ligne((0,0),(0,largeur)))
##    image.write(ligne((0,0),(hauteur,0)))
##    image.write(ligne((0,largeur),(hauteur,largeur)))
##    image.write(ligne((hauteur,0),(hauteur,largeur)))
    image.write(simplerectangle(largeur,rapport,""))
    # dessiner les polyominos
    #image.write("<polygon  points=\"0,0 600,0 600,200 700,200 700,600 300,600 300,700 0,700\" fill=\"none\" stroke=\"black\" transform="+transform+"/>\n")
    # le T
    image.write("<polygon  points=\"0,0 0,"+str(3*a)+" "+ str(a)+","+str(3*a)+" "+str(a)+","+str(2*a)+" "+str(3*a)+","+str(2*a)+" "+str(3*a)+","+str(a)+" "+str(a)+","+str(a)+" "+str(a)+","+str(0)+" "+str(0)+","+str(0)+"\" fill=\"none\" stroke=\"blue\" />\n")
    # Le Z
    image.write("<polygon  points=\"0,0 0,"+str(2*a)+" "+ str(2*a)+","+str(2*a)+" "+str(2*a)+","+str(3*a)+" "+str(3*a)+","+str(3*a)+" "+str(3*a)+","+str(a)+" "+str(a)+","+str(a)+" "+str(a)+","+str(0)+" "+str(0)+","+str(0)+"\" fill=\"none\" stroke=\"lime\" />\n")
    # Le F
    image.write("<polygon  points=\"0,0 0,"+str(2*a)+" "+ str(a)+","+str(2*a)+" "+str(a)+","+str(3*a)+" "+str(2*a)+","+str(3*a)+" "+str(2*a)+","+str(2*a)+" "+str(3*a)+","+str(2*a)+" "+str(3*a)+","+str(a)+" "+str(a)+","+str(a)+" "+str(a)+","+str(0)+" "+str(0)+","+str(0)+"\" fill=\"none\" stroke=\"orange\" />\n")
    # L'equerre
    image.write("<polygon  points=\"0,0 0,"+str(a)+" "+ str(2*a)+","+str(a)+" "+str(2*a)+","+str(2*a)+" "+str(3*a)+","+str(2*a)+" "+str(3*a)+","+str(a)+" "+str(4*a)+","+str(a)+" "+str(4*a)+","+str(0)+"\" fill=\"none\" stroke=\"black\" />\n")
    print(largeur*hauteur/(a*a))
    print(largeur/a)
    print(hauteur/a)
 
    image.write(pied)
    image.close()

gardner()
