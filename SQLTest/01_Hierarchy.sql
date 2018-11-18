/* define boss/dept header for id/parent_id/dept name/boss name table*/
create or replace function boss_dept( level positive, boss char, dept char ) return varchar2 as l_data varchar2(100);
begin
    l_data := ' - ' || boss || chr(10) ;
    l_data := l_data || lpad('   ', level + 2)  || dept;
    return l_data ;
end;

/* define employee list */
create or replace function emp_list(level positive, dept positive ) return varchar2 as l_data varchar2(1000);
begin
    l_data := chr(10);
    for x in ( select name from employee where dep_id = dept )
        loop
            l_data := l_data || lpad('   ', level + 2) || x.name || chr(10);
        end loop;
    return l_data ;
end;

/* run Hierarchy */
select lpad('   ', level) || boss_dept(level, boss, name) || emp_list(level + 2, id) as Hierarchy from department
    start with id = 0
    connect by nocycle prior id = parent_id;

