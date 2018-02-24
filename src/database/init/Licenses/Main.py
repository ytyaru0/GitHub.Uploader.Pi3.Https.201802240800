#!python3
#encoding:utf-8
import os.path
import shlex
import subprocess
import database.license.insert.Main
import database.TsvLoader
class Main:
    def __init__(self, db, client):
        self.__db = db
        self.__client = client
        self.__path_dir_this = os.path.abspath(os.path.dirname(__file__))

    def Create(self):
        path_sh = os.path.join(self.__path_dir_this, 'create/Create.sh')
        print(path_sh)
        print(self.__db.Paths['license'])
        subprocess.call(shlex.split("bash \"{0}\" \"{1}\"".format(path_sh, self.__db.Paths['license'])))
        
        name_table = 'Gnu'
        tsv = database.TsvLoader.TsvLoader()
        tsv.ToSqlite3(os.path.join(self.__path_dir_this, 'create/{0}.Insert.tsv'.format(name_table)), self.__db.Paths['license'], name_table)
    def Insert(self):
        inserter = database.license.insert.Main.Main(self.__db, self.__client)
        inserter.Initialize()
        
    def Cui(self):
        license_key = 'start'
        while '' != license_key:
            print('入力したKeyのライセンスを問い合わせます。(未入力+Enterで終了)')
            print('サブコマンド    l:既存リポジトリ m:一覧更新  f:ファイルから1件ずつ挿入')
            key = input()
            if '' == key:
                break
            elif 'l' == key or 'L' == key:
                self.licenses.Show()
            elif 'f' == key or 'F' == key:
                self.__InsertForFile()
            elif 'm' == key or 'M' == key:
                self.licenses.Update()
            else:
                self.licenses.InsertOne(key)
    """
    def __InsertForFile(self):
        file_name = 'insert/LicenseKeys.txt'
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
        if not(os.path.isfile(file_path)):
            print(file_name + 'ファイルを作成し、1行ずつキー名を書いてください。')
            return
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
                self.licenses.InsertOne(line.strip())
    """

