#Imports
try:
    import os
    import sys
    import webbrowser
    import ctypes

    from PIL import Image, ImageTk

    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog

except ImportError:
    try:
        from tkinter import messagebox
        messagebox.showerror("Error (Code E001)", "Ein oder mehrere Modul(e) konnte nicht importiert werden. Das Programm startet nicht.")
        sys.exit(1)
    except ImportError:
        print("Error (Code E001)", "Ein oder mehrere Modul(e) konnte nicht importiert werden. Das Programm startet nicht.")
        sys.exit(0)
    except:
        print("Error (Code E000)", "Ein unbekannter Fehler ist aufgetreten. Das Programm startet nicht.")
        sys.exit(0)
except:
    print("Error (Code E000)", "Ein unbekannter Fehler ist aufgetreten. Das Programm startet nicht.")
    sys.exit(0)

from PIL import Image, ImageTk


#App-ID
try:
    appid = u'tkdev.bewertungsbogen.bwb.3-0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
except Exception as e:
    print(f"Error (Code E003): {e}")
    messagebox.showerror(f"Error (Code E003)", "Ein unerwarteter Fehler ist aufgetreten. Das Program startet nicht. (Could not init App-ID)")
    sys.exit(3)


#Script directory
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except Exception as e:
    print(f"Error (Code E005): {e}")
    messagebox.showerror("Error (Code E005)","Ein unerwarteter Fehler ist aufgetreten. Das Program startet nicht. (Could not init script_dir)")
    sys.exit(5)


#Function to get dir -> At the time not used 
def select_directory():
    try:
        dirselect = Tk.tk()
        dirselect.withdraw()  # hide the root window
        directory = filedialog.askdirectory(title="Select a directory")
        return directory
    except Exception as e:
        print(f"Error (Code E005): {e}")
        messagebox.showerror(f"Error (Code E005)", "Fehler bei der Speicherortauswahl.")




#Create about window
def create_about_window():
    try:
        about_window = Toplevel(mainWindow)
        about_window.title("Über dieses Programm")
        about_window.geometry("300x220")
        about_window.resizable(False, False)
        Label(about_window, font=('TkDefaultFont', 21), text="Bewertungsbogen").pack()
        Label(about_window, font=('TkDefaultFont', 10), text="Version 3.0").pack()
        Label(about_window, font=('TkDefaultFont', 10), text="Copyright 2024 Tobias Kisling").pack()
        Label(about_window, font=('TkDefaultFont', 10), text="Diese Software ist durch\ndie MIT-License freigegeben.\nFür weitere Informationen lesen Sie \nbitte die Readme-Datei, die der \nInstallation beiliegt.").pack()
        Label(about_window, font=('Verdana', 10), text="tk_dev - Software with passion!").pack()
        Button(about_window, text="Schließen", command=about_window.destroy).pack()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror(f"Error (Code E003)", "Ein unerwarteter Fehler ist aufgetreten.")

#Create settings windows
def create_settings_window():
    try:
        settings_window = Toplevel(mainWindow)
        settings_window.title("Settings")
        settings_window.geometry("400x310")
        settings_window.resizable(False, False)

        Label(settings_window, font=("TkDefaultFont", 21), text="Einstellungen").pack()
        Label(settings_window, font=("TkDefaultFont"), text="").pack()
        rsscreatebutton = Button(settings_window, text="Kriterien-Speicherung neu erstellen", command=create_ruleset_save_doc)
        rsscreatebutton.pack()
        Label(settings_window, font=("TkDefaultFont"), text="").pack()
        rssdeletebutton = Button(settings_window, text="Kriterien-Speicherung löschen", command=delete_all_ruleset_save_docs)
        rssdeletebutton.pack()
        Label(settings_window, font=("TkDefaultFont"), text="").pack()
        deleteoutputbutton = Button(settings_window, text="Gesamten Output löschen", command=delete_all_output)
        deleteoutputbutton.pack()
        Label(settings_window, font=("TkDefaultFont"), text="").pack()
        Label(settings_window, font=("TkDefaultFont"), text="").pack()
        Label(settings_window, font=('Verdana', 14), text="Bewertungsbogen 3.0.0 (Initial Release)").pack()
        Label(settings_window, font=('Verdana', 14), text="tk_dev - Software with passion!").pack()
        Button(settings_window, text="Schließen", command=settings_window.destroy).pack()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror(f"Error (Code E003)", "Ein unerwarteter Fehler ist aufgetreten.")


