from connection import set_keyspace
from extract import extract_data
from queries import *
from test import test
import pandas as pd
import csv

def drop_tables(session):
    """
    drops the tables
    """
    for table in ['table1', 'table2', 'table3']:
        try:
            rows = session.execute(f"""
                                    DROP TABLE {table};
                                    """)
            print(f'dropped the {table}\n')
        except Exception as e:
            print(f'Error with dropping {table} table\n')
            print(e)

def create_table(session, query):
    """
    creates table
    """
    try:
        session.execute(query)
    except Exception as e:
        print('Error with creating table\n')
        print(e)

def load_table(session, query, data):
    """
    loads the data into table
    """
    try:
        session.execute(query, data)
    except Exception as e:
        print(e)

def main():
    """
    creates and loads table1, 2, 3
    """
    session, cluster = set_keyspace()
    extract_data()
    df = pd.read_csv('processed_data.csv')

    # create tables
    for query in create_table_queries:
        create_table(session, query)

    # loading data to the tables
    for row in df.values:
        table1_data = (row[i] for i in [0, 9, 5, 8, 3])
        table2_data = (row[0], row[9], row[8], row[3], row[1]+' '+row[4], row[10])
        table3_data = (row[9], row[1]+' '+row[4], row[10])
        # load all of them
        load_table(session, table1_insert_query, table1_data)
        load_table(session, table2_insert_query, table2_data)
        load_table(session, table3_insert_query, table3_data)

    test(session)

    # drop_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__=='__main__':
    main()


