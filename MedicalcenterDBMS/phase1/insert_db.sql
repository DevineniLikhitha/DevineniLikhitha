use laspalmasmedicalcenter;

set sql_safe_updates=0;


delete from Appointment;
delete from OnCall;
delete from Undergoes;
delete from Stay;
delete from Room;
delete from Prescribes;
delete from Medication;
delete from Nurse;
delete from Patient;
delete from `Procedure`;
delete from AffiliatedWith;
delete from Department;
delete from Physician;







insert into physician values(101,'Likhitha Devineni','Surgeon', 10919898);
insert into physician values(102,'Shravya Dharba','chiefofmedicine', 23451234);
insert into physician values(103,'MS Dhoni','Chiefofmedicine', 12323898);
insert into physician values(104,'Robert Stark','Senior', 10913454);
insert into physician values(105,'Damon Salvatore','resident', 10919898);
insert into physician values(106,'Elina Salvatore','Psychiartist', 10989898);

insert into Department values(21,'Surgery',101);
insert into Department values(22,'Psychiatry',106);
insert into Department values(23,'Generalmedicine',102);
insert into Department values(24,'GeneralMedicine',104);
insert into Department values(25,'Surgery',105);

insert into AffiliatedWith values(102,21);
insert into AffiliatedWith values(102,22);
insert into AffiliatedWith values(103,25);
insert into AffiliatedWith values(106,23);
insert into AffiliatedWith values(104,24);


insert into `procedure` values(345, 'ProcX',2343.00);
insert into `procedure` values(335, 'FirstAid',243.00);
insert into `procedure` values(125, 'ProcT',1793.00);
insert into `procedure` values(565, 'scanning',2000.00);
insert into `procedure` values(375, 'ProcI',4536.00);

insert into Patient values(256,12345678,'Ravi Ashwin','343-Blvd','1987-09-08','234-879-7890',34232,106);
insert into Patient Values(234,23223222,'Rishab Pant','764-riomale','1998-08-12','098-897-0987',23432,101);
insert into Patient Values(324,23432124,'Virat Kohli','874-SW drive','1989-04-13','093-345-1234',1232344,102);
insert into Patient values(232,12321234,'Shreya iyer','213-Iceleta','1999-06-10','980-234-1243',12345678,104);
insert into Patient values(398,32456549,'Hardik Pandya','567-Rioranche','1984-02-15','984-093-8888',23456,105);

insert into Nurse values(09,'Ross Geller','Nurse',3222232);
insert into Nurse values(19,'Chandler Bing','HeadNurse',6473822);
insert into Nurse values(22,'Rachel Green','Nurse',89342189);
insert into Nurse values(02,'Joey Tribiani','HeadNurse',87305421);
insert into Nurse values(24,'Monica Geller','Nurse',63098932);
insert into Nurse values(87,'Pheobe Buffayr','HeadNurse',09879087);


insert into Medication values(456, 'Dolo-650');
insert into Medication values(111, 'Iboprofin');
insert into Medication values(656, 'B-Complex');
insert into Medication values(993, 'Crocin');
insert into Medication values(098, 'Tylonol');

insert into Prescribes values(106,324,111,'2022-02-25','2/day');
insert into Prescribes values(102,256,993,'2022-01-25','6/day');
insert into Prescribes values(104,234,656,'2022-02-15','5/day');
insert into Prescribes values(105,398,456,'2022-02-23','2/day');
insert into Prescribes values(103,232,098,'2022-01-02','5/day');

insert into room values(32,'Single');
insert into room values(22,'Single');
insert into room values(42,'Double');
insert into room values(12,'Single');
insert into room values(62,'Double');

insert into stay values(99,234,22,'2022-01-23','2022-01-26');
insert into stay values(23,232,42,'2021-12-03','2021-12-10');
insert into stay values(56,398,32,'2022-01-08','2022-01-15');
insert into stay values(45,256,12,'2022-02-13','2022-02-26');
insert into stay values(89,324,62,'2022-01-03','2022-01-16');
insert into stay values(19,256,62,'2022-01-06','2022-01-11');
insert into stay values(100,234,62,'2021-01-06','2021-01-11');



insert into undergoes values(234,125,99,'2021-06-23',106,09);
insert into undergoes values(324,335,23,'2022-01-13',102,87);
insert into undergoes values(398,565,89,'2021-09-22',104,24);
insert into undergoes values(256,375,45,'2022-02-03',102,02);
insert into undergoes values(232,345,56,'2021-06-24',101,22);


insert into oncall values(22,'2021-07-31','2021-08-01');
insert into oncall values(24,'2022-05-11','2021-05-12');
insert into oncall values(02,'2021-04-3','2021-04-07');
insert into oncall values(87,'2022-07-12','2021-08-01');
insert into oncall values(22,'2021-03-21','2021-04-01');


insert into Appointment values(21,234,2,105,'2021-12-09 2:00','2021-12-09 2:15');
insert into Appointment values(34,256,87,104,'2022-01-10 10:15','2022-01-10 10:30');
insert into Appointment values(87,398,24,105,'2021-04-12 5:30','2021-04-12 5:50');
insert into Appointment values(11,324,22,101,'2021-06-21 3:00','2021-06-21 3:30');
insert into Appointment values(45,232,09,102, '2022-09-12 4:00','2022-09-12 4:30');