#Documentation
def open_documentation():
    try:
        #Check if file exists:
        if os.path.exists(os.path.join(script_dir, "res/documentation.html")):
            file_name = 'documentation.html'
            current_directory = os.path.dirname(__file__)
            file_path = os.path.join(current_directory, file_name)
            url = 'file://' + file_path
            webbrowser.open(url, new=2)  # open in new tab
        else:
            messagebox.showerror("Error (Code E002)", "Ein internes Dokument wurde nicht gefunden.")
    except Exception as e:
        print(f"Error (Code E002): {e}")
        messagebox.showerror("Error (Code E002)", "Ein internes Dokument wurde nicht gefunden.")

    
#Bugreport
def open_bugreport():
    try:
        if os.path.exists(os.path.join(script_dir, "res/bugreport.html")):
            file_name = 'bugreport.html'
            current_directory = os.path.dirname(__file__)
            file_path = os.path.join(current_directory, file_name)

            url = 'file://' + file_path
            webbrowser.open(url, new=2)  # open in new tab
        else:
            messagebox.showerror("Error (Code E002)", "Ein internes Dokument wurde nicht gefunden.")
    except Exception as e:
        print(f"Error (Code E002): {e}")
        messagebox.showerror("Error (Code E002)", "Ein internes Dokument wurde nicht gefunden.")














#Dropdown values
def get_dd_values():
    try:
        global dd_inputvar 
        dd_inputvar = clicked.get()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")

#Student name
def getsnameinput():
    try:
        global sname_inputvar
        sname_inputvar = snameinput.get("1.0", END).strip()
        create_output()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")



#Slider vars
def get_slider_values():
    try:
        global slider_inputvar
        slider_inputvar = [
            slider1.get(),
            slider2.get(),
            slider3.get(),
            slider4.get(),
            slider5.get(),
            slider6.get(),
            slider7.get(),
            slider8.get(),
            slider9.get(),
            slider10.get(),
            slider11.get(),
            slider12.get()
        ]
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")

#save general settings
def save_general_settings():
    try:
        global swinputvar, scinputvar, sdinputvar, stinputvar
        swinputvar = swinput.get("1.0", END).strip()
        scinputvar = scinput.get("1.0", END).strip()
        sdinputvar = sdinput.get("1.0", END).strip()
        stinputvar = stinput.get("1.0", END).strip()
        scvi_window.destroy() #Close window after saving
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")

#create generall settings
def create_general_settings_window():
    try:
        global swinputvar, scinputvar, sdinputvar, stinputvar, swinput, scinput, sdinput, stinput
        global scvi_window #To kill window by button

        scvi_window = Toplevel(mainWindow)
        scvi_window.title('Generelle Einstellungen ändern')
        scvi_window.geometry('450x370')

        Label(scvi_window, font=('TkDefaultFont', 21), text="Generelle Einstellungen ändern").pack()
        Label(scvi_window, font='TkDefaultFont', text="\nDiese Einstellungen werden\nfür die gesamte Session gespeichert.\n\nLeergelassene Felder werden\n auf dem Dokument nicht angezeigt.\n").pack()

        Label(scvi_window, text="Name der Arbeit eingeben: ").pack()
        swinput = Text(scvi_window, font="TkDefaultFont", height=1, width=20, blockcursor=False)
        swinput.pack()

        Label(scvi_window, text="Klasse eingeben: ").pack()
        scinput = Text(scvi_window, font="TkDefaultFont", height=1, width=20, blockcursor=False)
        scinput.pack()

        Label(scvi_window, text="Datum eingeben: ").pack()
        sdinput = Text(scvi_window, font="TkDefaultFont", height=1, width=20, blockcursor=False)
        sdinput.pack()

        Label(scvi_window, text="Name der Lehrperson eingeben: ").pack()
        stinput = Text(scvi_window, font="TkDefaultFont", height=1, width=20, blockcursor=False)
        stinput.pack()

        Button(scvi_window, text="Speichern", command=save_general_settings).pack()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")



#Set rulesets
def set_ruleset_preview():
    try:
        global ruleset_current 
        global Label4, Label5, Label6, Label7, Label8, Label9, Label10, Label11, Label12, Label13, Label14, Label15
    
        for i in range(12):
            globals()[f'ruleset_preview_{i + 1}'] = ruleset_current[i]
            globals()[f'Label{i + 4}'].config(text=globals()[f'ruleset_preview_{i + 1}'])
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")
    
