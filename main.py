import pymysql.cursors
import pymysql.connections

from pymysql import cursors

from creds import *


# join pets with owners
def joinData():
    # pull pets data
    sqlSelect = """
          select
            *
          from
            pets
          """

    # pull owners data
    sqlSelect2 = """
            select
             *
            from
             owners
        """

    # insert quit option
    insert_quit = """
        INSERT INTO 
            pets(id,animal_type_id,owner_id,name,age)
        VALUES
            (%s,%s,%s,%s,%s)
        """

    # Execute insert quit option
    #cursor.execute(insert_quit, ('999', '0', '0', 'Quit', '0'))

    # join all tables
    sql = '''SELECT * from pets INNER JOIN owners ON pets.owner_id = owners.id'''


    # Execute select

    cursor.execute(sqlSelect)
    cursor.execute(sqlSelect2)
    #cursor.execute(insert_quit)
    cursor.execute(sql)

# select pet id and name
def showData():
    # Our sql statement, easy to read
    dataSelect = """
        select
            id,name
        from
            pets
        """
    cursor.execute(dataSelect)
    for row in cursor:
        print(row)


# Connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()

# show initial pet name and id
try:
    with myConnection.cursor() as cursor:
        joinData()
        print(f"Name of all pets")
        showData()
except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()

# create function to export selected pet information
def petdata():
    petname = input("Enter pet name: ")
    # Our sql statement, easy to read
    sqlname = """
      select * from pets where name = %s;
      """
    cursor.execute(sqlname, ({petname, }))
    for row in cursor:
        print(row)


try:
    with myConnection.cursor() as cursor:
        petdata()

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
