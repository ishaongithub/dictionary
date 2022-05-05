# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:14:05 2022

@author: ishar
"""
from tkinter import *
root = Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(bg="purple")



label_of_supernova= Label(root, bg="pink")
label_of_comet= Label(root, bg="pink")
label_of_meteor= Label(root, bg="pink")
label_of_spiral_galaxy= Label(root, bg="pink")
label_of_nebula= Label(root, bg="pink")

dictionary={'Supernova':'A supernova is the explosion of a star at the end of its life. Supernovas are one of the largest space explosions.',
            'Comet':'Comets are frozen leftovers from the formation of the solar system composed of dust, rock, and ices. As they orbit closer to the sun, they heat up and spew gases and dust into a glowing head that can be larger than a planet.',
            'Meteor':'A meteor is a piece of rock or metal that burns very brightly when it enters the atmosphere of the Earth from space.',
            'Spiral Galaxy':'A spiral galaxy typically is a galaxy has a rotating disc with spirals that curve out from a dense central region. ',
            'Nebula':'A nebula is an enormous cloud of dust and gas occupying the space between stars and acting as a nursery for new stars. '
            }

def supernova():
    label_of_supernova["text"]=dictionary["Supernova"]
    
def comet():
    label_of_comet["text"]=dictionary["Comet"]
    
def meteor():
    label_of_meteor["text"]=dictionary["Meteor"]
    
def spiral():
    label_of_spiral_galaxy["text"]=dictionary["Spiral Galaxy"]
    
def nebula():
    label_of_nebula["text"]=dictionary["Nebula"]
    
button_supernova= Button(root, text="Meaning of Supernova", command=supernova, bg="light blue")
button_supernova.place(relx=0.5, rely=0.1, anchor = CENTER)
label_of_supernova.place(relx=0.5, rely=0.15, anchor=CENTER)

button_comet= Button(root, text="Meaning of Comet", command=comet, bg="light blue")
button_comet.place(relx=0.5, rely=0.3, anchor = CENTER)
label_of_comet.place(relx=0.5, rely=0.35, anchor=CENTER)

button_meteor= Button(root, text="Meaning of Meteor", command=meteor, bg="light blue")
button_meteor.place(relx=0.5, rely=0.5, anchor = CENTER)
label_of_meteor.place(relx=0.5, rely=0.55, anchor=CENTER)

button_spiral_galaxy= Button(root, text="Meaning of Spiral Galaxy", command=spiral, bg="light blue")
button_spiral_galaxy.place(relx=0.5, rely=0.7, anchor = CENTER)
label_of_spiral_galaxy.place(relx=0.5, rely=0.75, anchor=CENTER)

button_nebula= Button(root, text="Meaning of Nebula", command=nebula, bg="light blue")
button_nebula.place(relx=0.5, rely=0.9, anchor = CENTER)
label_of_nebula.place(relx=0.5, rely=0.95, anchor=CENTER)



root.mainloop()

