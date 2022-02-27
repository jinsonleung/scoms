create table continent
(
    id          int unsigned auto_increment comment '自增id'
        primary key,
    eng_name    varchar(32)  null comment '英文名',
    chn_name    varchar(32)  null comment '中文名',
    description varchar(128) null
);

INSERT INTO continent (id, eng_name, chn_name, description) VALUES (1, 'Asia', '亚洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (2, 'Europe', '欧洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (3, 'Africa', '非洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (4, 'Oceania', '大洋洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (5, 'Antarctica', '南极洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (6, 'North America', '北美洲', null);
INSERT INTO continent (id, eng_name, chn_name, description) VALUES (7, 'South America', '南美洲', null);