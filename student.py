import pymysql as sql
from os import system
from getpass import getpass

def login():

    
    system('clear')
    usr=input("Enter username : ")
    password=getpass()
    database=input("Enter database name :")

    try:
        db=sql.connect("localhost",usr,password,database)
        cursor=db.cursor() 
        while True:
            print("What you want to do : ")
            q="""
                 1.Create table
                 2.Insert
                 3.Search
                 4.Display
                 5.Update
                 6.Exit"""
            print(q)   
            ch=int(input())
            system('clear')

            if ch==1:
               create()
            elif ch==2:
               insert()
            elif ch==3: 
               search()
            elif ch==4:
               display()   
            elif ch==5:
               update()
            elif ch==6:
               exit()
            else:
               print("Wrong choice ")             
                # flag=False
        db.close()
        
    except:
        print('Wrong credential')


def create():

    try:

        query="""CREATE table stu(rno SMALLINT PRIMARY KEY,
               name VARCHAR(20) NOT NULL,sem SMALLINT DEFAULT 1,branch VARCHAR(10) NOT NULL,marks FLOAT DEFAULT 0.0)"""

        cursor.execute(query)

    except:
        print("Table already exist ")    

def insert():

    d_roll=int(input("Enter roll no. : "))
    d_name=input("Enter name : ")
    d_sem=int(input("Enter semester : "))
    d_branch=input("Enter branch : ")
    d_marks = float(input("Enter marks : "))

    system('clear')
    print("Entries saved successfully ")


    query = """INSERT INTO stu (rno,name,sem,branch,marks)
            VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(query,(int(d_roll),str(d_name),int(d_sem),str(d_branch),float(d_marks)))
    db.commit()
    

    
    

# insert()   

def search():

    print("Enter criteria for searching : ")
    print("1.By Roll no \n2.By Name \n3.By Semester \n4.By branch\n5.By Marks")
    ch=int(input())


    system('clear')

    try:
        if ch==1:
           id = int(input("Enter roll no : "))
           query = """SELECT * FROM stu
                    where rno=%s"""
           cursor.execute(query,(int(id)))
           res=cursor.fetchall()

        elif ch==2:
           name=input("Enter name : ")
           query = """SELECT * FROM stu
                    where name=%s"""
           cursor.execute(query,(name))
           res=cursor.fetchall()   

        elif ch==3:
           sem=input("Enter semester : ")
           query = """SELECT * FROM stu
                    where sem=%s"""
           cursor.execute(query,int((sem)))
           res=cursor.fetchall()
        
        elif ch==4:
           branch=input("Enter branch : ")
           query = """SELECT * FROM stu
                    where branch=%s"""
           cursor.execute(query,(branch))
           res=cursor.fetchall()

        elif ch==5:
           marks=input("Enter marks : ")
           query = """SELECT * FROM stu
                    where marks=%s"""
           cursor.execute(query,(float(marks)))
           res=cursor.fetchall()   
        else:
            print("Wrong choice")

    except:
       print("No result")    

    # print(res)
    if res:
        for i in res:
            print('Roll no  : '+str(i[0]))
            print('Name     : '+str(i[1]))
            print('Semester : '+str(i[2]))
            print('Branch   : '+str(i[3]))
            print('Marks    : '+str(i[4]))
            print()
    else:
      print("Not avaliable")        



# search()

def display():
    try:
        query = """SELECT * FROM stu"""
        cursor.execute(query)
        data = cursor.fetchall()
        print("*********************")
        for i in data:

            print('Roll no  : '+str(i[0]))
            print('Name     : '+str(i[1]))
            print('Semester : '+str(i[2]))
            print('Branch   : '+str(i[3]))
            print('Marks    : '+str(i[4]))
            print("*********************")
    except:
        print("Table does not exist")


# show()


def update():
    

    roll=int(input("Enter roll no. whose detail you want to update : "))
    system('clear')
    print("Enter new details : ")
    d_name=input("Enter name : ")
    d_sem=int(input("Enter semester : "))
    d_branch=input("Enter branch : ")
    d_marks = float(input("Enter marks : "))

    system('clear')
    print("Entries update successfully ")


    query="""UPDATE stu
         SET name=%s , sem=%s , branch=%s , marks=%s
         WHERE rno=%s"""
    cursor.execute(query,(str(d_name),int(d_sem),str(d_branch),float(d_marks),int(roll)))
    db.commit()

# update()
input("\n\t\t***** Welcome  to student database *****")
# flag=True
# while flag:
login()



    





