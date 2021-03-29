from cassandra.cluster import Cluster

def set_keyspace():
    """
    connects to the cluster, creates sparkify database,
    set the session to the sparkify database and returns the session
    """
    # connect to the cluster
    try:
        cluster = Cluster()
        session = cluster.connect()
    except Exception as e:
        print('Error in cluster connection\n')
        print(e)

    # create keyspace called sparkify
    try:
        session.execute("""CREATE KEYSPACE IF NOT EXISTS sparkify
                            WITH REPLICATION = {'class' : 'SimpleStrategy',
                                  'replication_factor' : 1}
                        """, ())
    except Exception as e:
        print('Error in creating keyspace\n')
        print(e)

    # set keyspace to sparkify
    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print('Error in setting keyspace\n')
        print(e)
    return session, cluster


if __name__=="__main__":
    set_keyspace()
