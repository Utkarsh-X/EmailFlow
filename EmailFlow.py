"""
EmailFlow - GUI Application Main File
-------------------------------------
This is the core GUI file built using CustomTkinter.
It handles:
- The full user interface layout and components
- Theme customization and preferences
- DPI settings and visual toggles
- Email configuration (sender, receiver, subject)
- File selection and conversion UI
- Integration with the logic layer (advmail.py)

Designed for simplicity, speed, and user customization.\n
For more detail visit https://github.com/Utkarsh-X/EmailFlow
"""

# === Standard Library ===
import os
import json
import threading
import warnings
import webbrowser
from datetime import date

# === Tkinter & GUI Libraries ===
import tkinter as tk
from tkinter import colorchooser, filedialog
import customtkinter
import CTkMessagebox
from PIL import Image, ImageTk

# === Local Application Modules ===
import advmail
from version import __version__

print(f"Version: {__version__}")

def var_load():
    global var4dpi, v2, v3, theme_color, theme_color16, theme_color2, theme_colorh, switch_v_pass1, list1, switch_v_date1, switch_v_sub1, switch_v_img1, switch_v_del11, addre1, recname1
    var4dpi = "300"
    v2 = ""
    v3 = ""
    theme_color = ""
    theme_color16 = ""
    theme_color2 = ""
    theme_colorh = ""
    switch_v_pass1 = "off"
    list1 = [""]
    switch_v_date1 = "on"
    switch_v_sub1 = "on"
    switch_v_img1 = "on"
    switch_v_del11 = "on"
    addre1 = ""
    recname1 = ""


var_load()


def load_variables(filename):
    global var4dpi, v2, v3, theme_color, theme_color16, theme_color2, theme_colorh, switch_v_pass1, list1, switch_v_date1, switch_v_sub1, switch_v_img1, switch_v_del11, addre1, recname1

    try:
        with open(filename, "r") as file:  # Open the file in read mode
            data = json.load(file)  # Load data from JSON format

            var4dpi = data.get("var4dpi", var4dpi)  # Use current value if key not found
            v2 = data.get("v2", v2)
            v3 = data.get("v3", v3)
            theme_color = data.get("theme_color", theme_color)
            theme_color16 = data.get("theme_color16", theme_color16)
            theme_color2 = data.get("theme_color2", theme_color2)
            theme_colorh = data.get("theme_colorh", theme_colorh)
            switch_v_pass1 = data.get("switch_v_pass1", switch_v_pass1)
            list1 = data.get("list1", list1)

            switch_v_date1 = data.get("switch_v_date1", switch_v_date1)
            switch_v_sub1 = data.get("switch_v_sub1", switch_v_sub1)
            switch_v_img1 = data.get("switch_v_img1", switch_v_img1)
            switch_v_del11 = data.get("switch_v_del11", switch_v_del11)
            addre1 = data.get("addre1", addre1)
            recname1 = data.get("recname1", recname1)
    except FileNotFoundError:
        print(f"{filename} not found. Using default values.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}. Using default values.")


# Function to update multiple variables at once
def update_variables(updates):
    global var4dpi, v2, v3, theme_color, theme_color16, theme_color2, theme_colorh, switch_v_pass1, list1, switch_v_date1, switch_v_sub1, switch_v_img1, switch_v_del11, addre1, recname1

    # Update the variables based on the updates dictionary
    if "var4dpi" in updates:
        var4dpi = updates["var4dpi"]
    if "v2" in updates:
        v2 = updates["v2"]
    if "v3" in updates:
        v3 = updates["v3"]
    if "theme_color" in updates:
        theme_color = updates["theme_color"]
    if "theme_color16" in updates:
        theme_color16 = updates["theme_color16"]
    if "theme_color2" in updates:
        theme_color2 = updates["theme_color2"]
    if "theme_colorh" in updates:
        theme_colorh = updates["theme_colorh"]
    if "switch_v_pass1" in updates:
        switch_v_pass1 = updates["switch_v_pass1"]
    if "list1" in updates:
        list1 = updates["list1"]
    if "switch_v_date1" in updates:
        switch_v_date1 = updates["switch_v_date1"]
    if "switch_v_sub1" in updates:
        switch_v_sub1 = updates["switch_v_sub1"]
    if "switch_v_img1" in updates:
        switch_v_img1 = updates["switch_v_img1"]
    if "switch_v_del11" in updates:
        switch_v_del11 = updates["switch_v_del11"]
    if "addre1" in updates:
        addre1 = updates["addre1"]
    if "recname1" in updates:
        recname1 = updates["recname1"]


# Function to gather all data into a dictionary
def data_to_save():
    return {
        "var4dpi": var4dpi,
        "v2": v2,
        "v3": v3,
        "theme_color": theme_color,
        "theme_color16": theme_color16,
        "theme_color2": theme_color2,
        "theme_colorh": theme_colorh,
        "switch_v_pass1": switch_v_pass1,
        "list1": list1,
        "switch_v_date1": switch_v_date1,
        "switch_v_sub1": switch_v_sub1,
        "switch_v_img1": switch_v_img1,
        "switch_v_del11": switch_v_del11,
        "addre1": addre1,
        "recname1": recname1,
    }


# Function to save variables
def save_variables(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)


load_variables("data.json")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.minsize(500, 500)
app_width = 1130
app_height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 1.85)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.title("EmailFlow Manager")
root.resizable(False, False)
root.iconbitmap("emailB.ico")


def apply1():
    global var4dpi
    try:
        # Validate input
        if entrybox20.get() == "":
            var4dpi = "300"
            entrybox20.insert(0, var4dpi)
            return

        # Attempt to convert input to integer
        var4dpi = int(entrybox20.get())

        # Validate DPI range
        if var4dpi < 10 or var4dpi > 1000:
            raise ValueError(
                "DPI must be between 10 and 1000.\n Or set default DPI 200"
            )

        # Update and save variables
        update_variables({"var4dpi": var4dpi})
        save_variables("data.json", data_to_save())

    except ValueError as e:
        CTkMessagebox.CTkMessagebox(title="Error", message=str(e), option_1="Ok")
        var4dpi = "300"  # Reset to default on error


