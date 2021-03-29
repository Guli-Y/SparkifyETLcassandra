# create tables queries

table1_create_query = """CREATE TABLE IF NOT EXISTS table1 (
                            artist TEXT, song TEXT, song_length FLOAT,
                            session_id INT, item_in_session INT,
                            PRIMARY KEY(session_id, item_in_session));
                      """
table2_create_query = """CREATE TABLE IF NOT EXISTS table2 (
                            artist TEXT, song TEXT, session_id INT,
                            item_in_session INT, user TEXT, user_id INT,
                            PRIMARY KEY(user_id, session_id, item_in_session));
                      """
table3_create_query = """CREATE TABLE IF NOT EXISTS table3 (
                            song TEXT, user TEXT, user_id INT,
                            PRIMARY KEY(song, user_id));
                      """

create_table_queries = [table1_create_query, table2_create_query, table3_create_query]

# insert queries

table1_insert_query = """INSERT INTO table1 (
                            artist, song, song_length,
                            session_id, item_in_session
                        )
                        VALUES (%s, %s, %s, %s, %s);
                      """
table2_insert_query = """INSERT INTO table2 (
                            artist, song, session_id,
                            item_in_session, user, user_id
                         )
                         VALUES (%s, %s, %s, %s, %s, %s);
                      """
table3_insert_query = """INSERT INTO table3 (
                            song, user, user_id
                         )
                         VALUES (%s, %s, %s);
                      """
