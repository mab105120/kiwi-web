class Config:
    username = ''
    password = ''
    hostname = ''
    database = ''
    SQLALCHEMY_DATABASE_URI=f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_RECORD_QUERIES=True