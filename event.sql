/*
创建临时表空间
*/
delimiter //
create procedure create_temp()
begin
  drop table if exists temp_affair;
  create temporary table temp_affair(`uid` BIGINT(20),`uname` VARCHAR(255));
  #insert into temp_affair(uid) select EntityInternalID from security_principal where EntityInternalID !=-1;
  insert into temp_affair(uid,uname) select security_principal.EntityInternalID,v3x_org_member.name from security_principal,v3x_org_member
          where v3x_org_member.id = security_principal.EntityInternalID;
end//

/*
创建插入提醒数据过程
*/

delimiter //
create procedure notify_birthday()
begin
  declare aid BIGINT(20);
  declare uid BIGINT(20);
  declare uname VARCHAR(120);
  declare senderId BIGINT(20) default '-884316703172445';
  declare bSubject VARCHAR(1000);
  declare bname VARCHAR(120);
  declare Done INT DEFAULT 0;
  declare affairId BIGINT(20);
  declare rs cursor for select * from temp_affair;
  declare continue handler FOR SQLSTATE '02000' SET Done = 1;
  select name from v3x_org_member where MONTH(birthday)=MONTH(CurDATE()) AND DAY(birthday)=DAY(CurDATE()) into bname;
  select unix_timestamp() into affairId;
  set bSubject = CONCAT(bname,"生日提醒");
  if (select bname)is not null then
    open rs;
    fetch next from rs into uid,uname;
    repeat
    if (select bname)is not null then
      set aid = uid + affairId;
#insert into 'v3x_affair' set 'id'=uid,'member_id'=uid,'sender_id'=senderId,'app'=1,'subject'=bSubject,state=2;
insert into v3x_affair(id,member_id,sender_id,subject,app,state) select aid,uid,senderId,bSubject,1,2;
fetch next from rs into uid,uname;
    end if;
    until Done end repeat;
    close rs;
end if;
end;//


/*
创建生日提醒时间
*/
CREATE EVENT `notify_birthday` ON SCHEDULE
EVERY 1 DAY
ON COMPLETION NOT PRESERVE
ENABLE
COMMENT 'notify_birthday'
DO BEGIN
  call create_temp();
  call notify_birthday();
END

