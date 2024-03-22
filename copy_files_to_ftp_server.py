import ftplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from env import HOSTNAME, USERNAME, PASSWORD

def CreateWidgets():
    # Label for source file selection
    link_Label = Label(root, text="Select The File To Copy:", bg="#E8D579")
    link_Label.grid(row=1, column=0, pady=5, padx=5)

    # Entry widget for source file path
    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    # Browse button for source file selection
    source_browseButton = Button(root, text="Browse", command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3, pady=5, padx=5)

    
    # Button to copy the file
    copyButton = Button(root, text="Copy File", command=CopyFile, width=15)
    copyButton.grid(row=3, column=1, pady=5, padx=5)    

    # Button to clear selection
    clearButton = Button(root, text="Clear Selection", command=ClearSelection, width=15)
    clearButton.grid(row=3, column=2, pady=5, padx=5)

def SourceBrowse():
    # Function to browse and select the source file
    # Below initial path is as per Windows 10 system    
    root.files_list = list(filedialog.askopenfilenames(initialdir="C:\\Users\\Student\\Desktop\\"))
    root.sourceText.insert('1', root.files_list)

def ClearSelection():
    # Function to clear the selected file text shown in entry wigdet
    root.sourceText.delete(0, 'end')

def CopyFile():
    # Fill Required Information
    """
    HOSTNAME = HOSTNAME    
    USERNAME = USERNAME
    PASSWORD = PASSWORD
    """    
    # Connect FTP Server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

    # force UTF-8 encoding
    ftp_server.encoding = "utf-8"

    # Read the file path from entry widget    
    file = root.sourceText.get()

    # Strip out the {} from the file path text
    file = file.strip('{}')

    # Split file path to get actual file name
    file_name = file.split('/')

    # Last item in the list is the file name selected 
    file_name = file_name[-1]

    # Preapre file to copy 
    file_to_send = open(file,"rb")

    # Copy file to FTP server
    ftp_server.storbinary(f'STOR {file_name}', file_to_send)
    
    # Close the open file
    file_to_send.close()      
    
    # Close FTP server connection
    ftp_server.quit()

    # Call ClearSelection function to clear Entry widget text
    ClearSelection()

    # Show file copy success message
    messagebox.showinfo("Success", "File copied successfully!")
    
# Create the main window
root = tk.Tk()
root.title("Copy Files to FTP Server")

# Variables to store file paths
sourceLocation = StringVar()
destinationLocation = StringVar()

# Create widgets
CreateWidgets()

# Run the GUI event loop
root.mainloop()