#Create rss document
def create_ruleset_save_doc():
    try:
        create_rs_doc = open("Kriterien-Speicherung.txt", "w")
        create_rs_doc.write("Hier koennen Beurteilungskriterien eingeben werden.\nEs koennen bis zu 12 Kriterien eingefuegt werden.\nLeere Zeilen bzw. Zeilen ausserhalb des Limits (Zeilen zwischen den '#') werden nicht beruecksichtigt.\nGenaueres kann im Info-Dokument gelesen werden.\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###\n\n###\n\n\n\n\n\n\n\n\n\n\n\n\n###")
        create_rs_doc.close()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")

#Delete rss document
def delete_all_ruleset_save_docs():
    try:
        should_delete_rss = messagebox.askokcancel("Warnung","Diese Operation löscht alle gespeicherten Bewertungskriterien!\nFortfahren?")
        if should_delete_rss:
            if os.path.isfile("Kriterien-Speicherung.txt"):
                os.remove("Kriterien-Speicherung.txt")
            else:
                messagebox.showerror("Error (Code E006)", "Die Datei existiert nicht.\nFalls Sie die Datei neu erstellen wollen, benutzen Sie die Option 'Kriterien-Datei neu erstellen' in den Einstellungen.")
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")

#Read rss document
def read_rs_doc():
    try:
        if not os.path.exists("Kriterien-Speicherung.txt"):
            create_ruleset_save_doc()
            messagebox.showwarning("Error (Code E006)", "Es sind keine Bewertungskriterien festgelegt. Legen Sie diese in der Datei 'Kriterien-Speicherung' fest.")
        else:
            global ruleset_current
            ruleset_current = []
            with open("Kriterien-Speicherung.txt", "r") as file:
                lines = file.readlines()
                get_dd_values()
                option_index = optionsdd1.index(dd_inputvar)
                start_line = 5 + (option_index * 15)
                end_line = start_line + 12
                for i in range(start_line, end_line):
                    ruleset_current.append(lines[i].strip())
            set_ruleset_preview()
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")


# Output creation
def open_output():
    try:
        output_name = sname_inputvar + " - Bewertung.html"
        if os.path.exists(os.path.join(script_dir, output_name)):
            file_name = output_name
            current_directory = os.path.dirname(__file__)
            file_path = os.path.join(current_directory, file_name)
            url = 'file://' + file_path
            webbrowser.open(url, new=2)  # open in new tab
        else:
            messagebox.showerror("Error (Code E007)", "Das erstellte Dokument konnte nicht geöffnet werden.")
    except:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")









#Create output
def create_output():
    try: 
        get_slider_values() 
        read_rs_doc()
        output_file_name = sname_inputvar + " - Bewertung" + ".html" 
        
        with open(output_file_name, "w") as output_file_create: 
            output_file_create.write("<!--This code has been generated by Bewertungsbogen, an application from tk_dev-->\n") 
            output_file_create.write("<!DOCTYPE html>\n") 
            output_file_create.write("<html lang='de-at'>\n") 
            output_file_create.write("<head>\n") 
            output_file_create.write("<meta charset='UTF-8'>\n")
            output_file_create.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')  
            output_file_create.write("<title>" + sname_inputvar + " - Bewertung</title>\n") 
            output_file_create.write('<link rel="stylesheet" href="res/display_styles.css">\n') 
            output_file_create.write("</head>\n") 
            output_file_create.write("<body>\n")

            output_file_create.write("<p class='error'>Falls Sie dies sehen, wird die Seite möglicherweise nicht korrekt angezeigt.<br>Aktualisieren Sie die Seite oder erstellen Sie das Dokument neu</p>\n")
            output_file_create.write("<div class='print-instructions'>Drücken Sie STRG + P um das Dokument zu drucken oder abzuspeichern.</div>\n")
            
            output_file_create.write("<div class='main-container'>\n")

            output_file_create.write('<div class="title-container"><h1>Bewertung</h1></div>\n')
            output_file_create.write("<div class='data-container'>\n")
            output_file_create.write("<h2>" + sname_inputvar + "</h2>\n")
            output_file_create.write("<p>Klasse: " + scinputvar + "</p>\n")
            output_file_create.write("<p>Lehrperson: " + stinputvar + "</p>\n")
            output_file_create.write("<p>Arbeit: " + swinputvar + "</p>\n")
            output_file_create.write("</div>\n") 

            output_file_create.write("<div class='rating-container'>\n")

            for i in range(12):
                if slider_inputvar[i] != 0: 
                    output_file_create.write("<div class='criteria'><p>" + globals()[f'ruleset_preview_{i + 1}'] + "</p></div>\n") 
                    if slider_inputvar[i] == 1: 
                        output_file_create.write("<div class='rating'><p>Sehr gut gelungen</p></div>\n") 
                    elif slider_inputvar[i] == 2: 
                        output_file_create.write("<div class='rating'><p>Gut gelungen</p></div>\n") 
                    elif slider_inputvar[i] == 3: 
                        output_file_create.write("<div class='rating'><p>Mittelmaessig gelungen</p></div>\n") 
                    elif slider_inputvar[i] == 4: 
                        output_file_create.write("<div class='rating'><p>Wenig gelungen</p></div>\n") 
                    elif slider_inputvar[i] == 5: 
                        output_file_create.write("<div class='rating'><p>Nicht gelungen</p></div>\n") 
                output_file_create.write("\n")
            
            output_file_create.write("</div>\n")
            output_file_create.write("</div>\n")

            output_file_create.write("<script>\n")
            output_file_create.write("window.addEventListener('beforeprint', function() {\n")
            output_file_create.write("console.log('Print dialog is about to open.');\n")
            output_file_create.write("});\n")
            output_file_create.write("window.addEventListener('afterprint', function() {\n")
            output_file_create.write("console.log('Print dialog is now closed.');\n")
            output_file_create.write("});\n")
            output_file_create.write("</script>\n")

            output_file_create.write("</body>\n")
            output_file_create.write("</html>\n")
        try:
            open_output() 
        except Exception as e:
            print(f"Error (Code E003): {e}")
            messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")







