import mysql.connector
import os
import datetime

cnx = mysql.connector.connect(user='root', password='',
                                
                                  database='laspalmasmedicalcenter',
                                  use_pure=False)


def displayMainMenu():
    print('------- MENU -------')
    print(' 1. show data in the tables')
    print(' 2. Get Average of a column')
    print(' 3. Insert data into tables')
    print(' 4. Delete record from table')
    print(' Enter any (0,5,6,7,8,9) to exit')
   
def initDB():
    mycursor = cnx.cursor()   

#show data in the tables        
        
def getAllUsers():
    
    print('------- TAbles -------')
    print('  1. Affiliatedwith')
    print('  2. Appointment')
    print('  3. Department')
    print('  4. Medication')
    print('  5. oncall')
    print('  6. Patient')
    print('  7. Nurse')
    print('  8. Physician')
    print('  9. Procedure')
    print('  10. Room')
    print('  11. Undergoes')
    print('  11. Stay')
    table = str(input("Which table data you want to see?\n"))
    if table in ['affiliatedwith','appointment','department','medication','oncall','patient','nurse','physician','prescribes','`procedure`','room','undergoes','stay']:
        

        mycursor = cnx.cursor()
        print('------ Information in the table------\n')
        mycursor.execute("SELECT * FROM %s" % table,)
        
        myresult = mycursor.fetchall()
      
 
            
        for row in myresult:
            print(row)
            print("\n")
        #exit()

#for getting average               
def getAverage():
    
    
    print('------- MENU -------')
    print(' a. Get tables')
    print(' b. Get info in tables')
    print(' c. Get average of column from table')
    
    while(True):
        
        print('------- TAbles -------')
        print('  1. Affiliatedwith')
        print('  2. Appointment')
        print('  3. Department')
        print('  4. Medication')
        print('  5. oncall')
        print('  6. Patient')
        print('  7. Nurse')
        print('  8. Physician')
        print('  9. `Procedure`')
        print('  10. Room')
        print('  11. Undergoes')
        print('  11. Stay')
    
        #enter option
            
        r =str(input("Enter your option a for info of the tables, b for getting average"))
                
       
        if r == 'a':
            mycursor = cnx.cursor()
            table = str(input("Which table you want to see information?\n"))
            if table in ['affiliatedwith','appointment','department','medication','oncall','patient','nurse','physician','prescribes','`procedure`','room','undergoes','stay']:
                mycursor.execute("SHOW COLUMNS FROM %s" % table,)
                myresult = mycursor.fetchall()
                for row in myresult:
                    print(row)
                    print("\n")
        elif r == 'b':
            mycursor = cnx.cursor()
            
            column = str(input("enter column name:"))
            table = str(input("enter table name:"))
            
            mycursor.execute("select avg(%s) from %s" %(column,table))
            
            myresult = mycursor.fetchone()
            print(myresult)
            
        else:
            return
            
#insert data
      
