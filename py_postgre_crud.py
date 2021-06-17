import psycopg2 as ps
from psycopg2 import sql,extensions
import sys

from psycopg2 import extensions
import psycopg2

connection = ps.connect(  
    database = "araba",  
    user = "postgres",
    password = "1234",
    host = "localhost",
    port = "5432",
)


cursor = connection.cursor()

autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
connection.set_isolation_level(autocommit)

def createDB(dbName):
    try:

        global connection
        global cursor
        create_db = "Create Database " + dbName
        cursor.execute(create_db)
        connection.commit()
        print("Veritabanı başarılı ile oluşturuldu.")
    
    except(Exception, ps.Error) as error:

        print("Veritabanı oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")


def createTable():
    try:
        global connection
        global cursor
        create_table = "Create Table araba(id integer primary key, marka Varchar(120), model Varchar(120), modelYil Varchar(120), fiyat Varchar(120))"
        cursor.execute(create_table)
        print("Tablo Başarıyla oluşturulmuştur.")
    
    except(Exception, ps.Error) as error:

        print("Tablo oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")


def insertTable(id, marka, model, modelYil, fiyat):

    try:
        global connection
        global cursor
        insert_table = "Insert into araba (id, marka, model, modelYil, fiyat) Values(%s,%s,%s,%s,%s)"
        inserted_values = (id, marka, model, modelYil, fiyat)
        cursor.execute(insert_table,inserted_values)       
        count = cursor.rowcount
        print(count, " kayıt tabloyu eklenmiştir.")
    
    except(Exception, ps.Error) as error:

        print("Tablo oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")

def selectTable():

    try:
        global connection
        global cursor

        select_query = "Select * from araba"
        cursor.execute(select_query) 
        arabalar = cursor.fetchall()
        for i in arabalar:
            print(i)

        count = cursor.rowcount        
        print(count, "Kayıt bulunmaktadır.")
    
    except(Exception, ps.Error) as error:

        print("Tablo oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")

def updateTable(id,fiyat):
    try:
        global connection
        global cursor

        update_query = "Update araba Set fiyat = %s Where id = %s"
        cursor.execute(update_query,(fiyat,id))
          
        count = cursor.rowcount
        print(count, " kayıt güncellenmiştir.")
    
    except(Exception, ps.Error) as error:

        print("Tablo oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")

def deleteTable(id):

    try:
        global connection
        global cursor

        delete_query = "Delete From araba where id = {}".format(id)
        cursor.execute(delete_query)
                  
        count = cursor.rowcount
        print(count, " kayıt başarıyla silinmiştir.")
    
    except(Exception, ps.Error) as error:

        print("Tablo oluştururken hata ! ", error)
        connection = None

    finally:

        if connection != None:
            cursor.close()
            connection.close()
            print("Veri tabanı kapatılmıştır.")


def menu():
    print("***************************")   
    print("1. Kayıtları Listele")
    print("2.Yeni veri ekle")
    print("3.Kayıt Güncelle")
    print("4.Kayıt Silme")
    print("5.Çıkış")

def main():
    while True:
        menu()
        secim = input("Seçim Yapın : ")
        if secim == "1":
            selectTable()
        elif secim == "2":
            id = input("ID : ")
            marka = input("Marka : ")
            model = input("Model : ")
            modelYil = input("ModelYil : ")
            fiyat = input("Fiyat : ")
            insertTable(id,marka,model,modelYil,fiyat)
        elif secim == "3":
            id = input("ID : ")
            fiyat = input("Fiyat : ")
            updateTable(id,fiyat)
        elif secim == "4":
            id = input("ID : ")
            deleteTable(id)
        elif secim == "5":
            sys.exit()
        else:
            print("Yanlış bir seçim yaptınız")

if __name__ == "__main__":
    createDB("araba")
    createTable()
    main()
    
    
   
    

