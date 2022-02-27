create table continent
(
    id              bigint auto_increment
        primary key,
    eng_name        varchar(128) null,
    chn_name        varchar(128) null,
    description     longtext     null,
    is_delete       tinyint(1)   not null,
    create_datetime datetime(6)  not null,
    create_by       varchar(32)  not null,
    update_datetime datetime(6)  not null,
    update_by       varchar(32)  not null
);

create index continent_create_datetime_4929139b
    on continent (create_datetime);

create index continent_update_datetime_c46436a9
    on continent (update_datetime);

INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (1, 'Asia', '亚洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (2, 'Europe', '欧洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (3, 'Africa', '非洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (4, 'Oceania', '大洋洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (5, 'Antarctica', '南极洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (6, 'North America', '北美洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');
INSERT INTO scomsdb.continent (id, eng_name, chn_name, description, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (7, 'South America', '南美洲', null, 0, '2021-01-18 18:18:18', 'admin', '2022-02-25 15:40:59', 'admin');