def choose_color_button():
    global theme_color
    color_code = colorchooser.askcolor(title="Choose color")[1]
    if color_code:
        theme_color = color_code
        update_variables(theme_color)
        save_variables("data.json", data_to_save())
        choose_color_button_load(theme_color)


def choose_color_button_load(theme_color):
    global widgets
    widgets = [
        menu_button,
        bs1,
        menu_button_p1,
        menu_button1,
        menu_item1,
        menu_item2,
        menu_item3,
        del_userbutton,
        add_userbutton,
        b2,
        b3,
        b4,
        b5,
    ]
    for widget in widgets:
        widget.configure(fg_color=theme_color)
    segmented_button.configure(selected_color=theme_color)

    switches = [switch1, switch2, switch3, switch4, switch6]
    for switch in switches:
        switch.configure(progress_color=theme_color)


def choose_color_button16():
    global theme_color16
    color_code1 = colorchooser.askcolor(title="Choose color")[1]
    if color_code1:
        theme_color16 = color_code1
        update_variables(theme_color16)
        save_variables("data.json", data_to_save())
        choose_color_button16_load(theme_color16)


def choose_color_button16_load(theme_color16):
    global widgets1
    widgets1 = [b6, b7, b65]
    for widget in widgets1:
        widget.configure(fg_color=theme_color16)


def choose_color_menu15():
    global theme_color2
    color_code2 = colorchooser.askcolor(title="Choose color")[1]
    if color_code2:
        theme_color2 = color_code2
        update_variables(theme_color2)
        save_variables("data.json", data_to_save())
        choose_color_menu15_load(theme_color2)


def choose_color_menu15_load(theme_color2):
    menu_frame.configure(fg_color=theme_color2)


def choose_color_hover():
    global theme_colorh
    color_code1 = colorchooser.askcolor(title="Choose color")[1]
    if color_code1:
        theme_colorh = color_code1
        update_variables(theme_colorh)
        save_variables("data.json", data_to_save())
        choose_color_hover_load(theme_colorh)


def choose_color_hover_load(theme_colorh):
    segmented_button.configure(selected_hover_color=theme_colorh)
    widgets = [
        b6,
        b7,
        bs1,
        b65,
        menu_button,
        menu_button1,
        menu_button_p1,
        menu_item1,
        menu_item2,
        menu_item3,
        del_userbutton,
        add_userbutton,
        b2,
        b3,
        b4,
        b5,
        theme1,
        theme15,
        theme16,
        theme2,
    ]
    for widget in widgets:
        widget.configure(hover_color=theme_colorh)


def default_color():
    global theme_color, theme_color16, theme_color2, theme_colorh

    if not any([theme_color, theme_color16, theme_color2, theme_colorh]):
        return
    theme_color = ""
    theme_color16 = ""
    theme_color2 = ""
    theme_colorh = ""

    update_variables(
        {
            "theme_color": theme_color,
            "theme_color16": theme_color16,
            "theme_color2": theme_color2,
            "theme_colorh": theme_colorh,
        }
    )

    save_variables("data.json", data_to_save())
    CTkMessagebox.CTkMessagebox(
        title="Reload Needed!",
        message="Please reload the application to see changes.\n",
        option_1="Ok",
    )


def toggle_menu1():
    apply1()
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()  # Hide the menu frame if it is currently visible
        menu_frame2.pack_forget()
    else:
        menu_frame.place(
            x=0, y=0
        )  # Place the menu frame at the top left corner of the window
        menu_frame.lift()  # Raise the menu frame to the top of the stacking order  # Placing the button at the top left corner of the window
        menu_frame2.pack_forget()


def toggle_menu():
    if menu_frame.winfo_ismapped():
        menu_frame.place_forget()  # Hide the menu frame if it is currently visible
        menu_frame2.pack_forget()
    else:
        menu_frame.place(
            x=0, y=0
        )  # Place the menu frame at the top left corner of the window
        menu_frame.lift()  # Raise the menu frame to the top of the stacking order  # Placing the button at the top left corner of the window
        menu_frame2.pack_forget()


def off_menu():
    menu_frame.place_forget()


def clc_click(event):
    if int(event.x) > 190:
        menu_frame.place_forget()


root.bind("<Button-1>", clc_click)


def changetheme():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        b5.configure(image=imaphoto2)
        root.iconbitmap("emailB.ico")
        link_label.configure(text_color="blue")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        b5.configure(image=imaphoto1)
        root.iconbitmap("emailL.ico")
        link_label.configure(text_color="lightblue")


def open1():
    if frame91.winfo_ismapped():
        frame91.place_forget()  # Hide the menu frame if it is currently visible
        menu_item3.configure(text="About Me")
    if frame9.winfo_ismapped():
        frame9.place_forget()  # Hide the menu frame if it is currently visible
        menu_item2.configure(text="Setting")
        menu_frame.place_forget()
    else:
        frame9.place(x=0, y=0)  # Place the menu frame to cover the entire root frame
        frame9.lift()
        menu_frame.lift()
        menu_item2.configure(text="Home")
        b5.lift()
        menu_frame.place_forget()


def open2():
    if frame9.winfo_ismapped():
        frame9.place_forget()  # Hide the menu frame if it is currently visible
        menu_item2.configure(text="Setting")
    if frame91.winfo_ismapped():
        frame91.place_forget()  # Hide the menu frame if it is currently visible
        menu_item3.configure(text="About Me")
    else:
        frame91.place(x=0, y=0)  # Place the menu frame to cover the entire root frame
        frame91.lift()
        menu_frame.lift()
        menu_item3.configure(text="Home")
        b5.lift()
        menu_frame.place_forget()


