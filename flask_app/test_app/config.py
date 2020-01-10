class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://rafayel114:1991114@localhost/test1'

    SECURITY_PASSWORD_SALT = 'salty_salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
