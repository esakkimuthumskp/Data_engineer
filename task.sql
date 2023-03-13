use task;
select * from indianprimeministers;

#task 1
select Name ,sum(Datediff(left_office,took_office)) as No_of_days from indianprimeministers group by Name;

#3 rank function
select name,count(name) from indianprimeministers group by 1;

#4 List the 3rd highest tenure(total time in office) prime minister.
select * from
(select name,sum(Datediff(left_office,took_office)) as no_of_days,
dense_rank () over (order by sum(Datediff(left_office,took_office)) desc ) as ranking
from indianprimeministers group by name) ran
where ran.ranking=3;
