use task;
show tables;

#1. Write a query to fetch the EmpFname from the EmployeeInfo table in the upper case and use the ALIAS name as EmpName.
select upper(EmpFname) EmpName from employeeinfo;

#2. Write a query to fetch the number of employees working in the department ‘HR’.
select * from employeeinfo where Department = 'HR';

#3. Write a query to get the current date.
select current_date();

#4. Write a query to retrieve the first four characters of EmpLname from the EmployeeInfo table.
select substring(EmpLname,1,4) from Employeeinfo;

#5. Write a query to fetch only the place name(string before brackets) from the Address column of EmployeeInfo table.
select substring_index(Address,'(',1) from employeeinfo;

#6. Write a query to create a new table that consists of data and structure copied from the other table.
create table CopyEmployeeinfo(select * from Employeeinfo);
select * from CopyEmployeeinfo;

#7. Write q query to find all the employees whose salary is between 50000 to 100000.
select * from Employeeinfo i join eposition e on i.empid=e.empid where salary between 50000 and 100000; 

#8. Write a query to find the names of employees that begin with ‘S’
select EmpFname from Employeeinfo where EmpFname like 'S%';

#9. Write a query to fetch top N records.
select * from employeeinfo i join eposition p on i.empid=p.empid order by salary desc limit 1;

#10. Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”. The first name and the last name must be separated with space.
select concat(EmpFname,' ',EmpLname) as FullName from employeeinfo;
select concat_ws(' ',EmpFname,EmpLname) from employeeinfo;



 