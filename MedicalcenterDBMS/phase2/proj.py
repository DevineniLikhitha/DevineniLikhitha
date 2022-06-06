import mysql.connector
from sys import argv
#question 1 Find physicians that have performed a given procedure name. Show the detailed information of each physician. 
def one():
    
    
    cnx = mysql.connector.connect(user='root', password='',
                                    
                                      database='laspalmasmedicalcenter',
                                      use_pure=False)
    
    
    
    pr_name = str(argv[2])
   
   
    
    
    proc_name = (pr_name,)
    
    mycursor = cnx.cursor()
        
    query_one="select p.physicianID,p.name,p.position,p.ssn from physician p, `procedure` pr, undergoes u where p.physicianID=u.physicianID and u.procedureID= pr.procID and pr.name =%s"
   
    mycursor.execute(query_one,proc_name)
  
   
        
    myresult = mycursor.fetchall()
  
    
    while myresult:
        print(myresult)
        myresult = mycursor.fetchall()



#2. Find appointments where a patient met with a physician other than their primary physician. Show patient name, physician name, nurse name, start and end datetime of appointment, and the name of the patient's primary physician.
def two():
    cnx = mysql.connector.connect(user='root', password='',
                                
                                  database='laspalmasmedicalcenter',
                                  use_pure=False)
    mycursor = cnx.cursor()
  
    
    q1='select p.name as patient_name,ph.name as physician_name,n.name as nurse_name,a.startDateTime,a.endDateTime,v.name as primary_physican from patient p, appointment a,nurse n,physician ph,v1 v where p.patientID=a.patientID and n.nurseID=a.nurseID and ph.physicianID=a.physicianID and v.physicianID=p.primaryPhysID and primaryPhysID not in (select physicianID from appointment,patient where p.primaryPhysID=a.physicianID);' 
    f'create view v1 as select ph.physicianID,ph.name from patient p,physician ph where p.primaryPhysID=ph.physicianID;'
   
    mycursor.execute(q1)

    
    myresult = mycursor.fetchall()
    
    
    for x in myresult:
        print(x)
    cnx.close()
    
#3. Find the patients that have undergone a procedure with a cost larger than a given cost. Show the detailed information of each patient. 
    
def three():
    cnx = mysql.connector.connect(user='root', password='',
                                
                                  database='laspalmasmedicalcenter',
                                  use_pure=False)
    cost = str(argv[2])
    cost_num=(cost,)
    mycursor = cnx.cursor()

    q="select p.patientID,p.ssn,p.name,p.address,p.dob,p.phone,p.insuranceNumber,p.primaryPhysID from patient p, `procedure` pr, undergoes u where p.patientID=u.patientID and u.procedureID=pr.procID and pr.cost > %s"
    mycursor.execute(q,cost_num)

    myresult = mycursor.fetchall()
    while myresult:
        print(myresult)
        myresult = mycursor.fetchall()
        
#4. Find the patients that their primary physician is the head of a given department name. Show the detailed information of each patient. 
        
def four():
    cnx = mysql.connector.connect(user='root', password='',
                                
                                  database='laspalmasmedicalcenter',
                                  use_pure=False)
    pr_name =str(argv[2])
    
    proc_name=(pr_name,)
    
    mycursor = cnx.cursor()
    q="select p.patientID,p.ssn,p.name,p.address,p.dob,p.address,p.dob,p.phone,p.insuranceNumber,p.primaryPhysID from patient p, department d where d.headId = p.primaryphysID and d.name =%s"
    
    mycursor.execute(q,proc_name)

    myresult = mycursor.fetchall()
    while myresult:
        print(myresult)
        myresult = mycursor.fetchall()
        
#5. Find information about a prescribed medication name. Show the patients name, physicians names, and the prescribed dates.       
        
