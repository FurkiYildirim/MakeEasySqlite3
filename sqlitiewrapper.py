"""
Created By: ! Kontragerilla ღ ヅ#1019 and Ouburursel#4098
github ! Kontragerilla ღ ヅ#1019: https://github.com/FurkiYildirim
github Ouburursel#4098 :  https://github.com/darkmechanism
"""

from sqlite3 import connect
from datetime import datetime


class Log:
    def __init__(self, filename):
        self.__filename = open(filename, "a")

    def plog(self, log):
        date = f'[{datetime.now().year}-{datetime.now().month}-{datetime.now().day}  {datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}]'
        self.__filename.write(date + " " + log + "\n")


class DbWrapper:
    def __init__(self, filename, log="log.txt"):
        self.__filename = filename
        self.__logfile = Log(log)

    def ShapeTable(self, paramarr: list, tablename):
        DbOverseer = connect(self.__filename)
        DbCursor = DbOverseer.cursor()
        DbCursor.execute(f"CREATE TABLE {tablename} ({', '.join(paramarr)})")
        DbOverseer.commit()
        DbOverseer.close()
        self.__logfile.plog(f"{self.__filename}: Created table {tablename} with variables {paramarr}.")

    def AppendLine(self, paramarr, tablename):
        DbOverseer = connect(self.__filename)
        DbCursor = DbOverseer.cursor()
        temp = [f"'{i}'" for i in paramarr]
        DbCursor.execute(f"INSERT INTO {tablename} VALUES ({', '.join(temp)})")
        DbOverseer.commit()
        DbOverseer.close()
        self.__logfile.plog(f"{self.__filename}: Appended line to table {tablename} with variables {paramarr}.")

    def GetTable(self, tablename):
        DbOverseer = connect(self.__filename)
        DbCursor = DbOverseer.cursor()
        DbCursor.execute(f"SELECT * FROM {tablename}")
        LineInfo = DbCursor.fetchall()
        DbOverseer.commit()
        DbOverseer.close()
        self.__logfile.plog(f"{self.__filename}: Requested table {tablename}.")
        return LineInfo
    def update_raw(self, tableName, valueThatChange, point, newValue, findBy):
        DbOverseer = connect(self.__filename)
        DbCursor = DbOverseer.cursor()
        DbCursor.execute(f"UPDATE {tableName} SET {valueThatChange} = '{newValue}' WHERE {findBy} = '{point}'")
        DbOverseer.commit()
        DbOverseer.close()
        self.__logfile.plog(f"{self.__filename}: Updated value {newValue}.")

    def DeleteTable(self, tablename):
        DbOverseer = connect(self.__filename)
        DbCursor = DbOverseer.cursor()
        DbCursor.execute(f"DROP TABLE IF EXISTS {tablename}")
        DbOverseer.commit()
        DbOverseer.close()
        self.__logfile.plog(f"{self.__filename}: Deleted table {tablename}.")


if __name__ == '__main__':
    fileName = "database.db"
    logF = "log.txt"

    db = DbWrapper(filename=fileName, log=logF)
    db.ShapeTable(['uid', 'username', 'password','access'], 'user')
    # # db.ShapeTable(['uid', 'username', 'password', 'email'], 'users')
    # db.DeleteTable('Authcode')
    #db.DeleteTable('user')