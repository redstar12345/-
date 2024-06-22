Delimiter //
drop procedure if exists Update_Department //
create procedure Update_Department(in old_did int, in new_did int)
begin
		declare state int default 0;
        declare Error_code int default 0;
        declare Temp char(8);
        declare continue handler for not found set Error_code = 1;
        start transaction;
        set SQL_SAFE_UPDATES = 0;
        select did
        from Department
        where did = old_did into Temp;
			set FOREIGN_KEY_CHECKS = 0;
            update Department set did = new_did
            where did = old_did;
            update pro set did = new_did
            where did = old_did;
            set FOREIGN_KEY_CHECKS = 1;
		set SQL_SAFE_UPDATES = 1;
		if Error_code = 0 then
			set state = 0;
            commit;
		else
			set state = 1;
			rollback;
		end if;
end //
Delimiter ;

Delimiter //
drop procedure if exists Update_pro //
create procedure Update_pro(in old_pid int, in new_pid int)
begin
		declare state int default 0;
		declare Error_code int default 0;
        declare Temp char(8);
        declare continue handler for not found set Error_code = 1;
        start transaction;
        set SQL_SAFE_UPDATES = 0;
        select pid
        from pro
        where pid = old_pid into Temp;
			set FOREIGN_KEY_CHECKS = 0;
            update pro set pid = new_pid
            where pid = old_pid;
            update class set pid = new_pid
            where pid = old_pid;
            set FOREIGN_KEY_CHECKS = 1;
		set SQL_SAFE_UPDATES = 1;
		if Error_code = 0 then
			set state = 0;
            commit;
		else
			set state = 1;
			rollback;
		end if;
end //
Delimiter ;

Delimiter //
drop procedure if exists Update_class //
create procedure Update_class(in old_cid int, in new_cid int)
begin
		declare state int default 0;
		declare Error_code int default 0;
        declare Temp char(8);
        declare continue handler for not found set Error_code = 1;
        start transaction;
        set SQL_SAFE_UPDATES = 0;
        select cid
        from class
        where cid = old_cid into Temp;
			set FOREIGN_KEY_CHECKS = 0;
            update class set cid = new_cid
            where cid = old_cid;
            update student set cid = new_cid
            where cid = old_cid;
            set FOREIGN_KEY_CHECKS = 1;
		set SQL_SAFE_UPDATES = 1;
		if Error_code = 0 then
			set state = 0;
            commit;
		else
			set state = 1;
			rollback;
		end if;
end //
Delimiter ;

Delimiter //
drop procedure if exists Update_student //
create procedure Update_student(in old_sid int, in new_sid int)
begin
		declare state int default 0;
		declare Error_code int default 0;
        declare Temp char(8);
        declare continue handler for not found set Error_code = 1;
        start transaction;
        set SQL_SAFE_UPDATES = 0;
        select sid
        from student
        where sid = old_sid into Temp;
			set FOREIGN_KEY_CHECKS = 0;
            update student set sid = new_sid
            where sid = old_sid;
            update rewards_punishment set sid = new_sid
            where sid = old_sid;
            update achievement set sid = new_sid
            where sid = old_sid;
            set FOREIGN_KEY_CHECKS = 1;
		set SQL_SAFE_UPDATES = 1;
		if Error_code = 0 then
			set state = 0;
            commit;
		else
			set state = 1;
			rollback;
		end if;
end //
Delimiter ;

Delimiter //
drop procedure if exists Update_course //
create procedure Update_course(in old_csid int, in new_csid int)
begin
		declare state int default 0;
		declare Error_code int default 0;
        declare Temp char(8);
        declare continue handler for not found set Error_code = 1;
        start transaction;
        set SQL_SAFE_UPDATES = 0;
        select csid
        from course
        where csid = old_csid into Temp;
			set FOREIGN_KEY_CHECKS = 0;
            update course set csid = new_csid
            where csid = old_csid;
            update achievement set csid = new_csid
            where csid = old_csid;
            set FOREIGN_KEY_CHECKS = 1;
		set SQL_SAFE_UPDATES = 1;
		if Error_code = 0 then
			set state = 0;
            commit;
		else
			set state = 1;
			rollback;
		end if;
end //
Delimiter ;