def copytempo():
    source_folder = advmail.create_folder()
    destination_folder = advmail.select_folder()
    if not os.path.isdir(destination_folder):
        return
    advmail.copy_files(source_folder, destination_folder)


def ne():
    if menu_frame2.winfo_ismapped():  # Check if menu_frame2 is currently visible
        menu_frame2.pack_forget()  # Hide the menu frame if it is currently visible
    else:
        menu_frame2.pack()  # Show the menu frame
        menu_frame2.lift()  # Bring the menu frame to the front


def getcombo(choice):
    global ref_receiver
    ref_receiver = choice


warnings.simplefilter("ignore", category=DeprecationWarning)

imaphoto1 = ImageTk.PhotoImage(
    Image.open("clicktolight.png").resize((21, 21), Image.ANTIALIAS)
)
imaphoto2 = ImageTk.PhotoImage(
    Image.open("clicktodark.png").resize((21, 21), Image.ANTIALIAS)
)

mode = "light"

# Filter out Deprecation Warning and UserWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

frame9 = customtkinter.CTkFrame(root, width=app_width, height=app_height)
frame91 = customtkinter.CTkFrame(root, width=app_width, height=app_height)
label20 = customtkinter.CTkLabel(frame9, text="Settings", font=("Bahnschrift", 40))
label20.place(x=160, y=3)
menu_button_p1 = customtkinter.CTkButton(
    frame9, font=("bold", 20), text="☰", command=toggle_menu1, width=50, height=10
)
menu_button_p1.place(x=10, y=10)
menu_button_p2 = customtkinter.CTkButton(
    frame91, font=("bold", 20), text="☰", command=toggle_menu, width=50, height=10
)
menu_button_p2.place(x=10, y=10)

label1 = customtkinter.CTkLabel(
    frame91, text="About the software", font=("Bahnschrift", 40)
)
label1.place(x=160, y=3)


def open_link(event):
    webbrowser.open("https://github.com/Utkarsh-X/EmailFlow")


main_text = (
    "Welcome to my open-source project! I'm excited to introduce a powerful tool designed to simplify your \nemail and file management tasks.\n\n"
    "This application seamlessly integrates core features—sending emails, converting PDFs to high-resolution \nimages (with DPI control), and managing multiple files at once.\n\n"
    "With a simple interface, you can automate the entire process: select recipients, set a subject line \n(optionally using today’s date), and choose whether to convert or attach files.\n\n"
    "The app remembers your preferences, making repeated tasks effortless.\n\n"
    "To enhance your user experience, the application remembers your settings and preferences, streamlining \nfuture interactions and making it easier for you to send emails without having to reconfigure each time.\n\n"
    "Whether you're a professional or a student, this tool adapts to your needs with speed and ease.\n\n"
    "Have suggestions or feedback? Feel free to contribute on"
)

inframe91 = customtkinter.CTkFrame(frame91, width=917, height=550, border_width=3)
inframe91.place(x=120, y=90)

# Create a label for the main text
para = customtkinter.CTkLabel(
    inframe91,
    text=main_text,
    wraplength=850,
    font=("Roboto", 17),
    justify="left",
    anchor="w",
)
para.place(x=40, y=30)

link_label = customtkinter.CTkLabel(
    inframe91,
    text="https://github.com/Utkarsh-X/EmailFlow",
    text_color="blue",
    fg_color=None,
    font=("Roboto", 17, "underline"),
)
link_label.place(x=476 + para.winfo_width(), y=346)
dev_label = customtkinter.CTkLabel(
    inframe91, text="Developed by Utkarsh-X", fg_color=None, font=("Roboto", 17)
)
dev_label.place(x=715 + para.winfo_width(), y=498)
link_dot = customtkinter.CTkLabel(
    inframe91, text=".", fg_color=None, font=("Roboto", 17)
)
link_dot.place(x=789 + para.winfo_width(), y=346)
# Bind the click event to open the link
link_label.bind("<Button-1>", open_link)

# Change cursor to pointer when hovering over the link label
link_label.bind("<Enter>", lambda e: link_label.configure(cursor="hand2"))
link_label.bind("<Leave>", lambda e: link_label.configure(cursor=""))

ver_dev_detail = customtkinter.CTkLabel(
    inframe91,
    text=f"                  Version {__version__}",
    fg_color=None,
    font=("Roboto", 17),
)
ver_dev_detail.place(x=716 + para.winfo_width(), y=475)

frame10 = customtkinter.CTkFrame(frame9, width=700, height=400)
frame10.place(x=40, y=90)

frame11 = customtkinter.CTkFrame(frame10)
frame11.pack(pady=(15, 10), padx=20, side="left" and "top")

label20_main = customtkinter.CTkLabel(
    frame11,
    text="Set DPI for generated images:",
    justify="left",
    font=("Bahnschrift", 18),
)
label20_main.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))


label20_sub = customtkinter.CTkLabel(
    frame11, text="Default DPI is set to 300.", justify="left", font=("Bahnschrift", 14)
)
label20_sub.grid(row=1, column=0, sticky="nw", padx=10, pady=(0, 10))

entrybox20 = customtkinter.CTkEntry(
    frame11,
    width=150,
    placeholder_text="Set DPI",
    font=("Bahnschrift", 18),
    corner_radius=5,
    justify="center",
)
entrybox20.grid(row=0, column=1, rowspan=2, padx=(0, 40), pady=(10, 40))

frame11.columnconfigure(0, weight=1)  # Make the first column expandable

frame11.pack(fill="x")  # Make the frame expand horizontally

frame14 = customtkinter.CTkFrame(frame10)
frame14.pack(pady=10, padx=20, side="top")

frame14.columnconfigure(0, weight=1)  # Make the first column expandable

frame14.pack(fill="x")  # Make the frame expand horizontally

frame16 = customtkinter.CTkFrame(frame10)
frame16.pack(pady=(10, 15), padx=20, side="top")

frame16.columnconfigure(0, weight=1)  # Make the first column expandable
frame16.pack(fill="x")


