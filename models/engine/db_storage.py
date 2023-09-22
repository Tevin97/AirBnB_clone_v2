#!/usr/bin/python3
"""A new dbstorage engine"""


class DBStorage():
    """A dbstorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes and links the engine to the db"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(getenv("HBNB_MYSQL_USER"),
                                            getenv("HBNB_MYSQL_PWD"),
                                            getenv("HBNB_MYSQL_HOST"),
                                            getenv("HBNB_MYSQL_DB")),
                                            pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):

