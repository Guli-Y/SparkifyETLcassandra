from connection import set_keyspace

def test_table1(session):
    try:
      rows = session.execute("""
                    SELECT artist, song, song_length
                    FROM table1
                    WHERE session_id = 338 AND item_in_session = 4;
                    """)
    except Except as e:
        print(e)
    # print the output
    for row in rows:
        print(row, '\n')

def test_table2(session):
    try:
      rows = session.execute("""
                    SELECT artist, song, user
                    FROM table2
                    WHERE user_id = 10 AND session_id = 182;
                    """)
    except Exception as e:
        print(e)
    # print the output
    for row in rows:
        print(row, '\n')

def test_table3(session):
    try:
      rows = session.execute("""
                    SELECT user
                    FROM table3
                    WHERE song='All Hands Against His Own';
                    """)
    except Except as e:
        print(e)
    # print the output
    for row in rows:
        print(row, '\n')

def test(session):
    print('querying table1\n')
    test_table1(session)
    print('querying table2\n')
    test_table2(session)
    print('querying table3\n')
    test_table3(session)
