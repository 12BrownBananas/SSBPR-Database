CREATE DEFINER=`root`@`localhost` PROCEDURE `rankCharUsage`()
BEGIN
	select cname, count(*) from (select p1_cname as cname from tournament_set union all select p2_cname as cname from tournament_set) as t1 group by cname order by count(*) desc;
END