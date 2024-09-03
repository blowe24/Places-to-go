import psycopg2

# connect to Postgresql server
conn = psycopg2.connect(host="localhost", dbname='postgres', user='postgres',
                        password='123', port=5432)

cur = conn.cursor()

# create table if there isn't already one
cur.execute("""CREATE TABLE IF NOT EXISTS restaurants (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    city VARCHAR(100),
    name VARCHAR(100)
);
""")

def add():
    # take in inputs for the pcuntry, city, and name of the restaurant
    country = input('What country is the restaurant?: ')
    city = input('What city is the restaurant?: ')
    name = input('Name of Restaurant: ')
    
    # insert the input into restaurant table
    cur.execute("""INSERT INTO restaurants(country, city, name) VALUES (%s, %s, %s);
                """, (country, city, name))
    
    # print that value was added
    print(f'Your {city} collection now includes {name}!')
    conn.commit()

def look_up():
    
    while True:   
        # get input on what to look up 
        look = input("What do you want to look up?(all, country, city, or name) ")
        if look == 'country':
            # sql query for wanted data
            cur.execute("""SELECT country FROM restaurants""")
            # use for loop to make output more readable
            for row in cur.fetchall():
                print(row)
            return
        elif look == 'city':
            cur.execute("""SELECT city FROM restaurants""")
            for row in cur.fetchall():
                print(row)
            return
        elif look == 'name':
            cur.execute("""SELECT name FROM restaurants""")
            for row in cur.fetchall():
                print(row)
            return
        elif look == 'all':
            cur.execute("""SELECT * FROM restaurants""")
            for row in cur.fetchall():
                print(row)
            return
        else:
            print(f'{look} is an invalid input')

def main():
    # main function seeing what the user wants to do
    while True:    
        goal = input('Do you want to add or lookup places to go?(lookup or add): ')
        if goal == 'add':
            add()
            return
        elif goal == 'lookup':
            look_up()
            return
        else:
            print(f'{goal} is an invalid input.')

main()

cur.close()
conn.close()