def reset_app_settings():
    global var4dpi, v2, v3, theme_color, theme_color16, theme_color2, theme_colorh, switch_v_pass1, list1, switch_v_date1, switch_v_sub1, switch_v_img1, switch_v_del11, addre1, recname1

    var_load()
    for var in [
        v2,
        v3,
        theme_color,
        theme_color16,
        theme_color2,
        theme_colorh,
        switch_v_pass1,
        switch_v_date1,
        switch_v_img1,
        switch_v_del11,
        list1,
        addre1,
        recname1,
    ]:
        update_variables(var)

    save_variables("data.json", data_to_save())
    combox1.set("")
    combox1.configure(values=[""])
    entrybox2.delete(0, "end")
    fname = "data.json"
    current_directory = os.getcwd()
    fs = os.path.join(current_directory, fname)
    if os.path.exists(fs):
        os.remove(fs)
        print(f"{fname} file cleared at address {fs}")
    else:
        print("Error deleting the file")  # with open(fname,'w') as file:
    #     file.write('{}')
    CTkMessagebox.CTkMessagebox(
        title="System",
        message="The application has been reset successfully.\nPlease restart the application to see the changes.",
        option_1="Ok",
    )


bs1 = customtkinter.CTkButton(
    frame16,
    width=70,
    height=30,
    font=("Bahnschrift", 16),
    text="Reset Application",
    corner_radius=5,
    command=reset_app_settings,
    border_width=2,
)
bs1.pack(padx=(20, 20), pady=(10, 10), anchor="sw")  #  for southeast corner

b5 = customtkinter.CTkButton(
    root,
    width=45,
    height=10,
    image=imaphoto1,
    text="",
    corner_radius=5,
    command=changetheme,
    border_width=2,
)
b5.pack(side="top", padx=(90, 10), pady=(10, 15), anchor="nw")

label2 = customtkinter.CTkLabel(root, text="EmailFlow", font=("Bahnschrift", 40))
label2.place(x=160, y=3)


# Create a button to toggle the menu
menu_button = customtkinter.CTkButton(
    root, font=("bold", 20), text="☰", command=toggle_menu, width=50, height=10
)
menu_button.place(x=10, y=10)

menu_frame = customtkinter.CTkFrame(root)

# Add menu items to the frame
menu_button1 = customtkinter.CTkButton(
    menu_frame, font=("bold", 20), text="☰", command=toggle_menu, width=50, height=30
)
menu_button1.place(x=10, y=10)
menu_button1.pack(side="left" and "top", pady=10, padx=10, anchor="w")

menu_frame2_visible = False  # Variable to track the visibility state of menu_frame2

menu_frame2 = customtkinter.CTkFrame(menu_frame)

menu_item2 = customtkinter.CTkButton(
    menu_frame, font=("Bahnschrift", 18), anchor="w", command=open1, text="Setting"
)
menu_item2.configure(width=150, height=35)
menu_item2.pack(pady=10, padx=(10, 30))

menu_item1 = customtkinter.CTkButton(
    menu_frame, command=ne, anchor="w", font=("Bahnschrift", 18), text="Change Theme"
)
menu_item1.configure(width=150, height=35)
menu_item1.pack(pady=10, padx=(10, 30))

theme1 = customtkinter.CTkButton(
    menu_frame2,
    anchor="w",
    font=("Bahnschrift", 16),
    text="Primary Color  ",
    command=choose_color_button,
    corner_radius=10,
    fg_color="black",
)
theme1.configure(width=150, height=35)
theme1.pack(pady=10, padx=(10, 30))

theme16 = customtkinter.CTkButton(
    menu_frame2,
    anchor="w",
    font=("Bahnschrift", 16),
    text="Secondary Color",
    command=choose_color_button16,
    corner_radius=10,
    fg_color="black",
)
theme16.configure(width=150, height=35)
theme16.pack(pady=10, padx=(10, 30))

theme15 = customtkinter.CTkButton(
    menu_frame2,
    anchor="w",
    font=("Bahnschrift", 16),
    text="Menu Color",
    command=choose_color_menu15,
    corner_radius=10,
    fg_color="black",
)
theme15.configure(width=150, height=35)
theme15.pack(pady=10, padx=(10, 30))

theme2 = customtkinter.CTkButton(
    menu_frame2,
    anchor="w",
    font=("Bahnschrift", 16),
    text="Hover Color",
    command=choose_color_hover,
    corner_radius=10,
    fg_color="black",
)
theme2.configure(width=150, height=35)
theme2.pack(pady=10, padx=(10, 30))

themedefault = customtkinter.CTkButton(
    menu_frame2,
    anchor="w",
    font=("Bahnschrift", 16),
    text="Default Color",
    command=default_color,
    corner_radius=10,
    fg_color="black",
)
themedefault.configure(width=150, height=35)
themedefault.pack(pady=10, padx=(10, 30))

menu_item3 = customtkinter.CTkButton(
    menu_frame, anchor="w", font=("Bahnschrift", 18), text="About Me", command=open2
)
menu_item3.configure(width=150, height=35)
menu_item3.pack(side="bottom", pady=(10, 1000), padx=(10, 30))

frame = customtkinter.CTkFrame(root)
frame.pack(side="top", anchor="nw", padx=20, pady=20)

label3 = customtkinter.CTkLabel(
    frame, text="Select The Email Reciever:", font=("Bahnschrift", 24)
)
label3.pack(pady=0, padx=10, anchor="w")

combox1 = customtkinter.CTkComboBox(
    frame,
    values=list1,
    height=25,
    width=363,
    font=("Bahnschrift", 20),
    dropdown_font=("Bahnschrift", 20),
    justify="center",
    command=getcombo,
    dropdown_hover_color="black",
)
combox1.pack(side="left", padx=10)


def input():
    dialog = customtkinter.CTkInputDialog(text="Enter the Email Below")
    val22 = dialog.get_input()
    global list1
    if val22 != "":
        list1 = list1 + [val22]
        update_variables(list1)
        save_variables("data.json", data_to_save())
        combox1.configure(values=list1)


