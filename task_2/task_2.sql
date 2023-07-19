
show databases;
use task;
show tables;
-- Create the 1st Table

create table Employee(Empid int primary key,EmpName varchar(25),Department char(10),ContactNo int,EmailId varchar(25),EmpHeadId int);
insert into Employee values(101,"Isha","E-101",1234567890,"isha@gmail.com",105),
(102,"Priya","E-104",1234567890,"priya@yahoo.com",103),
(103,"Neha","E-101",1234567890,"neha@gmail.com",101),
(104,"Rahul","E-102",1234567890,"rahul@yahoo.com",105),
(105,"Abhishek","E-101",1234567890,"abhishek@gmail.com",102);
select * from Employee;



-- Create the 2nd Table
create table EmDept(DepId char(10) primary key,DeptName varchar(20),Dept_off varchar(20),DeptHead int,Empid int,Salary int,IsPermanent varchar(5));
insert into EmDept values("E-101","HR","MONDAY",105,101,2000,"yes"),
("E-102","Development","TUESDAY",101,102,10000,"yes"),
("E-103","HOUS KEEPING","SATURDAY",103,103,5000,"No"),
("E-104","Sales","SUNDAY",104,104,1900,"Yes"),
("E-105","Purchage","Tuesday",104,105,2300,"Yes");
select * from EmDept;



-- Create the 3rd Table
create table EmpSalary(ProjectId char(10),Duration int);
insert into EmpSalary values("P-1",23),
("P-2",15),
("P-3",45),
("P-4",2),
("P-5",30);
select * from EmpSalary;



-- Create the 4th table
create table Country(Cid char(10),cname varchar(10));
insert into Country values("Cl-1","India"),
("Cl-2","USA"),
("Cl-3","china"),
("Cl-4","Pakistan"),
("cl-5","Russia");
select * from Country;


-- Create the 5th table
create table ClientTable(ClientId char(5),ClientName varchar(20),cid char(5));
insert into ClientTable values("cl-1","ABC Group","C-1"),
("cl-2","PQR","C-1"),
("cl-3","XYZ","C-2"),
("cl-4","tech altum","C-3"),
("cl-5","mnp","C-5");
select * from ClientTable;



-- Create 6th table
create table EmpProject(EmpId int,projectId char(10),ClientID char(5),StartYear int, EndYear int);
insert into EmpProject values(101,"p-1","Cl-1",2010,2010),
(102,"p-2","Cl-2",2010,2012),
(103,"p-1","Cl-3",2013,null),
(104,"p-4","Cl-1",2014,2015),
(105,"p-4","Cl-5",2015,null);
select * from EmpProject;



-- Query1 Select the detail of the employee whose name start with P.
select * from Employee where EmpName like"P%";

-- Query2 How many permanent candidate take salary more than 5000.
select * from EmDept where salary>=5000 and IsPermanent="yes";

-- Query3 Select the detail of employee whose emailId is in gmail.
select * from Employee where EmailId like"%gmail.com";

-- Query4  Select the details of the employee who work either for department E-104 or E-102.
select * from Employee where Department="E-102" or Department="E-104";

-- Query5  What is the department name for DeptID E-102?
select DepId,DeptName from EmDept where DepId="E-102";

-- Query6 What is total salarythat is paid to permanent employees?
select sum(salary) from EmDept where IsPermanent="yes";

-- Query7 List name of all employees whose name ends with a.
select * from Employee where EmpName like "%a";

-- Query8 List the number of department of employees in each project.
select count(*),Department from Employee  group by (Department);

-- Query9 How many project started in year 2010.
select EmpId, projectId, ClientID, StartYear from EmpProject where StartYear=2010;

-- Query10 How many project started and finished in the same year.
select count(*) from EmpProject where StartYear=EndYear;

-- Query11 select the name of the employee whose name's 3rd charactor is 'h'.
select * from Employee where EmpName like "__h%";

-- Query12 Select the department name of the company which is assigned to the employee whose employee id is grater 103.
select * from Employee where Empid>103;

-- Query13 Select the name of the employee who is working under Abhishek.
select * from Employee where EmpName ="Abhishek";

-- Query14 Select the employee whose department off is monday
select * from EmDept where Dept_off="MONDAY";

-- Query15 select the indian client details.
select ClientTable.ClientId,ClientTable.ClientName,Country.cid,Country.cname  from ClientTable left join Country on ClientTable.cid=Country.cid where cname="India";



 

