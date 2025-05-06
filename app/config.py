class Config:
    username = 'admin2'
    password = 'admin123'
    hostname = 'kiwidev.c7o6cy0we3aj.us-east-2.rds.amazonaws.com'
    database = 'kiwi-dev2'
    port = 3306
    SQLALCHEMY_DATABASE_URI=f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_RECORD_QUERIES=True