def add_user():
    input()


def del_user():
    global list1
    list2 = []
    selected_value = combox1.get()
    print(selected_value)
    if selected_value != "":
        list2 = [x for x in list1 if x != selected_value]
        list1 = list2
        update_variables(list1)
        save_variables("data.json", data_to_save())
        combox1.configure(values=list1)
        combox1.set(list1[0])


del_userbutton = customtkinter.CTkButton(
    frame,
    text="Delete User",
    command=del_user,
    height=20,
    width=35,
    font=("Bahnschrift", 22),
    text_color="black",
    state="normal",
)
del_userbutton.pack(side="right", padx=(5, 30), pady=10, anchor="e")

add_userbutton = customtkinter.CTkButton(
    frame,
    text="Add User",
    command=add_user,
    height=20,
    width=35,
    font=("Bahnschrift", 22),
    text_color="black",
    state="normal",
)
add_userbutton.pack(side="right", padx=(20, 30), pady=10)

frame4 = customtkinter.CTkFrame(root)
frame4.pack(side="top", anchor="nw", padx=20, pady=10)
frame_b2 = customtkinter.CTkFrame(frame4)
frame_b2.pack(side="left", padx=10)


def input2():
    global v2
    dialog2 = customtkinter.CTkInputDialog(text="Enter the Password Below")
    v2 = dialog2.get_input()
    update_variables(v2)
    save_variables("data.json", data_to_save())
    # Update the text of the b2

    ads = "*" * len(v2)
    if v2 != "":
        if switch_v_pass.get() == "on":
            label_below_b2.configure(text=ads)
        else:
            label_below_b2.configure(text=v2)


if "v2" not in globals():
    v2 = "Click Above to Enter Password"

b2 = customtkinter.CTkButton(
    frame_b2,
    text="Enter your Password",
    height=20,
    width=20,
    corner_radius=5,
    command=input2,
    font=("Bahnschrift", 18),
    text_color="black",
    state="normal",
    fg_color="#b3e0dc",
)
b2.pack(side="top", padx=10)

label_below_b2 = customtkinter.CTkLabel(frame_b2, text=v2, font=("Bahnschrift", 14))
label_below_b2.pack(side="top", padx=10)


def input3():
    global v3
    dialog3 = customtkinter.CTkInputDialog(text="Enter Sender/Your Email Below")
    v3 = dialog3.get_input()
    update_variables(v3)
    save_variables("data.json", data_to_save())
    # Update the text of the b3
    if v3 != "":
        if len(v3) <= 24:
            label_below_b3.configure(text=v3)
        else:
            v3 = v3[:24]
            label_below_b3.configure(text=v3)


# Add a Label in the additional options frame
if "v3" not in globals():
    v3 = "Click Above to Enter Email"

# Add a Blank Button in the additional options frame
frame_b3 = customtkinter.CTkFrame(frame4)
frame_b3.pack(side="left", padx=10)
frame_b3.configure(width=200, height=100)

b3 = customtkinter.CTkButton(
    frame_b3,
    text="Enter Sender Email",
    height=20,
    width=20,
    corner_radius=5,
    command=input3,
    font=("Bahnschrift", 18),
    text_color="black",
    state="normal",
    fg_color="#b3e0dc",
)
b3.pack(side="top", padx=10)

label_below_b3 = customtkinter.CTkLabel(frame_b3, text=v3, font=("Bahnschrift", 14))
label_below_b3.pack(side="top", padx=10)

switch_v_pass = customtkinter.StringVar(value="off")


def passshow():
    global switch_v_pass1
    ads = "*" * len(v2)
    if switch_v_pass.get() == "on":
        switch_v_pass1 = "on"
        label_below_b2.configure(text=ads)
    else:
        switch_v_pass1 = "off"
        label_below_b2.configure(text=v2)
    update_variables(switch_v_pass1)
    save_variables("data.json", data_to_save())


label22_main = customtkinter.CTkLabel(
    frame14,
    text="Always hide password on screen",
    justify="left",
    font=("Bahnschrift", 18),
)
label22_main.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

label22_sub = customtkinter.CTkLabel(
    frame14,
    text="Want to hide the password from view? We’ve got you!",
    justify="left",
    font=("Bahnschrift", 14),
)

label22_sub.grid(row=1, column=0, sticky="nw", padx=10, pady=(0, 10))

switch6 = customtkinter.CTkSwitch(
    frame14,
    text="",
    command=passshow,
    switch_width=50,
    switch_height=25,
    variable=switch_v_pass,
    onvalue="on",
    offvalue="off",
    font=("Bahnschrift", 18),
    state="normal",
)
switch6.grid(row=0, column=1, rowspan=2, padx=(0, 40), pady=(10, 40))


def sub1():
    global flag_sub1, switch_v_sub1
    flag_sub1 = switch_v_sub.get()
    if switch_v_sub.get() == "off":
        frame5.place_forget()
        switch_v_sub1 = "off"
    else:
        frame5.place(x=470, y=295)
        switch_v_sub1 = "on"
    update_variables(switch_v_sub1)
    save_variables("data.json", data_to_save())


def datew():
    global switch_v_date1, today_datew
    if switch_v_date.get() == "on":
        today_datew = date.today().strftime("%d-%b-%Y")
        switch_v_date1 = "on"
        entrybox1.delete(0, tk.END)  # Clear existing text
        entrybox1.insert(0, today_datew)  # Insert current date
    else:
        switch_v_date1 = "off"
        entrybox1.delete(0, tk.END)  # Clear the text in EntryBox1
    update_variables(switch_v_date1)
    save_variables("data.json", data_to_save())


switch_v_sub = customtkinter.StringVar(value="on")
switch_v_img = customtkinter.StringVar(value="on")

