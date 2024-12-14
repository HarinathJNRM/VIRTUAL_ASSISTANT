from tkinter import*
from PIL import Image, ImageTk  #To add Image in Tkinter becoz tkinter directly not allows to add pictures. So, module PILLOW is imported.
import speech_to_text
import action
root = Tk()                     #To create Window
root.title("DESKTOP Assistant")      #To give Name to window
root.geometry("550x675")        #To create height and width of window
root.resizable(False, False)    #To fix the window size and dont allow user to re-size the window
root.config(bg="#6F8FAF")       #To give back-ground color for window


#'ask' Function for (BUTTON1)
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+ user_val+"\n")
    if(bot_val != None):
        text.insert(END, "BOT <---"+str(bot_val)+"\n")
        
    if(bot_val == 'Okay, sir'):
        root.destroy()
        

#'send' Function for (BUTTON2)
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->'+ send+"\n")
    if(bot != None):
        text.insert(END, "BOT <---"+str(bot)+"\n")
    if(bot == 'Okay, sir'):
        root.destroy()
        

#'delete' Function for (BUTTON3)
def del_text():
    text.delete('1.0', "end")


#FRAME
frame = LabelFrame(root, padx= 100, pady= 7, borderwidth= 3, relief= 'raised')
frame.config(bg="#6F8FAF")
frame.grid(row= 0, column= 1, padx= 55, pady= 10)

#TEXT LABEL INSIDE FRAME
text_label = Label(frame, text="MY ASSISTANT", font=("comic Sans ms", 14, "bold"), bg= "#356696")
text_label.grid(row= 0, column= 0, padx= 20, pady= 10)

#IMAGE
image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame, image=image)
image_label.grid(row= 1, column= 0, pady= 20)

#ADDING TEXT WIDGET
text = Text(root, font=('courior 10 bold'), bg="#356696")
text.grid(row= 2, column= 0)
text.place(x= 100, y= 375, width= 375, height= 100)

#ENTRY WIDGET (Where User can enter Text)
entry = Entry(root, justify= CENTER)
entry.place(x= 100, y= 500, width= 350, height= 30)

#BUTTON1
Button1 = Button(root, text = "ASK", bg= "#356696", padx= 40, pady= 16, borderwidth= 3, relief= SOLID, command=ask)
Button1.place(x= 70, y= 575)

#BUTTON2
Button2 = Button(root, text = "Send", bg= "#356696", padx= 40, pady= 16, borderwidth= 3, relief= SOLID, command=send)
Button2.place(x= 400, y= 575)

#BUTTON3
Button3 = Button(root, text = "Delete", bg= "#356696", padx= 40, pady= 16, borderwidth= 3, relief= SOLID, command=del_text)
Button3.place(x= 225, y= 575)



root.mainloop()                 #To create Window