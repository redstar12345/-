delimiter //
drop trigger if exists delete_student //
create trigger delete_student after delete on student for each row
begin
	update class set class.num = class.num - 1 where class.cid = old.cid;
end //
delimiter ;

delimiter //
drop trigger if exists insert_student //
create trigger insert_student after insert on student for each row
begin
	update class set class.num = class.num + 1 where class.cid = new.cid;
end //
delimiter ;

delimiter //
drop trigger if exists update_student //
create trigger update_student after update on student for each row
begin
	update class set class.num = class.num - 1 where class.cid = old.cid;
    update class set class.num = class.num + 1 where class.cid = new.cid;
end //
delimiter ;