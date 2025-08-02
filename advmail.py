"""
EmailFlow - Advanced Email & File Processing
--------------------------------------------
This file contains the backend logic used by the GUI.
It handles:
- Sending emails with attachments via SMTP
- Converting PDF files to high-resolution images
- File and folder management
- Internet and credentials checks
- Background threading and cleanup utilities

Used internally by GUImain_app.py to power file processing and email features.\n
For more detail visit https://github.com/Utkarsh-X/EmailFlow
"""

# === Standard Library ===
import os
import shutil
import subprocess
import threading
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# === Third-party Libraries ===
from tqdm import tqdm
import requests
from send2trash import send2trash
from pdf2image import convert_from_path

# === Tkinter & GUI Libraries ===
import tkinter as tk
from tkinter import colorchooser, filedialog
import customtkinter
import CTkMessagebox


def list1_files(directory):
    q = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
    return q


# To delete files, Takes the folder path variable and delete all the files in it.
def delete_filesindir(folder_path):
    try:
        # Get the list of files in the directory
        files = os.listdir(folder_path)

        # Check if the directory is empty
        if not files:
            # print("Buffer is empty already")
            return

        count = 0  # Initialize count to keep track of deleted files

        for filename in files:
            file_path = os.path.join(folder_path, filename)
            # Check if it's a file and move it to trash
            if os.path.isfile(file_path):
                send2trash(file_path)
                count += 1
                # print(f"\033[2mMoved to trash: {file_path}\033[0m")
            else:
                print(f"Skipped (not a file): {file_path}")

        print("\n")
        print(f"\033[35mBuffer Cleared. Total files moved to trash: {count}\033[0m")

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_files(file_list):
    total_deleted = 0
    for file_path in file_list:
        # Normalize and clean up the file path
        file_path = os.path.normpath(file_path.strip())

        try:
            if os.path.exists(file_path):
                send2trash(file_path)
                total_deleted += 1
                # Uncomment below if you want to see each deletion
                # print(f"\033[2mDeleted: {file_path}\033[0m")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

    print(f"\033[35m{total_deleted} Original Files deleted.\033[0m")


def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def networkcheck():
    if not check_internet_connection():
        tmy = CTkMessagebox.CTkMessagebox(
            title="Warning Message!",
            message="Unable to connect!",
            icon="warning",
            option_1="Cancel",
            option_2="Retry",
        )

        if tmy.get() == "Retry":
            networkcheck()
        elif tmy.get() == "Cancel":
            pass
            return


def convert_all_pdfs(file_list, output_folder, dpi1):
    # def threadconvert():
    total_files = len(file_list)

    with tqdm(total=total_files, desc="Converting PDFs", colour="yellow") as pbar:
        for i, pdf_path in enumerate(file_list):
            pdf_file = os.path.basename(pdf_path)
            images = convert_from_path(pdf_path, dpi=dpi1)
            for j, img in enumerate(images):
                new_file_name = f"{pdf_file[:-4]}_{j+1}.jpg"
                img.save(os.path.join(output_folder, new_file_name), "JPEG")

            pbar.update(1)
        pbar.set_postfix(color="green")
    print("\033[92mConverted successfully\033[0m")
    # threading.Thread(target=threadconvert).start()


# {SMTP Setup Starts..
def send_email(sender_email, receiver_email, password, file_list, subject_main):
    print("\033[92mIntialising Upload Stream\033[0m")
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject_main

    for file_path in file_list:
        filename = os.path.basename(file_path)
        attachment = open(file_path, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("\033[92mUploaded successfully!\033[0m")


def sendingprotocol(sender_email, receiver_email, password, file_list, subject_main):
    try:
        send_email(sender_email, receiver_email, password, file_list, subject_main)
        print("Email sent successfully!")
        global files_uploaded
        files_uploaded = len([filename for filename in file_list])
        print(f"Number of files uploaded: {files_uploaded}")
    except Exception as e:
        print(f"Email sending failed. Error: {e}")
        CTkMessagebox.CTkMessagebox(
            title="Error in sending mail",
            message=(f"Email Sending Failed{e}"),
            option_1="Ok",
        )


# SMTP Setup Ended.}

# Global variable to hold the folder location
temp_image_folderloc = None
folder_creation_event = threading.Event()


def create_folder():
    global temp_image_folderloc

    def threadfolder():
        global temp_image_folderloc
        folder_name = "Temp_image"

        if not os.path.exists(folder_name):
            print("os path exists true check")
            # Create a new directory
            os.mkdir(folder_name)
            print("Folder created:", folder_name)
            temp_image_folderloc = os.path.abspath(folder_name)
        else:
            print("1 check done")
            temp_image_folderloc = os.path.abspath(folder_name)

        delete_filesindir(temp_image_folderloc)
        folder_creation_event.set()  # Signal that the folder creation is done

    # Start the thread
    threading.Thread(target=threadfolder).start()

    # Wait for the thread to finish and get the folder location
    folder_creation_event.wait()  # Block until the thread signals it's done
    return temp_image_folderloc


def copy_files(source_folder, destination_folder):
    try:
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Get a list of all files in the source folder
        files = os.listdir(source_folder)

        # Copy each file from the source folder to the destination folder
        for file in files:
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy2(source_file, destination_file)

    except Exception as e:
        print(f"An error occurred: {e}")


def select_folder():
    folder_pazes = filedialog.askdirectory()
    if folder_pazes:
        print("Selected folder:", folder_pazes)
        return folder_pazes
    else:
        print("No folder selected")


def check_credentials(sender_email, password):
    if password == "" or sender_email == "":
        CTkMessagebox.CTkMessagebox(
            title="Enter Credentials",
            message="Enter Credential email and password!",
            option_1="Ok",
        )
        return False
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.quit()
        print("\033[32mCredentials are correct.\033[0m")
        return True
    except Exception as e:
        print(f"Invalid credentials. Error: {e}")
        CTkMessagebox.CTkMessagebox(
            title="Error",
            message=f"Incorrect email or password\nEmail: {sender_email}\nPassword: {password}",
            option_1="Ok",
        )
        return False


def openfol(directory_path):
    directory_path = directory_path.replace("\\", "\\\\")
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        subprocess.Popen(f'explorer "{directory_path}"')
    else:
        print("The specified path does not exist or is not a directory.")
