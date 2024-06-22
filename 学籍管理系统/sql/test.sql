insert into student(sid, sname, sex, birth, entry, cid)
values
('7', '吴丙', '女', '2002-04-19', '2022-09-01', '4'),
('25', '张六', '男', '2003-04-13', '2021-09-01', '1');

delete from student where sid = 25;

select * from student left join class on student.cid = class.cid where student.sid = 15;

select class.cid, class.cname, class.num, pro.pname from class left join pro on class.pid = pro.pid limit 8 offset 0;

select * from rewards_punishment;

select * from rewards_punishment limit 8 offset 0;

insert into pro(pid, pname, did)
values
('9', '能源工程', '3');

insert into login(username, pwd)
values
('Dth', '123456');


select student.sid, student.sname, student.sex, student.birth, student.entry, class.cname 
from student left join class
on student.cid = class.cid;


select student.sid, student.sname, student.sex, student.birth, student.entry, class.cname
from student left join class
on student.cid = class.cid
where class.cname = '%智能%';

select class.cid, class.cname, class.num, pro.pname
from class left join pro
on class.pid = pro.pid
where class.cid = 1;

select class.cid, class.cname, class.num, pro.pname from class left join pro on class.pid = pro.pid where class.cid=5;

select course.csid, course.csname, course.cstime, course.credit
from course;

select course.csid, course.csname, course.cstime, course.credit from course where course.csid=5;

select pro.pid, pro.pname, Department.dname
from pro left join Department
on pro.did = Department.did;

select achievement.sid, course.csname, achievement.score
from achievement left join course
on achievement.csid = course.csid
limit 8 offset 0;

select * from class where cname = '软件工程1班';

select achievement.sid, student.sname, achievement.csid, course.csname, achievement.score
from achievement, student, course
where achievement.sid = student.sid and achievement.csid = course.csid  and achievement.sid=2;

insert into class(cid, cname, num, pid)
values
(15, '大数据10班', 0, 1);

insert into pro(pid, pname, did)
values
('16', '软件工程2', '1');

insert into Department(did, dname)
values
('4', '计算机科学与技术系2');

insert into course(csid, csname, cstime, credit)
values
('100', '数据库2', '80', '4');

insert into rewards_punishment(rpid, sid, rpname, rpperiod)
values
('4', '4', '成绩优异', '奖学金');

insert into achievement(sid, csid, score)
values
('10', '5', '99');