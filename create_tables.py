import mysql.connector
import yaml

def create_table():
    with open('db_config.yaml', 'r') as f:
            db_config = yaml.safe_load(f.read())

    hostname = db_config['datastore']['hostname']
    username = db_config['datastore']['user']
    current_database = db_config['datastore']['db']
    portnumber = db_config['datastore']['port']
    pw = db_config['datastore']['password']

    db_conn = mysql.connector.connect(host=hostname, user=username, database=current_database, port=portnumber, password=pw)

    c = db_conn.cursor()

    c.execute('''
            CREATE TABLE IF NOT EXISTS videos
            (videoID INT NOT NULL AUTO_INCREMENT,
            path VARCHAR(500) NOT NULL,
            PRIMARY KEY (videoID))
    ''')

    db_conn.commit()
    db_conn.close()