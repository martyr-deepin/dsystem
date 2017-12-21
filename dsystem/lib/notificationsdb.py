#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

class NotificationsDB:
    def __init__(self, dbPath):
        self.conn = sqlite3.connect(dbPath)

    def rowcount(self):
        cursor = self.conn.execute('select count(*) from notifications;')
        counttuple = cursor.fetchone()
        return int(counttuple[0])

    def deleteAll(self):
        cursor = self.conn.execute('delete from notifications;')
        self.conn.commit()
        return True

    def selectAll(self):
        '''
        CREATE TABLE notifications(ID TEXT PRIMARY KEY,Icon TEXT,Summary
        TEXT,Body TEXT,AppName TEXT,CTime TEXT)
        '''
        cursor = self.conn.execute('select * from notifications;')
        return cursor
