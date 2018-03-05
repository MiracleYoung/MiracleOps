#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/5/18 9:46 AM
# @Author  : Miracle Young
# @File    : init_data.py

import pymysql, uuid, datetime

conn_str = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'MiracleOps',
    'charset': 'utf8mb4'
}

conn = pymysql.connect(**conn_str)
with conn.cursor() as cursor:
    print('role init starting...')
    init_role_sql = '''
        insert into role (`name`, `c_time`) values ('{}', '{}');
        insert into role (`name`, `c_time`) values ('{}', '{}');
        insert into role (`name`, `c_time`) values ('{}', '{}');
        insert into role (`name`, `c_time`) values ('{}', '{}');
    '''.format('Anonymous', datetime.datetime.now(), 'Normal', datetime.datetime.now(), 'Admin',
               datetime.datetime.now(), 'UnVerified', datetime.datetime.now())
    cursor.execute(init_role_sql)
    conn.commit()
    print('role init completed.')
conn.close()