switch1 = customtkinter.CTkSwitch(
    frame4,
    text="Add Subject        ",
    command=sub1,
    variable=switch_v_sub,
    onvalue="on",
    offvalue="off",
    font=("Bahnschrift", 18),
    state="normal",
)
switch1.pack(side="top", padx=(25, 57), pady=10)


def toggle_switch():
    global switch_v_img1
    if switch_v_img.get() == "off":
        switch_v_img1 = "off"
    else:
        switch_v_img1 = "on"
    update_variables(switch_v_img1)
    save_variables("data.json", data_to_save())


switch2 = customtkinter.CTkSwitch(
    frame4,
    text="Convert to Image",
    command=toggle_switch,
    variable=switch_v_img,
    onvalue="on",
    offvalue="off",
    font=("Bahnschrift", 18),
    state="normal",
)
switch2.pack(side="top", padx=(25, 57), pady=10)

frame5 = customtkinter.CTkFrame(root)
frame5.place(x=470, y=291)

frame6 = customtkinter.CTkFrame(root)
frame6.place(x=20, y=290)

frame8 = customtkinter.CTkFrame(root)
frame8.place(x=20, y=390)

frame15 = customtkinter.CTkFrame(root)
frame15.place(x=20, y=450)

label4 = customtkinter.CTkLabel(
    frame5, text="Enter Email Subject", font=("Bahnschrift", 18)
)
label4.pack(pady=(5, 10), padx=(0, 10))

entrybox1 = customtkinter.CTkEntry(
    frame5, width=200, font=("Bahnschrift", 18), corner_radius=35, justify="center"
)
entrybox1.pack(anchor="center")
today_datew = date.today().strftime("%d-%b-%Y")
entrybox1.insert(0, today_datew)

switch_v_date = customtkinter.StringVar(value="on")
switch3 = customtkinter.CTkSwitch(
    frame5,
    text=" or put Subject as Date",
    command=datew,
    variable=switch_v_date,
    onvalue="on",
    offvalue="off",
    font=("Bahnschrift", 18),
    state="normal",
)
switch3.pack(side="top", padx=10, pady=10)

p2 = "Set Address"


def segmented_button_logic(value):
    global p2
    p2 = segmented_button.get()
    print(f"\033[35m{segmented_button.get()}\033[0m")
    if p2 == "Browse Files":
        label5.pack_forget()
        b7.pack_forget()
        entrybox2.pack_forget()
        b4.pack(side="left", padx=10, pady=15)
        # browse_files()
    else:
        label5.pack(pady=(10, 5))
        b7.pack(anchor="e", side="left", padx=(50, 10), pady=10)
        entrybox2.pack(anchor="center", padx=(20, 25), pady=(0, 10))
        b4.pack_forget()


value1 = ["Browse Files", "Set Address"]
segmented_button = customtkinter.CTkSegmentedButton(
    frame15, command=segmented_button_logic, values=value1, font=("Helvetica", 18)
)
segmented_button.pack(padx=10, pady=5)
segmented_button.set("Set Address")


def clear_selection():
    if len(fradsc1.winfo_children()) > 0:
        for child in fradsc1.winfo_children():
            child.destroy()


file_paths = []  # List to store the addresses of selected files.
file_names = []  # List to store the names of selected files.


def browse_files():
    global file_paths, count  # Use the global file_paths list

    file_paths.clear()
    file_names.clear()
    selected_files = filedialog.askopenfilenames()
    if selected_files:
        count = 0
        for file in selected_files:
            count += 1
            file_paths.append(
                file
            )  # Add the selected file paths to the file_paths list
        # print("Selected files:", file_paths)  # Print the list of selected file paths
        print(count)

        for idx, file_path in enumerate(file_paths):
            file_name = file_path.split("/")[-1]  # Extract the file name from the path
            vmjr = f"{idx+1}. {file_name}"
            file_names.append(vmjr)
        print(file_names)
        for pa in file_paths:
            print(f"\033[34m{pa}\033[0m")

        if len(fradsc1.winfo_children()) > 0:
            print(len(fradsc1.winfo_children()))
            for child in fradsc1.winfo_children():
                child.destroy()

                # print labels
        for xw in range(len(file_names)):
            if len(file_names[xw]) >= 45:
                # Create a new variable for the filtered list
                filtered_names = [s for s in file_names[xw] if len(s) <= 45]
                for name in filtered_names:
                    customtkinter.CTkLabel(
                        fradsc1, text=name, font=("Helvetica", 14), justify="left"
                    ).pack(padx=(2, 2), pady=5)
            else:
                customtkinter.CTkLabel(
                    fradsc1, text=file_names[xw], font=("Helvetica", 14), justify="left"
                ).pack(padx=(2, 2), pady=5)


file_addresses = []  # List to store the addresses of selected files.
file_namess = []  # List to store the names of selected files.


def load_folder_files():
    file_addresses.clear()
    file_namess.clear()

    if entrybox2.get() == "":
        return
    else:
        if os.path.isdir(entrybox2.get()):
            print(f"The directory '{entrybox2.get()}' exists.")
            files = os.listdir(entrybox2.get())
            if files:
                for file in files:
                    file_path = os.path.join(entrybox2.get(), file)
                    if os.path.isfile(file_path):
                        file_addresses.append(file_path)
            else:
                print("The directory is empty.")
                CTkMessagebox.CTkMessagebox(
                    title="Error",
                    message="The directory is empty !, Please check again.",
                    option_1="Ok",
                )
                return
        else:
            print(f"The directory '{entrybox2.get()}' does not exist.")
            CTkMessagebox.CTkMessagebox(
                title="Error", message="Wrong address provide !", option_1="Ok"
            )
            return

        print("Addresses of all the files in the given directory:")
        for address in file_addresses:
            print(f"\033[34m{address}\033[0m")
        print(len(file_addresses))

        for idxx, idm in enumerate(file_addresses):
            file_namezz = os.path.basename(idm)  # Extract the file name from the path
            formatted_name = f"{idxx+1}. {file_namezz}"
            file_namess.append(formatted_name)

        # print(file_namess)


