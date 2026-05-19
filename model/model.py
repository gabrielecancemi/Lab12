from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getNazioni(self):
        return DAO.getNazioni()