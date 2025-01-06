import os

def help_Menu():
    print("Available Commands:")
    #Change the directory
    print("\tCDIR <directory> - Change the directory to the new directory")
    #List of files in the current directory
    print("\tLIST - List of files in the current directory.")
    #List of files in a specific directory
    print("\tLIST <directory> - List of files in the directory.")
    #Delete a file in the current directory or a specific directory
    print("\tDELETE <filename> - Delete a file.")
    #Rename a file or directory 
    print("\tRENAME <oldname> <newname> - Rename a file or directory.")
    #make a new directory
    print("\tMKD <Directory name> - make a new directory.")
    #Remove a directory
    print("\tRD <Directory name> - Remove the directory.")
    #Show available commands
    print("\tHELP - Show available commands.")
    #Exit
    print("\tEXIT - Exit the mini OS.")

def Run_Command(command):
    try:
        cmd, *args = command.split()
        arg = " ".join(args)
        if cmd=="cdir":#change dir
            Change_dir(arg)
            return True
        elif cmd=="list":#list of files in the dir
            List_files(arg)
            return True
        elif cmd=="delete":#delete a file in the dir
            Delete_file(arg)
            return True
        elif cmd=="rename":#rename a file in the dir
            Rename_file()
            return True
        elif cmd=="mkd":#make a dir
            Make_dir(arg)
            return True
        elif cmd=="rd":#remove a dir
            Remove_dir(arg)
            return True
        elif cmd=="help":#show available commands
            help_Menu()
            return True
        elif cmd=="exit":#exit the mini OS
            print("Exiting the mini OS. Goodbye!")
            return False 
    except Exception as e:
        print(f"Error: {e}")
        return True

def Change_dir():
    try:
        os.chdir(arg)#change the current directory to the arg directory
        BASE_DIR = os.getcwd()#update the current directory
        print("\tDirectory changed.\n")
    except FileNotFoundError:
        print("\tDirectory not found.\n")
def List_files(arg):
    #path can be the current path or a certain path
    path = arg if arg else BASE_DIR
    try:
        files = os.listdir(path)#list of files in the path
        for file in files:
            file_path = os.path.join(path, file)#creat file path
            size = os.path.getsize(file_path)#size of file
            opening_time = time.ctime(os.path.getmtime(file_path))#creating file's time  
            print(f"{opening_time} | {file} | {size} bytes ")
    except FileNotFoundError:
        print("\tPath not found.\r\n")
def Delete_file(arg):
    try:
        os.remove(arg)#remove the file
        print("\tFile deleted successfully.\n")
    except FileNotFoundError:
        print("\tFile not found.\r\n")
def Rename_file():
    input=1
def Make_dir(arg):
    try:
        os.makedirs(arg)
        print(f"\t\"{arg}\" directory created.\n")
    except Exception as e:
        print(f"\tFailed to create directory: {e}\n")
def Remove_dir(arg):
    try:
        os.rmdir(arg)
        print(f"\tDirectory \"{arg}\" removed successfully.\n")
    except Exception as e:
        print(f"\tFailed to remove directory: {e}\n")
def Change_dir():
    input=1

def main():
    print("Welcome to the Mini OS!")

if __name__ == "__main__":
    main()