#Delete output
def delete_all_output():
    try:
        output_found = False
        should_delete_output = messagebox.askokcancel("Warnung","Diese Operation löscht alle Bewertungsdateien!\nFortfahren?")
        if should_delete_output == True:
            for filename in os.listdir():
                if filename.endswith(" - Bewertung.html"):
                    os.remove(filename)
                    output_found = True
            if output_found == True: 
                messagebox.showinfo("Erfolg", "Alle Bewertungsdateien wurden gelöscht.")
    except Exception as e:
        print(f"Error (Code E003): {e}")
        messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")
























#Center window onscreen
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = mainWindow.winfo_screenwidth()
    screen_height = mainWindow.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    mainWindow.geometry('%dx%d+%d+%d' % (width, height, x, y))

#Create programm menu
def create_menu():
    menu = Menu(mainWindow)
    mainWindow.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="Datei", menu=filemenu)
    filemenu.add_command(label="Exit", command=mainWindow.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Hilfe", menu=helpmenu)
    helpmenu.add_command(label="Über", command=create_about_window)
    helpmenu.add_command(label="Dokumentation", command=open_documentation)
    helpmenu.add_command(label="Einen Fehler melden", command=open_bugreport)

#Scroll up/down
def _on_mousewheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, 'units')
    else:
        canvas.yview_scroll(1, 'units')

#Create dropdown
def create_dropdown():
    global clicked
    global optionsdd1
    optionsdd1 = [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4",
        "Option 5",
        "Option 6",
        "Option 7",
        "Option 8",
        "Option 9",
        "Option 10",
        "Option 11",
        "Option 12",
    ]
    clicked = StringVar()
    clicked.set( "Option 1" )