def insertdata():
    
    print('------- TAbles -------')
    print('  1. Affiliatedwith')
    print('  2. Appointment')
    print('  3. Department')
    print('  4. Medication')
    print('  5. oncall')
    print('  6. Patient')
    print('  7. Nurse')
    print('  8. Physician')
    print('  9. Procedure')
    print('  10. Room')
    print('  11. Undergoes')
    print('  11. Stay')
    while(True):
        table = str(input("enter table:"))
        if table == 'physician':
            mycursor = cnx.cursor()

            print('------ physician regestration ------\n')
            
            phy_id=  int(input('Enter id : '))
            name = input('Enter name:')
            position = (input('Enter position : '))
            SSN = int(input('Enter SSN : '))
            
            sql = 'INSERT INTO `Physician` (`physicianid`,`name`,`position`,`ssn`) VALUES (%s,%s,%s,%s)'
            val = (phy_id,name,position,SSN)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
        if table == 'department':
            mycursor = cnx.cursor()
            print('------Department registration-----')
            dept_id = int(input('Enter Department Id: '))
            name = input('Enter department name: ')
            head_id = int(input('Enter the head Id of the department: '))
            sql = 'INSERT INTO `department` (`deptid`,`name`,`headid`) VALUES (%s,%s,%s)'
            val = (dept_id,name,head_id)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
        
        if table =='affiliatedwith':
            mycursor = cnx.cursor()
            print('------physician affiliated with-----')
            
            phy_id = int(input('Enter physician id: '))
            dept_id = int(input("Enter department id: "))
            sql = 'INSERT INTO `affiliatedwith` (`physicianid`,`departmentid`) VALUES (%s,%s)'
            val = (phy_id,dept_id)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
        
        
        if table =='procedure':
            mycursor = cnx.cursor()
            print('------procedure-----')
            
            proc_id = int(input('Enter procedure id: '))
            name = input("Enter procedure name: ")
            cost = int(input("Enter the cost: "))
            sql = 'INSERT INTO `procedure` (`procid`,`name`,`cost`) VALUES (%s,%s,%s)'
            val = (proc_id,name,cost)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
            
        if table =='patient':
            mycursor = cnx.cursor()
            print('------patient-----')
            
            patient_id = int(input('Enter patient id: '))
            ssn = int(input("Enter ssn: "))
            name = input("Enter patient name: ")
            date =  input("Enter a date in YYYY-MM-DD format: ")
            
            phone_no = input("Enter phone number: ")
            i_n = int(input("Enter insurance number: "))
            prim_pid = int(input("Enter primary physician id: "))
            sql = 'INSERT INTO `patient` (`patientid`,`ssn`,`name`,`dob`,`phone`,`insurancenumber`,`primaryphysid`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            val = (patient_id,ssn,name,date,phone_no,i_n,prim_pid,)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
            
        if table =='nurse':
            mycursor = cnx.cursor()
            print('------Nurse-----')
            
            nurse_id = int(input('Enter nurse id: '))
           
            name = input("Enter patient name: ")
            position = input("Enter position: ")
            ssn = int(input("Enter ssn: "))
            
           
            sql = 'INSERT INTO `nurse` (`nurseid`,`name`,`position`,`ssn`) VALUES (%s,%s,%s,%s)'
            val = (nurse_id,name,position,ssn)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
            
        if table =='medication':
            mycursor = cnx.cursor()
            print('------Medication-----')
            
            med_id = int(input('Enter medication id: '))
           
            name = input("Enter medication name: ")
           
            
           
            sql = 'INSERT INTO `medication` (`medid`,`name`) VALUES (%s,%s)'
            val = (med_id,name)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
        if table =='prescribes':
            mycursor = cnx.cursor()
            print('------Prescribed medcine-----')
            
            phy_id = int(input("Enter physician id: "))
            pa_id = int(input("Enter patient id: "))
            med_id =int(input("Enter medication id: "))
            date =  input("Enter prescribed date in YYYY-MM-DD format: ")
            dose = input("Enter the dosage: ")
           
         
            
           
            sql = 'INSERT INTO `prescribes` (`physicianid`,`patientid`,`medicationid`,`prescribeddate`,`dose`) VALUES (%s,%s,%s,%s,%s)'
            val = (phy_id,pa_id,med_id,date,dose)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
        if table =='room':
            mycursor = cnx.cursor()
            print('------Room-----')
            
            room_id = int(input("Enter Room id: "))
            room_type= (input("Enter Room type: "))
            
              
            sql = 'INSERT INTO `room` (`roomid`,`roomtype`) VALUES (%s,%s)'
            val = (room_id,room_type)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
        if table =='stay':
            mycursor = cnx.cursor()
            print('------Prescribed medcine-----')
            
            stay_id = int(input("Enter stay id: "))
            pa_id = int(input("Enter patient id: "))
            room_id =int(input("Enter room  id: "))
            start_date =  input("Enter start date in YYYY-MM-DD format: ")
            end_date =  input("Enter end date in YYYY-MM-DD format: ")
            
           
         
            
           
            sql = 'INSERT INTO `stay` (`stayid`,`patientid`,`roomid`,`startdate`,`enddate`) VALUES (%s,%s,%s,%s,%s)'
            val = (stay_id,pa_id,room_id,start_date,end_date)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
        if table =='undergoes':
            mycursor = cnx.cursor()
            print('------Undergoes-----')
            
            pa_id = int(input("Enter Patient id: "))
            proc_id = int(input("Enter Procedure id: "))
            stay_id =int(input("Enter Stay  id: "))
            proc_date =  input("Enter procedure date in YYYY-MM-DD format: ")
            phy_id = int(input("Enter physician id: "))
            nu_id = int(input("Enter nurse id: "))
            
        
            sql = 'INSERT INTO `undergoes` (`patientid`,`procedureid`,`stayid`,`procdate`,`physicianid`,`nurseid`) VALUES (%s,%s,%s,%s,%s,%s)'
            val = (pa_id,proc_id,stay_id,proc_date,phy_id,nu_id)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
            
        if table =='oncall':
            mycursor = cnx.cursor()
            print('------Oncall-----')
            
            nu_id = int(input("Enter Nurse id: "))
            
            start_date =  input("Enter start date in YYYY-MM-DD format: ")
            end_date =  input("Enter end date in YYYY-MM-DD format: ")
            
            
        
            sql = 'INSERT INTO `oncall` (`nurseid`,`startdate`,`enddate`) VALUES (%s,%s,%s)'
            val = (nu_id,start_date,end_date)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
            
            
        if table =='appointment':
            mycursor = cnx.cursor()
            print('------Appointment-----')
            
            app_id = int(input("Enter appointment id: "))
            pa_id = int(input("Enter Patient id: "))
            nu_id = int(input("Enter Nurse id: "))
            phy_id = int(input("Enter physician id: "))
            st_dt_time = input("Enter end date in YYYY-MM-DD time:time format: ")
            end_dt_time = input("Enter end date in YYYY-MM-DD time:time format: ")
           
            
        
            sql = 'INSERT INTO `appointment` (`appid`,`patientid`,`nurseid`,`physicianid`,`startdatetime`,`enddatetime`) VALUES (%s,%s,%s,%s,%s,%s)'
            val = (app_id,pa_id,nu_id,phy_id,st_dt_time,end_dt_time)
            mycursor.execute(sql,val)
            cnx.commit()
            
            print('------ SUCCESS ------\n')
        
            
        else:
            return
        
