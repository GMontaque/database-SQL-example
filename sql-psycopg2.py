import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# query 2 - select only the "name" column from the "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# query 3 - select only "queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s',["Queen"])

# query 4 - select only by "artistId" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s',[51])

# query 5 - select only the albums with "artistId" #51 on the "album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s',[51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# Query 7 - personal test
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s',["AC/DC"])
cursor.execute('SELECT * FROM "track" WHERE "genre_id" = %s', [11] )


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for item in results:
    print(item)