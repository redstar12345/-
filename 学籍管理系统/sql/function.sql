Delimiter //
drop function if exists func//
create function func(id int)
returns float
reads sql data
begin
		declare state int default 0;
		declare grade, sum, result, num float default 0;
		declare sc cursor for (select score from achievement where achievement.csid = id);
        declare continue handler for not found set state = 1;
        open sc;
        repeat
			fetch sc into grade;
			if state = 0 then
				set sum = sum + grade;
                set num = num + 1;
			end if;
            until state = 1
		end repeat;
        close sc;
        if num != 0 then
			set result = sum/num;
		end if;
        return result;
end //
Delimiter ;

select csid, func(csid) as average from course