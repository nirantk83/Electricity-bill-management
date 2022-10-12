import mysql.connector
import datetime
from tabulate import tabulate


db=input("Enter name of your database:")
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
sql="create database if not exists %s" %(db,)
mycursor.execute(sql)
print("database created successfully")
mycursor=mydb.cursor()
mycursor.execute('use '+db)
tablename=input('enter table name')
query="create table if not exists "+tablename+"(custno int primary key,cname varchar(15),cadd varchar(20),cmeterno varchar(20),creadings int,customer_bill float,Billgendate date,Due_date date)"
print('table'+tablename+'created succesfully')
mycursor.execute(query)

while True:
    print('\n\n\n')
    print("*"*90)
    print('\t\t\t\tMain Menu')
    print("*"*90)
    print('\t\t\t\t1.add customer')
    print('\t\t\t\t2.display record of all customer')
    print('\t\t\t\t3.display record of particular customer')
    print('\t\t\t\t4.delete record of all customer') 
    print('\t\t\t\t5.delete record of particular customer')
    print('\t\t\t\t6.modification in record')
    print('\t\t\t\t7.bill of all customer')
    print('\t\t\t\t8.bill of perticulat customer')
    print('\t\t\t\t11.print Final bill of customer')
    print('\t\t\t\t12.print Ongiing Month bill')
    print('\t\t\t\t10.exit')
    print('enter choice',end='')
    choice=int(input())
    if choice==1:
        try:  
            print("enter customer info")
            custno=int(input("enter customer no:"))
            cname=input("enter customer name:")
            cadd=input("enter customer addres:")
            cmeterno=input('enter customer meter no')
            Billgendate=input('enter date')
            Due_date=input('enter due date')
            creadings=int(input("enter reading"))
            
            if creadings<100:
               customer_bill=creadings*0+100
               print('the bill is',customer_bill,'Rs')
            elif 100<=creadings<200:
               customer_bill=creadings*5 
               print('bill is:',customer_bill)
            elif creadings>=200:
              customer_bill=((creadings-200)*10)+(((creadings-(creadings-200))-100)*5)
              print(customer_bill)
            else:  
              print('enter proper reading')
              
            rec=(custno,cname,cadd,cmeterno,creadings,customer_bill,Billgendate,Due_date)
            query="insert into "+tablename+" values(%s,%s,%s,%s,%s,%s,%s,%s)"  
            mycursor.execute(query,rec)
            mydb.commit()
            print('record added')
            
        except Exception as e:
            print("something went wrong",e)



    elif choice==2:
        try:
            query="select * from "+tablename
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['custno','cname','cadd','cmeterno','creadings','customer_bill','Billgendate','Due_date'],tablefmt='psql'))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)
        except Exception as e:
            print("something went wrong",e)
 

            
    elif choice==3:
        try:
            en=input("enter customer no of record to be displayed")
            query="select * from "+tablename+" where custno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\n record of customer no:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==1:
                print("")
                                
        except Exception as e:
            print("something went wrong",e)

    elif choice==4:
        try:
            ch=input("do you want to delete all records of customer(y/n)")
            if ch.upper()=='Y' or 'y':           
                mycursor.execute('delete from '+tablename)
                mydb.commit()
                print("all records are deleted")
                                
        except Exception as e:
            print("something went wrong",e)

    elif choice==5:
        try:
            en=input("enter customer no of record to be deleted")
            query="delete from "+tablename+" where custno="+en            
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("deletion done")
            else:
                print("customer no",en,"not found")
                                
        except Exception as e:
            print("something went wrong",e)

                                 
    elif choice==6:
        try:
            en=input("enter customer no of record to be modified")
            query="select * from "+tablename+" where custno="+en            
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print("custno"+en+"does not exist")
            else:
                cname=myrecord[1]
                cadd=myrecord[2]
                creadings=myrecord[3]
                cmeterno=myrecord[4]
                customer_bill=myrecord[5]
                print("cust no:",myrecord[0])
                print("cname:",myrecord[1])
                print("cadd",myrecord[2])
                print("creadings",myrecord[3])
                print("cmeterno",myrecord[4])
                print("customer_bill",myrecord[5])
               
                print("type value to modify below or just press enter for no change")
                x=input("enter name:")
                if len(x)>0:
                    cname=x
                x=input("enter cadd")
                if len(x)>0:
                    cadd=x
                x=input("enter cmeterno")
                if len(x)>0:
                    cmeterno=(x)  
                x=input("enter creadings")
                if len(x)>0:
                    creadings=(x)

                x=input("enter Billing date")
                if len(x)>0:
                    Billgendate=(x)

                x=input("enter Due_date")
                if len(x)>0:
                    Due_date=(x)    
                    
                
                query="update "+tablename+" set cname ="+ cname + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                query="update "+tablename+" set cadd ="+ cadd + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")


                query="update "+tablename+" set cmeterno ="+ cmeterno + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                query="update "+tablename+" set creadings ="+ creadings + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                query="update "+tablename+" set Billgendate ="+ Billgendate + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                query="update "+tablename+" set Due_date ="+ Due_date + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")


                

                cunits = int(input("Enter Current Units on Meter : "))
                punits = int(input("Enter Previous Units of Meter : "))
                creadings=cunits-punits
                if creadings<100:
                  customer_bill=creadings*0+100
                  print('the bill is',customer_bill,'Rs')
                elif 100<=creadings<200:
                  customer_bill=creadings*5 
                  print('bill is:',customer_bill)
                elif creadings>=200:
                  customer_bill=((creadings-200)*10)+(((creadings-(creadings-200))-100)*5)
                  print(customer_bill)
                else:  
                  print('enter proper reading')

                print("type value to modify below or just press enter for no change")
                x=input("enter customer bill:")
                if len(x)>0:
                    customer_bill=x
                
                query="update "+tablename+" set customer_bill="+ customer_bill + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")


 
   


                
                
        except:
                print("something went wrong")


            
    elif choice==7:
        try:
            query="select * from "+tablename
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['custno','cname','cmeterno','creadings','customer_bill','Billgendate','Due_date'],tablefmt='psql'))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print(rec)
        except Exception as e:
            print("something went wrong",e)

                     
    elif choice==8:
        try:
            en=input("enter customer no to display light bill")
            query="select * from "+tablename+" where custno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\n record of customer no:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==1:
                print("")
                                
        except Exception as e:
            print("something went wrong",e)


            

  

            

    elif choice==11:
        try:
            en=input("enter customer no to display the bill ")
            query="select * from "+tablename+" where custno="+en            
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print("custno"+en+"does not exist")
            else:
                cname=myrecord[1]
                cadd=myrecord[2]
                cmeterno=myrecord[3]
                creadings=myrecord[4]
                customer_bill=myrecord[5]
                Due_date=myrecord[7]
                Billgendate=myrecord[6]
            
                print("cust no       :",myrecord[0])
                print("cname         :",myrecord[1])
                print("cadd          :",myrecord[2])
                print("cmeterno      :",myrecord[3])
                print("creadings     :",myrecord[4])
                print("customer_bill :",myrecord[5],'Rs')
                print("Billgendate   :",myrecord[6])
                print("Due_date      :",myrecord[7])
                
        except:
                print("something went wrong")


    elif choice==12:
        try:
            en=input("enter customer no to display the bill ")                                  
            query="select * from "+tablename+" where custno="+en           
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print("custno"+en+"does not exist")
            else:
                cname=myrecord[1]
                cadd=myrecord[2]
                cmeterno=myrecord[3]
                creadings=myrecord[4]
                customer_bill=myrecord[5]
                Due_date=myrecord[7]
                Billgendate=myrecord[6]
                print("cust no       :",myrecord[0])
                print("cname         :",myrecord[1])
                print("cadd          :",myrecord[2])
                print("cmeterno      :",myrecord[3])
                print("last month creadings     :",myrecord[4])
                print("Old Month customer_bill :",myrecord[5],'Rs')
                print("Billgendate   :",myrecord[6])
                print("Due_date      :",myrecord[7])


                
                print("type value to modify below or just press enter for no change")
                
                x=input("enter creadings")
                if len(x)>0:
                    creadings=(x)
                
                query="update "+tablename+" set creadings="+ creadings + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")






                cunits = int(input("Enter current Units of Meter : "))
                punits = int(input("Enter Previous Units of Meter : "))
                creadings=cunits-punits
                if creadings<100:
                  customer_bill=creadings*0+100
                  print('the bill is',customer_bill,'Rs')
                elif 100<=creadings<200:
                  customer_bill=creadings*5 
                  print('bill is:',customer_bill)
                elif creadings>=200:
                  customer_bill=((creadings-200)*10)+(((creadings-(creadings-200))-100)*5)
                  print(customer_bill)
                else:  
                  print('enter proper reading')

                print("type value to modify below or just press enter for no change")
                x=input("enter customer bill:")
                if len(x)>0:
                    customer_bill=x
                
                query="update "+tablename+" set customer_bill="+ customer_bill + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                print("type value to modify below or just press enter for no change")
                x=input("enter billing date:")
                if len(x)>0:
                    Billgendate=x
                
                query="update "+tablename+" set Billgendate="+ Billgendate + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")

                print("type value to modify below or just press enter for no change")
                x=input("enter Due date:")
                if len(x)>0:
                   Due_date=x
                

                query="update "+tablename+" set Due_date="+ Due_date + "where custno="+en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print("record modified")


                
        except:
                print("something went wrong")

 
              


    elif choice==10:
             break
    else:
            print("wrong choice")
            
print("*"*10)