def showlist():
    if entrybox2.get() == "":
        CTkMessagebox.CTkMessagebox(
            title="Error", message="No Address Provided,provide one!,", option_1="Ok"
        )
        return False
    else:
        load_folder_files()
        if len(fradsc1.winfo_children()) > 0:
            for child in fradsc1.winfo_children():
                child.destroy()
            # print labels
        for xwz in range(len(file_namess)):
            customtkinter.CTkLabel(
                fradsc1, text=file_namess[xwz], font=("Helvetica", 14), justify="left"
            ).pack(padx=(2, 2), pady=5)


def send():
    def sendthread():
        b6.configure(state="disabled")
        buffer_folder = advmail.create_folder()

        if not advmail.check_internet_connection():
            tmy = CTkMessagebox.CTkMessagebox(
                title="Warning Message!",
                message="Unable to connect!",
                icon="warning",
                option_1="Cancel",
                option_2="Retry",
            )
            if tmy.get() == "Retry":
                advmail.check_internet_connection()
            elif tmy.get() == "Cancel":
                return

        apply1()
        selected_value = combox1.get()
        if selected_value != "" and "@" in selected_value:
            receiver_email = selected_value
        else:
            CTkMessagebox.CTkMessagebox(
                title="Error!",
                message="No receiver email selected\nor not a valid email!",
                option_1="Ok",
            )
            b6.configure(state="normal", border_width=3)
            return
        # S_EMAIL
        sender_email = v3

        # PASSWORD
        password = v2
        if not advmail.check_credentials(sender_email, password):
            b6.configure(state="normal", border_width=3)
            return

        # SUBJECT
        if switch_v_sub.get() == "on":
            subject_main = entrybox1.get()
        else:
            subject_main = ""
        dpi1 = var4dpi
        p3 = segmented_button.get()

        if p3 == "Set Address":
            showlist()
            if len(file_addresses) != 0:
                if switch_v_img.get() == "on":
                    try:
                        advmail.delete_filesindir(buffer_folder)
                        advmail.convert_all_pdfs(file_addresses, buffer_folder, dpi1)
                    except Exception as e:
                        print(
                            f"Provided file is not a Pdf so can't convert.\nError: {e}"
                        )
                        b6.configure(state="normal", border_width=3)
                        return
                    file_list = advmail.list1_files(buffer_folder)
                    advmail.sendingprotocol(
                        sender_email, receiver_email, password, file_list, subject_main
                    )
                    advmail.delete_filesindir(buffer_folder)

                    if switch_v_del1.get() == "on":
                        advmail.delete_files(file_addresses)
                        file_addresses.clear()
                    val1 = advmail.files_uploaded
                    clear_selection()
                    file_addresses.clear()
                    file_namess.clear()
                    CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message=f"Uploaded successfully!\nNumber of files uploaded: {val1}",
                        icon="check",
                        option_1="OK",
                    )
                else:
                    file_list = file_addresses
                    advmail.sendingprotocol(
                        sender_email, receiver_email, password, file_list, subject_main
                    )
                    if switch_v_del1.get() == "on":
                        advmail.delete_files(file_addresses)
                        file_addresses.clear()
                    val1 = advmail.files_uploaded
                    clear_selection()
                    file_addresses.clear()
                    file_namess.clear()
                    CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message=f"Uploaded successfully!\nNumber of files uploaded: {val1}",
                        icon="check",
                        option_1="OK",
                    )

            else:
                CTkMessagebox.CTkMessagebox(
                    title="Error",
                    message="No File selected, Please Select File",
                    option_1="Ok",
                )
                b6.configure(state="normal", border_width=3)
                return

        elif p3 == "Browse Files":
            if len(file_paths) != 0:
                if switch_v_img.get() == "on":
                    try:
                        advmail.delete_filesindir(buffer_folder)
                        advmail.convert_all_pdfs(file_paths, buffer_folder, dpi1)
                    except Exception as e:
                        print(
                            f"Provided file is not a Pdf so can't convert.\nError: {e}"
                        )
                        b6.configure(state="normal", border_width=3)
                        return
                    file_list = advmail.list1_files(buffer_folder)
                    advmail.sendingprotocol(
                        sender_email, receiver_email, password, file_list, subject_main
                    )
                    advmail.delete_filesindir(buffer_folder)
                    if switch_v_del1.get() == "on":
                        advmail.delete_files(file_paths)
                        file_paths.clear()
                    val1 = advmail.files_uploaded
                    clear_selection()
                    file_addresses.clear()
                    file_namess.clear()
                    CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message=f"Uploaded successfully!\nNumber of files uploaded: {val1}",
                        icon="check",
                        option_1="OK",
                    )
                else:
                    file_list = file_paths
                    advmail.sendingprotocol(
                        sender_email, receiver_email, password, file_list, subject_main
                    )
                    if switch_v_del1.get() == "on":
                        advmail.delete_files(file_paths)
                        file_paths.clear()
                    val1 = advmail.files_uploaded
                    clear_selection()
                    file_addresses.clear()
                    file_namess.clear()
                    CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message=f"Uploaded successfully!\nNumber of files uploaded: {val1}",
                        icon="check",
                        option_1="OK",
                    )

            else:
                CTkMessagebox.CTkMessagebox(
                    title="Error",
                    message="No File selected, Please Select File",
                    option_1="Ok",
                )
                b6.configure(state="normal", border_width=3)
                return
        b6.configure(state="normal", border_width=3)

    threading.Thread(target=sendthread).start()


