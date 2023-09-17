
from class_project import notebook_phon

x=notebook_phon()

while (1):
    print()
    print()
    print("▪︎ add number = add \n▪︎ show number = show \n▪︎ delete number = delete \n▪︎ serchnuber = serch \n▪︎ create phonebook txt file  = file \n▪︎ exit = exit")

    start=input( '---> What do you want to do?: ')
    print()

    if start=="add":
        x.addnumber()
    elif start=="show":
        x.shownumber()
    elif start=="delete":
        x.deletenumber()
    elif start=="serch":
        x.serchnumber()
    elif start=="file":
        x.fileNumber()
    elif start=="exit":
        exit()
    
        
        
        

        