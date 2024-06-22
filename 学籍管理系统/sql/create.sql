create table Department(
	did int Primary Key,
    dname varchar(100) not null
);

create table pro(
	pid int Primary Key,
    pname varchar(100) not null,
    did int not null,
    Foreign key(did) references Department(did)
);

create table class(
	cid int Primary Key,
    cname varchar(100) not null,
    num int not null default 0,
    pid int not null,
    Foreign Key(pid) references pro(pid)
);

create table student(
	sid int Primary Key,
    sname varchar(100) not null,
    sex varchar(10) not null,
    birth date,
    entry date,
    cid int not null,
    Foreign Key(cid) references class(cid)
);

create table course(
	csid int Primary Key,
    csname varchar(100) not null,
    cstime int default 0,
    credit int default 0
);

create table rewards_punishment(
	rpid int Primary Key,
    sid int not null,
    rpname varchar(100) not null,
    rpperiod varchar(100) not null,
    Foreign Key(sid) references student(sid)
);

create table achievement(
	sid int not null,
    csid int not null,
    score int not null,
    Primary key(sid, csid),
    Foreign key(sid) references student(sid),
    Foreign key(csid) references course(csid)
);

create table login(
	username varchar(100) Primary Key,
    pwd varchar(100) not null default "123456",
    avatar_path varchar(100) 
);