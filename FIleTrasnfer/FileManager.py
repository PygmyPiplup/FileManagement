import os
import tkinter as tk

global place

school_extensions = {".jpg": "C:/Users/016407037/Sorted/JPG", ".exe": "C:/Users/016407037/Sorted/EXE",
                     ".png": "C:/Users/016407037/Sorted/PNG", ".jpeg": "C:/Users/016407037/Sorted/JPEG",
                     ".pdf": "C:/Users/016407037/Sorted/PDF", ".ppsx": "C:/Users/016407037/Sorted/PPSX",
                     ".txt": "C:/Users/016407037/Sorted/TXT", ".wvm": "C:/Users/016407037/Sorted/WVM",
                     ".zip": "C:/Users/016407037/Sorted/ZIP", ".gif": "C:/Users/016407037/Sorted/GIF",
                     ".jfif": "C:/Users/016407037/Sorted/JFIF", ".py": "C:/Users/016407037/Sorted/PY",
                     ".psd": "C:/Users/016407037/Sorted/PSD", ".raw": "C:/Users/016407037/Sorted/RAW",
                     ".tiff": "C:/Users/016407037/Sorted/TIFF", ".mp3": "C:/Users/016407037/Sorted/MP3",
                     ".docx": "C:/Users/016407037/Sorted/DOCX", "msi": "C:/Users/016407037/Sorted/MSI"}

# def main_location():
#   file = []
#  holder = 0
# f = open("fileLocation.txt", "w+")
# contents = f.read()
# file.append(contents)
# print(file)
# f file[0] == '':
#   while holder == 0:
#      location = input(f"So you want to set {file[0]} as the directory?")
#     if location.lower() == "yes":
#        f.write(file_location)
#
#               holder = 1
#          else:
#             file_location = input("What is the file location you would like?")
#
#   f.close()
#  return contents


home_extensions = {".jpg": "C:/sorted/JPG", ".exe": "C:/Sorted/EXE",
                   ".png": "C:/Sorted/PNG", ".jpeg": "C:/Sorted/JPEG",
                   ".pdf": "C:/Sorted/PDF", ".ppsx": "C:/Sorted/PPSX",
                   ".txt": "C:/Sorted/TXT", ".wvm": "C:/Sorted/WVM",
                   ".zip": "C:/Sorted/ZIP", ".gif": "C:/Sorted/GIF",
                   ".jfif": "C:/Sorted/JFIF", ".py": "C:/Sorted/PY",
                   ".psd": "C:/Sorted/PSD", ".raw": "C:/Sorted/RAW",
                   ".tiff": "C:/Sorted/TIFF", ".mp3": "C:/Sorted/MP3",
                   ".docx": "C:/Sorted/DOCX", ".msi": "C:/Sorted/MSI",
                   ".ico": "C:/Sorted/ICO", ".xlsx": "C:/Sorted/XLSX",
                   ".stl": "C:/Sorted/STL", ".sql": "C:/Sorted/SQL"}


def starting_location(place):
    if place == "home":
        starting_file = "C:/Users/patri/downloads"
    else:
        starting_file = "C:/Users/016407037/downloads"
    print(f"Your starting location is {starting_file}")
    return starting_file


def ending_location(key, place):
    if place == "home":
        ending_file = home_extensions.get(key)
    else:
        ending_file = school_extensions.get(key)
    print(f"Your ending location is {ending_file}")
    return ending_file


def printing_directory(ending):
    global place
    holder = 0
    try:
        print(f"You are attempting to move the {ending}s")
        directory = starting_location(place)
        ending_file = ending_location(ending, place)

        for filename in os.listdir(directory):
            if filename.endswith(ending):
                print(f"{directory}/{filename}")
                os.rename(f"{directory}/{filename}", f"{ending_file}/{filename}")
                print(f"\tMoved to {ending_file}/{filename}")
                holder += 1
                print(f"The total number of {ending}s that were moved are {holder}")
            else:
                continue
    except:
        print("There were either no files to be moved, or there was an error moving the files. "
              "Contact the Creator to fix the problem.... Like everything else.")


def home():
    print("You choose home!")
    global place
    place = "home"


def school():
    print("You choose school!")
    global place
    place = "school"


def run_programs():
    try:
        if place.lower() == "home":
            print("You have selected home!")
            for item in home_extensions:
                printing_directory(item)
            else:
                print("Have a nice day!")
        elif place.lower() == "school":
            print("You have selected school!")
            for item in school_extensions:
                printing_directory(item)
            else:
                print("Have a nice day!")
        else:
            print("You did not select a correct option, goodbye!")
    except:
        print("There were either no files to be moved, or there was an error moving the files. "
              "Contact the Creator to fix the problem.... Like everything else.")


