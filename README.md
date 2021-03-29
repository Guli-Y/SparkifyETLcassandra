## context

Sparkify is a startup company who provides music streaming services. They have collected user activities and the data is stored in csv files in data folder (not uploaded to this repostory). The analytics team in Sparkify asked the data engineering team to create a cassandra database for analyzing what songs their user are listening.

## purpose

To create a canssandra database and three tables based on three queries.

## queries and tables

1. query the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4

- artist TEXT, song TEXT, song_length FLOAT, session_id INT, item_in_session INT, PRIMARY KEY(session_id, item_in_session)

2. query the name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182   

- artist TEXT, song TEXT, session_id INT, item_in_session INT, user TEXT, user_id INT, PRIMARY KEY(user_id, session_id, item_in_session)

3. query every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

- song TEXT, user TEXT, user_id INT, PRIMARY KEY(song, user_id)


## usage

To setup cassandra in WSL go to [setup_cassandra_in_WSL.md](https://github.com/Guli-Y/SparkifyETLcassandra/blob/master/setup_cassandra_in_WSL.md)

To create/update the database:
- run > python etl.py

# reference
The data and the sparkify concept are from Udacity Data Engineering course.
The setup instructions and the codes are written by me.