def saveimg():
    apply1()
    dpi1 = var4dpi

    if switch_v_img.get() == "off":
        CTkMessagebox.CTkMessagebox(
            title="Not Applicable",
            message="First turn on the (Convert to image option)",
            option_1="Ok",
        )
        return
    else:
        if p2 == "Set Address":
            showlist()
            if len(file_addresses) != 0:
                destinationfol = filedialog.askdirectory()
                try:
                    advmail.convert_all_pdfs(file_addresses, destinationfol, dpi1)
                    msg = CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message="Successfully Converted",
                        icon="check",
                        option_1="Open Folder",
                        option_2="OK",
                    )
                    response = msg.get()
                    if response == "Open Folder":
                        advmail.openfol(destinationfol)

                except Exception as e:
                    CTkMessagebox.CTkMessagebox(
                        title="Crash Error",
                        message=f"Error occured\n {e}",
                        option_1="Ok",
                    )
                    return
            else:
                CTkMessagebox.CTkMessagebox(
                    title="File not found!",
                    message="The selected file is not present at the provided location unfortunately\nPlease try Again to select the files",
                    option_1="Ok",
                )
                return
        elif p2 == "Browse Files":
            if len(file_paths) != 0:
                destinationfol = filedialog.askdirectory()
                try:
                    advmail.convert_all_pdfs(file_paths, destinationfol, dpi1)
                    msg = CTkMessagebox.CTkMessagebox(
                        title="Done",
                        message="Successfully Converted",
                        icon="check",
                        option_1="Open Folder",
                        option_2="OK",
                    )
                    response = msg.get()
                    if response == "Open Folder":
                        advmail.openfol(destinationfol)
                except Exception as e:
                    CTkMessagebox.CTkMessagebox(
                        title="Crash Error",
                        message=f"Error occured\n {e}",
                        option_1="Ok",
                    )
                    return
            else:
                CTkMessagebox.CTkMessagebox(
                    title="File not found!",
                    message="The selected file is not present at the provided location unfortunately\nPlease try Again to select the files",
                    option_1="Ok",
                )
                return


fradsc = customtkinter.CTkFrame(root)
fradsc.place(x=740, y=76)

labelff = customtkinter.CTkLabel(
    fradsc, text="Files Showcase ", font=("Bahnschrift", 24)
)
labelff.pack(anchor="w", padx=(20, 10), pady=(0, 5))
fradsc1 = customtkinter.CTkScrollableFrame(fradsc, height=532, width=350)
fradsc1.pack(pady=(1, 5))
fradsc1.pack(fill="x", expand=True)  # Fill and expand the main frame

b4 = customtkinter.CTkButton(
    frame6,
    text="Browse Files",
    height=20,
    width=20,
    corner_radius=5,
    command=browse_files,
    font=("Bahnschrift", 18),
    text_color="black",
    state="normal",
    fg_color="#b3e0dc",
)

label5 = customtkinter.CTkLabel(
    frame6, text="Enter Folder Path Below", font=("Bahnschrift", 18)
)
label5.pack(pady=(10, 10))

entrybox2 = customtkinter.CTkEntry(
    frame6, width=395, font=("Bahnschrift", 18), corner_radius=35, justify="center"
)
entrybox2.pack(anchor="center", padx=(20, 25), pady=(0, 10))
# Set the fixed value "abc" in the entry box NOTE: TO DELETE BELOW WHEN PUBLISING FOR FURTHER USE

frame7 = customtkinter.CTkFrame(root, width=200)
frame7.place(x=20, y=590)

b6 = customtkinter.CTkButton(
    frame7,
    text="SEND EMAIL",
    height=50,
    command=send,
    width=80,
    corner_radius=5,
    font=("Bahnschrift", 30),
    text_color="black",
    state="normal",
    border_width=3,
)
b6.pack(padx=10, pady=10, side="left")
b65 = customtkinter.CTkButton(
    frame7,
    text="SAVE IMAGE",
    command=saveimg,
    height=50,
    width=70,
    corner_radius=5,
    font=("Bahnschrift", 30),
    text_color="black",
    state="normal",
    border_width=3,
)
b65.pack(side="left", padx=(50, 10), pady=5)
b7 = customtkinter.CTkButton(
    frame7,
    text="SHOW FILES",
    height=50,
    width=80,
    corner_radius=5,
    command=showlist,
    font=("Bahnschrift", 30),
    text_color="black",
    state="normal",
    border_width=3,
)
b7.pack(anchor="e", side="left", padx=(50, 10), pady=10)


def dele1():
    global switch_v_del11
    if switch_v_del1.get() == "off":
        switch_v_del11 = "off"
    else:
        switch_v_del11 = "on"
    update_variables(switch_v_del11)
    save_variables("data.json", data_to_save())


switch_v_del1 = customtkinter.StringVar(value="on")
switch4 = customtkinter.CTkSwitch(
    frame8,
    text="Delete files after email is sent successfully",
    command=dele1,
    variable=switch_v_del1,
    onvalue="on",
    offvalue="off",
    font=("Bahnschrift", 18),
    state="normal",
)
switch4.pack(side="top", padx=(24, 23), pady=10)


if switch_v_del11 == "off":
    switch4.deselect()
    dele1()

if addre1 != "":
    entrybox2.insert(0, f"{addre1}")

if recname1 != "":
    combox1.set(f"{recname1}")

if switch_v_img1 == "off":
    switch2.deselect()
    toggle_switch()

if switch_v_sub1 == "off":
    switch1.deselect()
    sub1()

if switch_v_date1 == "off":
    switch3.deselect()
    datew()

if switch_v_pass1 == "on":
    switch6.select()
    passshow()
if var4dpi != 0:
    entrybox20.insert(0, f"{var4dpi}")

if theme_color != "":
    choose_color_button_load(theme_color)

if theme_color16 != "":
    choose_color_button16_load(theme_color16)

if theme_color2 != "":
    choose_color_menu15_load(theme_color2)

if theme_colorh != "":
    choose_color_hover_load(theme_colorh)


def on_closing():
    global addre1, recname1
    if entrybox2.get() != "":
        addre1 = entrybox2.get()
        update_variables(addre1)
        save_variables("data.json", data_to_save())
    if combox1.get() != "":
        recname1 = combox1.get()
        print(recname1)
    update_variables(recname1)
    save_variables("data.json", data_to_save())
    root.destroy()


# Bind the close event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