#delete record       
def deleterecord():
    print('------- TAbles -------')
    print('  1. Affiliatedwith')
    print('  2. Appointment')
    print('  3. Department')
    print('  4. Medication')
    print('  5. oncall')
    print('  6. Patient')
    print('  7. Nurse')
    print('  8. Physician')
    print('  9. `Procedure`')
    print('  10. Room')
    print('  11. Undergoes')
    print('  11. Stay')

    while(True):
        table = str(input("enter table:"))
        if table == 'physician':
            mycursor = cnx.cursor()
            phy_id = str(input("enter physician id:"))
            
            mycursor.execute("DELETE FROM %s WHERE physicianid = %s"%(table,phy_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'department':
            mycursor = cnx.cursor()
            dept_id = str(input("enter department id:"))
            
            mycursor.execute("DELETE FROM %s WHERE deptid = %s"%(table,dept_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'affiliatedwith':
            mycursor = cnx.cursor()
            phy_id = str(input("enter physician id:"))
            
            mycursor.execute("DELETE FROM %s WHERE physicianid = %s"%(table,phy_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == '`procedure`':
            mycursor = cnx.cursor()
            proc_id = str(input("enter procedure id:"))
            
            mycursor.execute("DELETE FROM %s WHERE procid = %s"%(table,proc_id))
            
            cnx.commit()
        
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
        
        elif table == 'patient':
            mycursor = cnx.cursor()
            p_id = str(input("enter patient id:"))
            
            mycursor.execute("DELETE FROM %s WHERE patientid = %s"%(table,p_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
        elif table == 'nurse':
            mycursor = cnx.cursor()
            n_id = str(input("enter nurse id:"))
            
            mycursor.execute("DELETE FROM %s WHERE nurseid = %s"%(table,n_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue ')
            
        elif table == 'medication':
            mycursor = cnx.cursor()
            m_id = str(input("enter medication id:"))
            
            mycursor.execute("DELETE FROM %s WHERE medid = %s"%(table,m_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
        elif table == 'prescribes':
            mycursor = cnx.cursor()
            p_id = str(input("enter patient id:"))
            
            mycursor.execute("DELETE FROM %s WHERE patientid = %s"%(table,p_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'room':
            mycursor = cnx.cursor()
            r_id = str(input("enter room id:"))
            
            mycursor.execute("DELETE FROM %s WHERE roomid = %s"%(table,r_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
        elif table == 'stay':
            mycursor = cnx.cursor()
            s_id = str(input("enter stay id:"))
            
            mycursor.execute("DELETE FROM %s WHERE patientid = %s"%(table,s_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'undergoes':
            mycursor = cnx.cursor()
            p_id = str(input("enter patient id:"))
            
            mycursor.execute("DELETE FROM %s WHERE patientid = %s"%(table,p_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'oncall':
            mycursor = cnx.cursor()
            n_id = str(input("enter nurse id:"))
            
            mycursor.execute("DELETE FROM %s WHERE nurseid = %s"%(table,n_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
        elif table == 'appointment':
            mycursor = cnx.cursor()
            a_id = str(input("enter appointment id:"))
            
            mycursor.execute("DELETE FROM %s WHERE appid = %s"%(table,a_id))
            
            cnx.commit()
            print('--------Deleted-------')
            print('Enter anything for menu or continue')
            
            
            
            
        
        else:
            return
            

            

    
        
def run():
    
    while(True):
        displayMainMenu()
        n = int(input("Enter option : "))
        if n == 1:
            getAllUsers()
        elif n==2:
            getAverage()
        elif n == 3:
            insertdata()
        elif n == 4:
            deleterecord()
            
        else:
            return

if __name__ == '__main__':
    initDB()
    run()