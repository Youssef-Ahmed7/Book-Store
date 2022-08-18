from tkinter import *
from tkinter import messagebox
# color and data variables
fg = "#0d5bdb"    # blue = #0d5bdb
bg = "#111e3e"
font = "Roboto"
table_heading = "0e16a3"
font_size = 25
button_font = 15
####################################################################################
# starting functions section
def main_display_button():
    #**********************************************
    file = open("data.txt", "r")
    check_file = file.read()
    if check_file == "":
       impty_window = Tk()
       impty_window.geometry("600x500")
       impty_window.wm_iconbitmap("book.ico")
       impty_window.title("Warning")
       impty_window.config(bg=bg)
       impty_label = Label(impty_window,fg="white",bg=bg,font=(font,font_size),text="No Available Books")
       impty_label.pack(expand=YES)

    else:
            # get data from the file

            file = open("data.txt", "r")
            # take the data from file

            new_data = file.read().split("\n")
            for i in range(0, len(new_data)):
                new_data[i] = new_data[i].split("#*")
                file.close()
            print(len(new_data))
            print(new_data)
            titles = [["ISBN", "Title", "Author", "Description"]]
            lst = titles + new_data
            total_rows = len(lst)
            total_columns = len(lst[0])
            # *********************************************
            display_window = Tk()
            display_window.geometry("600x500")
            display_window.wm_iconbitmap("book.ico")
            display_window.title("Display Books")
            display_window.config(bg = bg)
            table_frame = Frame(display_window)
            table_frame.pack(expand=YES)
            display_text = Label(table_frame,text="{} Of Amazing Books".format(total_rows-1), bg=fg, fg = "white", font=(font, font_size, "bold"), pady=10,padx=10)
            display_text.pack()

        # creating the table
            class Table:
                def __init__(self,  display_window):
                    # code for creating table
                    for i in range(total_rows):
                        for j in range(total_columns):
                            if i==0:
                                self.e = Entry(display_window, width=20, fg="white", bg="#003a7f",font=(font, font_size, 'bold'),border=1)
                            else:
                                 self.e = Entry( display_window, width=20, fg="white", bg=fg, font=(font, font_size, 'bold'))
                            self.e.grid(row=i, column=j)
                            self.e.insert(END, lst[i][j])
            table_frame = Frame(display_window)
            table_frame.pack(expand=YES)
            table= Table(table_frame)
            display_window.mainloop()
def main_Enter_button():
    Enter_window = Tk()
    Enter_window.geometry("600x500")
    Enter_window.wm_iconbitmap("book.ico")
    Enter_window.title("Enter Details")
    Enter_window.config(bg = bg,pady=10,padx=10)
    isbn_text = Label( Enter_window,text="ISBN",font=(font,font_size),fg="white",bg=bg,border=0,width=10,height=2)
    isbn_text.grid(column= 0 , row=0)
    isbn = Entry( Enter_window,width=20,bg=fg,fg = "white",font=(font,font_size))
    isbn.grid(column= 4 , row=0)
    title_text = Label( Enter_window,text="Title",font=(font,font_size),fg="white",bg=bg,border=0,width=10,height=2)
    title_text.grid(column= 0 , row=2)
    title = Entry( Enter_window,width=20,bg=fg,fg = "white",font=(font,font_size))
    title.grid(column= 4 , row=2)
    author_text = Label(Enter_window, text="Author", font=(font, font_size), fg="white", bg=bg, border=0, width=10, height=2)
    author_text.grid(column=0, row=4)
    author = Entry(Enter_window, width=20, bg=fg, fg="white", font=(font, font_size))
    author.grid(column=4, row=4)
    disc_text = Label(Enter_window, text="Description", font=(font, font_size), fg="white", bg=bg, border=0, width=10,height=2)
    disc_text.grid(column=0, row=6)
    disc = Entry(Enter_window, width=20, bg=fg, fg="white", font=(font, font_size))
    disc.grid(column=4, row=6)
    def save_action():
        if isbn.get() == "" or title.get() == "" or author.get() == "" or disc.get() == "":
            messagebox.showinfo("Warning", "You should write all information")
        else:
            if (isbn.get().isnumeric()) and ( title.get().isnumeric() == False) and ( author.get().isnumeric() == False) and (disc.get().isnumeric() == False):
                file = open("data.txt", "r")
                check_file = file.read()
                file.close()
                if check_file == "":
                    file = open("data.txt", "w")
                    file.write("{0}#*{1}#*{2}#*{3}".format(isbn.get(), title.get(), author.get(), disc.get()))
                else:
                    file = open("data.txt", "a")
                    file.write("\n{0}#*{1}#*{2}#*{3}".format(isbn.get(), title.get(), author.get(), disc.get()))
                isbn.delete(0,len(isbn.get()))
                title.delete(0, len(title.get()))
                author.delete(0, len(author.get()))
                disc.delete(0, len(disc.get()))
            else:
                messagebox.showinfo("Warning","ISBN must be a number, title,Author and Description must be a string")
    save_button = Button(Enter_window, text="Save", fg="white", bg=fg, font=(font, button_font), width=20,command=save_action)
    save_button.grid(column=0, row=7)





#############################################################################################

# Starting main widow section
main_window = Tk()
main_window.geometry("600x500")
main_window.wm_iconbitmap("book.ico")
main_window.title("Book Store")
main_window.config(bg=bg)
main_frame = Frame(main_window)
main_frame.pack(expand=YES)
main_frame.config(bg=bg)
main_text = Label(main_frame,text="Welcome to our book store", bg=bg, fg="white", font=(font,font_size))
main_text.pack()
# but the image
main_image = PhotoImage(file="image.png").zoom(6).subsample(15)
main_canvas = Canvas(main_frame, width=550,height=350, bg=bg,bd=0,highlightthickness=0)
main_canvas.create_image(550/2,350/2, image = main_image)
main_canvas.pack()
main_button_frame = Frame(main_frame)
main_button_frame.pack(expand=YES)
main_display_button = Button(main_button_frame,text="Display",bg=fg,fg="white",font=(font,button_font),pady=5,padx=5,width=10,command=main_display_button)
main_display_button.pack(side=LEFT)
main_Enter_button = Button(main_button_frame,text="Enter",bg=fg,fg="white",font=(font,button_font),pady=5,padx=5,width=10,command=main_Enter_button)
main_Enter_button.pack(side=RIGHT)
###################################################################################
main_window.mainloop()