def GUI():
    root = tk.Tk()
    # shows icon, only works at home
    # root.iconbitmap(bitmap="C:/Sorted/ICO/thebest.ico")
    root.title("File Management")
    root.configure(bg='black')

    homeBTN = tk.Button(root, padx=25, pady=25, text="Home", bg='green', fg='gold', command=home)
    homeBTN.grid(sticky=tk.NSEW, row=1, column=3)

    schoolBTN = tk.Button(root, padx=25, text="School", bg='green', fg='gold', command=school)
    schoolBTN.grid(sticky=tk.NSEW, row=1, column=4)

    docxBTN = tk.Button(root, text="DOCX", bg='blue', fg='white', command=lambda: printing_directory(".docx"))
    docxBTN.grid(sticky=tk.NSEW, row=2, column=1)

    exeBTN = tk.Button(root, text="EXE", bg='blue', fg='white', command=lambda: printing_directory(".exe"))
    exeBTN.grid(sticky=tk.NSEW, row=2, column=2)

    gifBTN = tk.Button(root, padx=25, pady=25, text="GIF", bg='blue', fg='white',
                       command=lambda: printing_directory(".gif"))
    gifBTN.grid(sticky=tk.NSEW, row=2, column=3)

    jfifBTN = tk.Button(root, padx=25, pady=25, text="JFIF", bg='blue', fg='white',
                        command=lambda: printing_directory(".jfif"))
    jfifBTN.grid(sticky=tk.NSEW, row=2, column=4)

    jpegBTN = tk.Button(root, padx=25, pady=25, text="JPEG", bg='blue', fg='white',
                        command=lambda: printing_directory(".jpeg"))
    jpegBTN.grid(sticky=tk.NSEW, row=2, column=5)

    jpgBTN = tk.Button(root, padx=25, pady=25, text="JPG", bg='blue', fg='white',
                       command=lambda: printing_directory(".jpg"))
    jpgBTN.grid(sticky=tk.NSEW, row=2, column=6)

    mp3BTN = tk.Button(root, padx=25, pady=25, text="MP3", bg='blue', fg='white',
                       command=lambda: printing_directory(".mp3"))
    mp3BTN.grid(sticky=tk.NSEW, row=3, column=1)

    msiBTN = tk.Button(root, padx=25, pady=25, text="MSI", bg='blue', fg='white',
                       command=lambda: printing_directory(".msi"))
    msiBTN.grid(sticky=tk.NSEW, row=3, column=2)

    pdfBTN = tk.Button(root, padx=25, pady=25, text="PDF", bg='blue', fg='white',
                       command=lambda: printing_directory(".pdf"))
    pdfBTN.grid(sticky=tk.NSEW, row=3, column=3)

    pngBTN = tk.Button(root, padx=25, pady=25, text="PNG", bg='blue', fg='white',
                       command=lambda: printing_directory(".png"))
    pngBTN.grid(sticky=tk.NSEW, row=3, column=4)

    ppsxBTN = tk.Button(root, padx=25, pady=25, text="PPSX", bg='blue', fg='white',
                        command=lambda: printing_directory(".ppsx"))
    ppsxBTN.grid(sticky=tk.NSEW, row=3, column=5)

    psdBTN = tk.Button(root, padx=25, pady=25, text="PSD", bg='blue', fg='white',
                       command=lambda: printing_directory(".psd"))
    psdBTN.grid(sticky=tk.NSEW, row=3, column=6)

    pyBTN = tk.Button(root, padx=25, pady=25, text="PY", bg='blue', fg='white',
                      command=lambda: printing_directory(".py"))
    pyBTN.grid(sticky=tk.NSEW, row=4, column=1)

    rawBTN = tk.Button(root, padx=25, pady=25, text="RAW", bg='blue', fg='white',
                       command=lambda: printing_directory(".raw"))
    rawBTN.grid(sticky=tk.NSEW, row=4, column=2)

    tiffBTN = tk.Button(root, padx=25, pady=25, text="TIFF", bg='blue', fg='white',
                        command=lambda: printing_directory(".tiff"))
    tiffBTN.grid(sticky=tk.NSEW, row=4, column=3)

    txtBTN = tk.Button(root, padx=25, pady=25, text="TXT", bg='blue', fg='white',
                       command=lambda: printing_directory(".txt"))
    txtBTN.grid(sticky=tk.NSEW, row=4, column=4)

    wvmBTN = tk.Button(root, padx=25, pady=25, text="WVM", bg='blue', fg='white',
                       command=lambda: printing_directory(".wvm"))
    wvmBTN.grid(sticky=tk.NSEW, row=4, column=5)

    zipBTN = tk.Button(root, padx=25, pady=25, text="ZIP", bg='blue', fg='white',
                       command=lambda: printing_directory(".zip"))
    zipBTN.grid(sticky=tk.NSEW, row=4, column=6)

    AllBTN = tk.Button(root, padx=25, pady=25, text="All", bg='gold', fg='green', command=run_programs)
    AllBTN.grid(sticky=tk.NSEW, row=5, column=3)



    root.mainloop()


GUI()
