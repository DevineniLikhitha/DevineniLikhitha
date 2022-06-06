
/* Project phase one*/
create database laspalmasmedicalcenter;


use laspalmasmedicalcenter;
/* Physican*/
create table Physician
			(physicianID int,
			 name varchar(40),
			 position varchar(40),
			 ssn int,
			 primary key(physicianID),
			 check(position in('Intern','Surgeon','senior','Chiefofmedicine','Resident','Psychiartist'))
			);
            

/*Department*/


create table Department
			(deptID int,
			 name varchar(40),
			 headID int,
			 primary key(deptID),
			 foreign key(headID)references Physician(physicianID)on delete set null,
			 check(name in('GeneralMedicine','Surgery','Psychiatry'))
			);
            
			
/* Affiliated with*/

create table AffiliatedWith
						(physicianID int,
						 departmentID int,
						 primary key(physicianID,departmentID),
						 foreign key(physicianID)references Physician(physicianID)on delete cascade,
						 foreign key(departmentID)references Department(deptID)on delete cascade
						);
						
/*procedure*/

create table `procedure`
				( procID int,
				  name varchar(40),
				  cost real,
				  primary key(procID)
				);
                
                
/*patient*/

create table Patient
					(patientID int,
					ssn int,
					name varchar(40),
					address varchar(100),
					dob date,
					phone varchar(16),
					insuranceNumber int,
					primaryPhysID int,
					primary key(patientID),
					foreign key(primaryPhysID)references Physician(physicianID)on delete set null
					);
					
/*Nurse*/

create table Nurse
				(nurseID int,
				name varchar(40),
				position varchar(40),
				ssn int,
				primary key(nurseID),
				check(position in('HeadNurse','Nurse'))
				);
                
                
                /* Medication */

create table Medication
					(medID int,
					name varchar(40),
					primary key(medID)
					);
					
/* Prescribes */

create table Prescribes
					(physicianID int,
					patientID int,
					medicationID int,
					prescribedDate date,
					dose varchar(40),
					primary key(physicianID,patientID,medicationID,prescribedDate),
					foreign key(physicianID) references Physician(physicianID)on delete cascade,
					foreign key(patientID) references Patient(patientID)on delete cascade,
					foreign key(medicationID) references Medication(medID)on delete cascade
					);
                    
                    /*Room */

create table Room
				(roomID int,
				 roomType varchar(40),
				 primary key(roomID),
				 check(roomType in('Single','Double'))
				);
				
				
/*Stay*/

create table Stay
				(stayID int,
				patientID int,
				roomID int,
				startDate date,
				endDate date,
				primary key(stayID),
				foreign key(patientID)references Patient(patientID)on delete set null,
				foreign key(roomID) references Room(roomID)on delete set null
				);
                
                
                				
/*Undergoes */

create table Undergoes
					(patientID int,
					procedureID int,
					stayID int,
					procDate date,
					physicianID int,
					nurseID int,
					primary key (patientID,procedureID,stayID,procDate),
					foreign key(patientID) references Patient(patientID)on delete cascade,
					foreign key(procedureID) references `Procedure`(procID)on delete cascade ,
					foreign key(stayID) references Stay(stayID)on delete cascade,
					foreign key(physicianID)references Physician(physicianID)on delete cascade,
					foreign key(nurseID)references Nurse(nurseID)on delete cascade
					);
					
/*on call*/

create table OnCall
					(nurseID int,
					startDate date,
					endDate date,
					primary key(nurseID,startDate,endDate),
					foreign key(nurseID)references Nurse(nurseID)on delete cascade
					);

/* Appointment */

create table Appointment
					(appID int,
					patientID int,
					nurseID int,
					physicianID int,
					startDateTime datetime,
					endDateTime datetime,
					primary key(appID),
					foreign key(patientID) references Patient(patientID)on delete set null,
					foreign key(nurseID)references Nurse(nurseID)on delete set null,
					foreign key(physicianID)references Physician(physicianID)on delete set null
					);