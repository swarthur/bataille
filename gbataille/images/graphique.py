import customtkinter
from tkinter import*
from bataille.classes.carte import Carte, SYMBOLES


def crea_images():
    app = customtkinter.CTk()
    app.title('Bataille')
    app.geometry('400X150')

    
    
    #button = customtkinter.CTkButton(app, text='Appuyer ici !', command=bouton_clique)
    #button.grid(row=2,column=0,pady=20)

    app.grid_columnconfigure(0,weight=1)


    app.attributes("-fullscreen",1)

    fond = Canvas(app,wdith=1920, height=1080,highlightthickness=1)
    fond.place(x=0,y=0)

    for symbole in SYMBOLES:
        for valeur in range(1,14):
            fichier = PhotoImage(file=f"..\\images\\{symbole}_{valeur}.png")
            image = fond.create_image(50,100,image=fichier)

    app.mainloop()