/* define average department salary */
create or replace function get_avg(dept_no integer)
return number is
    dept_avg number(10,4);
begin 
    dept_avg := 0 ;
    select avg(salary) into dept_avg from employee where employee.dep_id = dept_no; 
    return dept_avg; 
end; 

select dep_id, name, salary from employee where salary > get_avg(dep_id);