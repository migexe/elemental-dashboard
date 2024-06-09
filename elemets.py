#Importing customtkinter module
import customtkinter
from customtkinter import *

#The main customtkinter frame
app = CTk()
app.geometry("700x600+400+50")
set_appearance_mode("dark")
app.resizable(False,False)

#The function for the whole answer widget
def answer():

#The function to for the back button in answer widget
    def back():
       answer_form.destroy()

####What if the user has entered nothing
    if search_bar.get().lower() == "":
        print("There is nothing")
        notice = CTkLabel(master = user_form,
            text="Write the element to search",
            text_color = "red",
            font = ("times new roman",15,"bold")
            )
        notice.place(rely = 0.3, relx = 0.5, anchor = "center")
        notice.after(1000,notice.destroy)

#What if the user enters an unrecognised text
    elif search_bar.get().lower() not in elements.keys():
        print("Can't find it in the periodic table")
        alert = CTkLabel(master = user_form,
            text="Can't find that element.Enter the full name!",
            text_color = "red",
            font = ("times new roman",15,"bold")
            )
        alert.place(rely = 0.3, relx = 0.5, anchor = "center")
        alert.after(2000,alert.destroy)

#If the user has entered the correct element
    else:
        def show_element_info():
            element = search_bar.get().lower()
            if element in elements:
                info = elements[element]
                final_answer.configure(text=f"ABOUT THE ELEMENT {element}\n\n\nSymbol:     {info['Symbol']}\n\n\nGroup:     {info['Group']}\n\n\n Period:     {info['Period']}\n\n\nNucleon number/Atomic mass:  {info['Nucleon number/Atomic mass']}\n\n\nProton number/atomic number:  {info['Proton number/atomic number']}\n\n\nNumber of electrons in outer shell:  {info['Number of electrons in outer shell']} ")

#The frame for the answers
        answer_form = CTkFrame(master = app,
        fg_color = "#FFFFFF",
        height = 300,
        width = 500,
        corner_radius = 20
        )
        answer_form.pack(fill = BOTH, expand = True)


        final_answer = CTkLabel(master = answer_form, text = "", text_color="black",font = ("times new roman",20,"bold"))
        final_answer.pack()

        show_element_info()

        back_button = CTkButton(master = answer_form, text = "BACK", corner_radius = 32, fg_color = "transparent", hover_color = "black", border_color = "black", border_width = 2, text_color = "grey", font = ("times new roman",20,"bold"),width = 300,height = 50, command = back)
        back_button.place(rely = 0.9, relx = 0.5, anchor = "center")
#The function for the whole answer widget ends here

#The answer dictionary
elements = {"sodium":{"Symbol":"Na","Group":1,"Period":3,"Nucleon number/Atomic mass":5,"Proton number/atomic number":7,"Number of electrons in outer shell":10},"carbon":{"Symbol":"Na","Group":6,"Period":10,"Nucleon number/Atomic mass":9,"Proton number/atomic number":10,"Number of electrons in outer shell":10}}
#The answer dictionary ends in here


#the Frame for searching for the element
user_form = CTkFrame(master = app,
    fg_color = "#FFFFFF",
    height = 300,
    width = 500,
    corner_radius = 20
    )
user_form.place(relx = 0.5, rely = 0.5, anchor="center")

#the label to command the user to search for the element
search = CTkLabel(master = user_form,
 text = "SEARCH FOR THE ELEMENT",
  text_color = "black",
  font = ("helvetica",20,"bold")
  )
search.place(rely = 0.1, relx = 0.5, anchor = "center")

#The user input
search_bar = CTkEntry(
	master = user_form,
	placeholder_text = "Enter the element......", width = 400, text_color = "black", fg_color = "white", font = ("times new roman",25,"bold"), height = 60)
search_bar.place(rely = 0.4, relx = 0.5, anchor = "center")


#The button to find the answer
search_button = CTkButton(master = user_form, text = "SEARCH", corner_radius = 32, fg_color = "transparent", hover_color = "black", border_color = "black", border_width = 2, text_color = "grey", font = ("times new roman",20,"bold"),width = 300,height = 50, command = answer)
search_button.place(rely = 0.8, relx = 0.5, anchor = "center")

app.mainloop()
