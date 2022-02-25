create table continents
(
    id       int unsigned auto_increment comment '自增id'
        primary key,
    chn_name varchar(32) null comment '中文名',
    eng_name varchar(32) null comment '英文名'
);

INSERT INTO continents (id, chn_name, eng_name) VALUES (1, '亚洲', 'Asia');
INSERT INTO continents (id, chn_name, eng_name) VALUES (2, '欧洲', 'Europe');
INSERT INTO continents (id, chn_name, eng_name) VALUES (3, '非洲', 'Africa');
INSERT INTO continents (id, chn_name, eng_name) VALUES (4, '大洋洲', 'Oceania');
INSERT INTO continents (id, chn_name, eng_name) VALUES (5, '南极洲', 'Antarctica');
INSERT INTO continents (id, chn_name, eng_name) VALUES (6, '北美洲', 'North America');
INSERT INTO continents (id, chn_name, eng_name) VALUES (7, '南美洲', 'South America');