def five():
    
    cnx = mysql.connector.connect(user='root', password='',
                                    
                                      database='laspalmasmedicalcenter',
                                      use_pure=False)
    
    
    
    m_name = str(argv[2])
    
   
    
    
    med_name = (m_name,)
    
    mycursor = cnx.cursor()
        
    q="select pa.name as patient_name,ph.name as physician_name,pe.prescribedDate from prescribes pe, patient pa, physician ph, medication m where pa.patientID=pe.patientID and ph.physicianID=pe.physicianID and m.medID=pe.medicationID and m.name= %s"
 
    mycursor.execute(q,med_name)
  
    
        
    myresult = mycursor.fetchall()
    
    while myresult:
        print(myresult)
        myresult = mycursor.fetchall()
        
#6. Find nurses who have been on call at a given date. Show the detailed information of each nurse and their on call start date and end date.
        
def six():
    
    
    cnx = mysql.connector.connect(user='root', password='',
                                    
                                      database='laspalmasmedicalcenter',
                                      use_pure=False)
    
    
    
    date = str(argv[2])
   
   
    
    
    given_date= (date,)
    
    mycursor = cnx.cursor()
        
    query_six="select n.nurseID,n.name,n.position,n.ssn,o.startDate,o.endDate from nurse n, oncall o where n.nurseID=o.nurseID and  %s between o.startDate and o.endDate;"
   
    mycursor.execute(query_six,given_date)
  
   
        
    result_six = mycursor.fetchall()
  
    
    for x in result_six:
        print(x)
    cnx.close()
    
    
#7. Find all patients that have stayed together in a "Double" room at a given date. For each room ID, show each patient's name and their start and end date of stay.
def seven():
    
    
    cnx = mysql.connector.connect(user='root', password='',
                                    
                                      database='laspalmasmedicalcenter',
                                      use_pure=False)
    
    
    
    date_ = str(argv[2])
   
   
    
    
    givendate= (date_,)
    
    mycursor = cnx.cursor()
        
    query_seven="select s.roomid, p.name, s.startdate, s.enddate from stay s, room r, patient p where r.roomtype = 'Double'  and r.roomid = s.roomid and %s between s.startdate and s.enddate and s.patientid = p.patientid and  s.roomid in (select roomid from stay where %s between startdate and enddate group by roomid having count(patientid) >1);"
   
    mycursor.execute(query_seven,givendate)
  
   
        
    result_six = mycursor.fetchall()
  
    
    for x in result_six:
        print(x)
    cnx.close()
    
#8. Find information about all appointments with physicians affiliated with a given department name. Show the detailed information of each patient along with the detailed information of the physician with whom they have met and the appointment ID. 
def eight():
    
    cnx = mysql.connector.connect(user='root', password='',
                                    
                                      database='laspalmasmedicalcenter',
                                      use_pure=False)
    
    
    
    d_name = str(argv[2])
    
    
    

    
    
    dep_name=(d_name,)
    
    mycursor = cnx.cursor()
        
    q="select pa.patientID,pa.ssn,pa.name, pa.address,pa.dob,pa.phone,pa.insuranceNumber,pa.primaryPhysID,ph.physicianID,ph.name,ph.position,ph.ssn,a.appID from physician ph,patient pa, appointment a,affiliatedwith af,department d where a.physicianID=ph.physicianID and a.patientID=pa.patientID and af.physicianID=ph.physicianID and af.departmentID=d.deptID and ph.physicianID = d.headID and d.name =%s"
    mycursor.execute(q,dep_name)
  
           
    ans_eight = mycursor.fetchall()
    
    
    while ans_eight:
        print(ans_eight)
        ans_eight = mycursor.fetchall()
#calling all the functions
def main():
    if argv[1]=='1':
        print(one())
    if argv[1]=='2':
        print(two())
    if argv[1]=='3':
        print(three())
    if argv[1]=='4':
        print(four())
    if argv[1]=='5':
        print(five())
    if argv[1]=='6':
        print(six())
    if argv[1]=='7':
        print(seven())
    if argv[1]=='8':
        print(eight())
        
#main function
if __name__ == "__main__":
    main()

    
