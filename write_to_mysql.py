import yaml
import mysql.connector

def write_to_mysql(path):

    with open('db_config.yaml', 'r') as f:
        db_config = yaml.safe_load(f.read())

    hostname = db_config['datastore']['hostname']
    username = db_config['datastore']['user']
    current_database = db_config['datastore']['db']
    portnumber = db_config['datastore']['port']
    pw = db_config['datastore']['password']

    db = mysql.connector.connect(host=hostname, user=username, database=current_database, port=portnumber, password=pw)

    mycursor = db.cursor()

    sql = "INSERT INTO videos (path) VALUES (%s)"

    val = [path]
    mycursor.execute(sql, val)

    db.commit()
    db.close()


