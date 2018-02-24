#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database.init.DbInitializer import DbInitializer
import os.path
import setting.Setting

# ユーザ単位DB（※AccountsDBの初期化後であること（DatabaseMetaの呼出順に注意））
# DbInitializerとの違いは、ユーザ単位のDBをdictで持つこと。
# * DbFileName = {f'{user}': f'GitHub.{DbId}.{user}.sqlite3', ... }
# * DbFilePath = {f'{user}': os.path.join(setting.DbPath, DbFileName[f'{user}']), ... }
# * Db         = {f'{user}': dataset.connect('sqlite:///' + self.__filepaths[f'{user}']), ...}
class DbInitializerByMultiUsers(DbInitializer):
    def __init__(self):
        super().__init__()
        self.__filenames = {}
        self.__CreateFilenames()
        self.__filepaths = {}
        self.__CreateFilepath()
        self.__dbs = {}

    def CreateDb(self):
        for username in self.DbFileName:
            if not os.path.isfile(self.DbFilePath):
                with open(self.DbFilePath, 'w') as f: pass

    def ConnectDb(self):
        for username in self.DbFileName:
            self.__dbs[username] = dataset.connect('sqlite:///' + self.__filepaths[username])

    @property
    def DbFileName(self): return self.__filenames
    @property
    def DbFilePath(self): return self.__filepaths
    @property
    def Db(self): return self.__dbs

    def __CreateFilepath(self):
        import setting.Setting
        setting = setting.Setting.Setting()
        for username in self.__GetUsernames():
            self.__filepaths[username] = os.path.join(setting.DbPath, self.__filenames[username])

    def __CreateFilenames(self):
        for username in self.__GetUsernames():
            self.__filenames[username] = 'GitHub.{0}.{1}.sqlite3'.format(self.DbId, username)

    def __GetUsernames(self):
        for username in Db().Accounts['Accounts'].find()['Username']: yield username
        
