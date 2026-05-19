from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getConfiniAnno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1no, state2no, conttype from contiguity c 
                    where year <= %s"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row["state1no"])
        cursor.close()
        conn.close()
        return result
