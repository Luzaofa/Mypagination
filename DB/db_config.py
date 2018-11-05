__author__ = 'Luzaofa'
__date__ = '2018/9/12 19:57'

import random
import sqlite3


class DB_helper(object):

    def __init__(self):

        self.conn = sqlite3.connect('E:/LuzaofaPage/Mydissertation.db')

        self.cursor = self.conn.cursor()

    def commit_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            # print(e)
            self.conn.rollback()         # 数据回滚，若一个插入失败都不做插入

    # def create_table(self):
    #     sql = """
    #         create table Mydissertation_taoguba(
    #         Title CHAR(100),
    #         Author CHAR(20),
    #         Skim INT,
    #         Talk INT,
    #         Time DATE,
    #         Content TEXT
    #         )"""
    #     self.commit_sql(sql)


    def select_title(self):
        sql = """
            select Title, Author, Skim, Talk
            from Mydissertation_taoguba
            """
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        value = []
        for i in values:
            value.append(i)
        return value


