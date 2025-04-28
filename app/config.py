def get_cnx_string():
    username = ''
    password = ''
    hostname = ''
    port = 3306
    database = ''
    return f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'