#Init I
try:
    #Declare main data vars
    sname_inputvar=""
    swinputvar=""
    scinputvar=""
    sdinputvar=""
    stinputvar=""

    dd_inputvar=""
    slider_inputvar=[]



    #Create main window
    mainWindow = Tk()
    mainWindow.title('Bewertungsbogen 3.0')

    icon=Image.open("res/icon.ico")
    icon=ImageTk.PhotoImage(icon)
    mainWindow.iconphoto(True, icon)
    mainWindow.resizable(False, False)

    canvas = Canvas(mainWindow, width=100, height=600)
    scrollbar = Scrollbar(mainWindow, orient=VERTICAL, command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    #Bind scrollwheel on function
    mainWindow.bind_all("<MouseWheel>", _on_mousewheel)

except Exception as e:
    print(f"Error (Code E003): {e}")
    messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")
    sys.exit(3)


#Call functions for window
try:
    center_window(640, 509)
    create_menu()
    create_dropdown()
except Exception as e:
    print(f"Error (Code E003): {e}")
    messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten.")
    sys.exit(3)

#Place widgets
try:
    frame = Frame(canvas)

    title = Label(frame, font=('TkDefaultFont', 30), text='Konfigurationspanel')
    title.pack()

    Label2 = Label(frame, font=('TkDefaultFont', 15), text='Geben Sie hier Daten ein und bewegen die\nSlider zur gewünschten Note.\nFür Hilfe lesen Sie die Dokumentation.\n')
    Label2.pack()

    Label3 = Label(frame, font=('TkDefaultFont', 15), text='Name des Schülers / der Schülerin eingeben:')
    Label3.pack()

    snameinput = Text(frame, autoseparators=True, blockcursor=False, exportselection=True, font='TkDefaultFont', undo=True, width=15, height=1)
    snameinput.pack()

    startbutton = Button(frame, font='TkDefaultFont', text='Dokument erstellen', command=getsnameinput)
    startbutton.pack()

    setsemiconvars = Button(frame, font='TkDefaultFont', text='Generelle Einstellungen/Werte ändern', command=create_general_settings_window)
    setsemiconvars.pack()

    separator1 = Frame(frame, height=2, borderwidth=1, relief="solid")
    separator1.pack(fill="x", padx=10, pady=20)





    Label4 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (1)')
    Label4.pack()

    slider1 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider1.pack()
    slider1.set(3)

    Label5 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (2)')
    Label5.pack()

    slider2 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider2.pack()
    slider2.set(3)

    Label6 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (3)')
    Label6.pack()

    slider3 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider3.pack()
    slider3.set(3)

    Label7 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (4)')
    Label7.pack()

    slider4 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider4.pack()
    slider4.set(3)

    Label8 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (5)')
    Label8.pack()

    slider5 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider5.pack()
    slider5.set(3)

    Label9 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (6)')
    Label9.pack()

    slider6 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider6.pack()
    slider6.set(3)

    Label10 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (7)')
    Label10.pack()

    slider7 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider7.pack()
    slider7.set(3)

    Label11 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (8)')
    Label11.pack()

    slider8 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider8.pack()
    slider8.set(3)

    Label12 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (9)')
    Label12.pack()

    slider9 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider9.pack()
    slider9.set(3)

    Label13 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (10)')
    Label13.pack()

    slider10 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider10.pack()
    slider10.set(3)

    Label14 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (11)')
    Label14.pack()

    slider11 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider11.pack()
    slider11.set(3)

    Label15 = Label(frame, font=('TkDefaultFont', 15), text='Keine Bewertungskriterie ausgewählt (12)')
    Label15.pack()

    slider12 = Scale(frame, from_=0, to=5, width=15, length=625,orient=HORIZONTAL)
    slider12.pack()
    slider12.set(3)




    separator2 = Frame(frame, height=2, borderwidth=1, relief="solid")
    separator2.pack(fill="x", padx=10, pady=20)

    label4 = Label(frame, font=('TkDefaultFont', 15), text='\nWählen Sie hier die Bewertungskriterien aus.\nKlicken Sie auf Aktualisieren, um die Kriterien zu laden.')
    label4.pack()

    drop1 = OptionMenu(frame , clicked , *optionsdd1) 
    drop1.pack() 

    criteria_reload_button = Button(frame, text=" Aktualisieren  ", command=read_rs_doc)
    criteria_reload_button.pack()

    separator3 = Frame(frame, height=2, borderwidth=1, relief="solid")
    separator3.pack(fill="x", padx=10, pady=20)

    open_settings_button = Button(frame, text=" Einstellungen ", command=create_settings_window)
    open_settings_button.pack()

    title_height = title.winfo_reqheight()


    
    canvas.create_window((0, 0), window=frame, anchor='nw')
    canvas.configure(scrollregion=canvas.bbox("all"), yscrollincrement=title_height)

    frame.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.columnconfigure(0, weight=1)
    canvas.rowconfigure(0, weight=1)
    canvas.columnconfigure(0, weight=1)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    #Main loop
    mainWindow.mainloop()

except Exception as e:
    print(f"Error (Code E003): {e}")
    messagebox.showerror("Error (Code E003)", "Ein interner Fehler ist aufgetreten. Das Programm kann nicht ausgeführt werden.")
    sys.exit(3)
#Exit after done
sys.exit(0)