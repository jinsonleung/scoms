create table enterprise
(
    id                         smallint auto_increment
        primary key,
    enterprise_level           varchar(64)  null,
    account                    varchar(16)  not null,
    full_name                  varchar(64)  not null,
    abbreviation_name          varchar(32)  null,
    enterprise_type            varchar(32)  not null,
    architecture               varchar(64)  not null,
    unified_social_credit_code varchar(32)  null,
    registered_capital         varchar(32)  null,
    established_date           datetime(6)  null,
    effective_start_date       datetime(6)  null,
    effective_end_date         datetime(6)  null,
    address                    varchar(128) null,
    city                       varchar(32)  null,
    industry                   varchar(32)  null,
    website                    varchar(64)  null,
    legal_person_name          varchar(16)  null,
    legal_person_email         varchar(64)  null,
    contact_name               varchar(32)  null,
    contact_tel                varchar(32)  null,
    contact_phone              varchar(32)  null,
    contact_email              varchar(64)  null,
    business_scope             longtext     null,
    remark                     longtext     null,
    is_available               tinyint(1)   not null,
    is_delete                  tinyint(1)   not null,
    create_datetime            datetime(6)  not null,
    create_by                  varchar(32)  not null,
    update_datetime            datetime(6)  not null,
    update_by                  varchar(32)  not null,
    constraint account
        unique (account)
);

INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES (null, '1001', '赛诚国际物流有限公司', '赛诚国际', '外商投资企业', '总公司', '91310000717853668T', '人民币500.0000万', '2005-01-05 00:00:00', '2005-01-05 00:00:00', '2025-01-04 14:15:50', '上海市静安区武定路458号洪安大厦9楼', '上海市 / 市辖区 / 静安区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, '国际流通物流业务', null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1002', '深圳市前海赛诚物流有限公司', '深圳赛诚', '外商投资企业', '子公司', '91310000717853668T-1', '人民币200.0000万', '2005-01-05 00:00:00', '2005-01-05 00:00:00', '2025-01-04 14:15:50', '深圳市南山区深南大道与前海路交汇处振业国际商务中心11层1101-1102室', '广东省 / 深圳市 / 南山区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, '国际流通物流业务', null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1003', '河南赛诚进出口贸易有限公司', '河南赛诚', '外商投资企业', '子公司', '91310000717853668T-2', '人民币300.0000万', '2005-01-05 00:00:00', '2005-01-05 00:00:00', '2025-01-04 14:15:50', '河南省郑州市经济技术开发区航海东路1346号国安大厦B座3层310室', '河南省 / 郑州市 / 郑州经济技术开发区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, '国际流通物流业务', null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1004', '广州赛诚物流有限公司', '广州赛诚', '外商投资企业', '子公司', '91310000717853668T-3', '人民币300.0000万', '2005-01-05 00:00:00', '2005-01-05 00:00:00', '2025-01-04 14:15:50', '广州市南沙区龙穴岛保税物流园4号仓库南1-8单元', '河南省 / 郑州市 / 郑州经济技术开发区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, '国际流通物流业务', null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1005', '赛诚国际物流(杭州）有限公司', '杭州赛诚', '外商投资企业', '子公司', '91310000717853668T-4', '人民币300.0000万', '2005-01-05 00:00:00', null, null, '杭州市江干区下沙出口加工区（内）14号大街506号1-2库房', '上海市 / 市辖区 / 静安区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, '国际流通物流业务', null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1006', '北京办事处', '北京办事处', '其他', '其他', null, null, null, null, null, '北京市顺义区南法信旭辉空港中心2-325室', '北京市 / 市辖区 / 顺义区', null, null, null, null, null, null, null, null, null, null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1007', '乌鲁木齐办事处', '乌鲁木齐办事处', '其他', '其他', null, null, null, null, null, '新疆乌鲁木齐市开发区中亚南路111号', '新疆维吾尔自治区 / 乌鲁木齐市 / 新市区', '物流运输', 'http://www.saichenglogistics.com/', '陈清', null, null, null, null, null, null, null, 1, 1, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');
INSERT INTO scomsdb.enterprise (enterprise_level, account, full_name, abbreviation_name, enterprise_type, architecture, unified_social_credit_code, registered_capital, established_date, effective_start_date, effective_end_date, address, city, industry, website, legal_person_name, legal_person_email, contact_name, contact_tel, contact_phone, contact_email, business_scope, remark, is_available, is_delete, create_datetime, create_by, update_datetime, update_by) VALUES ('赛诚国际物流有限公司', '1008', 'AAA办事处', 'AAA办事处', '其他', '其他', null, null, null, null, null, '海南省海口市天涯海角888号', '海南省 / 海口市 / 龙华区', '物流运输', 'http://www.lcw-lg.com/', '张三', null, null, null, null, null, null, null, 1, 0, '2022-01-18 14:18:31', 'admin', '2022-01-18 14:18:48', 'admin');