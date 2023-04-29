from flask import request, jsonify, Response
from flask_restful import Resource
from mysql.connector.errors import ProgrammingError
from config.mysql_config import MySQLConnection
from typing import List, Dict, Any
from queue import Queue

class GenericResource(Resource):
    task = Queue()

    def __init__(self, table_name: str, id_column: str, columns: List[str]) -> None:
        super().__init__()
        self.table_name = table_name
        self.id_column = id_column

        self.columns = columns

    def get(self, id=None) -> Response:
        try:
            with MySQLConnection() as conn:
                cursor = conn.cursor(dictionary=True)
                if id:
                    query = f"SELECT * FROM {self.table_name} WHERE {self.id_column} = %s"
                    cursor.execute(query, (id,))
                    result = cursor.fetchone()
                    if not result:
                        return Response(status=404)
                    return jsonify(result)
                else:
                    query = f"SELECT * FROM {self.table_name}"
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return jsonify(results)
        except ProgrammingError:
            return Response(status=500)

    def post(self) -> Dict[str, Any]:
        try:
            data = request.json
            with MySQLConnection() as conn, conn.cursor() as cursor:
                query = f"""
                    INSERT INTO {self.table_name} 
                    ({', '.join(self.columns)}) 
                    VALUES ({', '.join(['%s' for _ in self.columns])})
                """
                values = [data[column] for column in self.columns]
                cursor.execute(query, values)
                new_id = cursor.lastrowid
                conn.commit()
            return {'message': f'New item created! ID: {new_id}'}, 201
        except ProgrammingError:
            return Response(status=500)

    def put(self, id) -> Dict[str, Any]:
        try:
            data = request.json
            with MySQLConnection() as conn, conn.cursor() as cursor:
                query = f"""
                    UPDATE {self.table_name}
                    SET {', '.join([f"{column}=%s" for column in self.columns])}
                    WHERE {self.id_column}=%s
                """
                values = [data[column] for column in self.columns] + [id]
                cursor.execute(query, values)
                conn.commit()
                message = f'Item updated! ID: {id}'
                status_code = 200 if cursor.rowcount > 0 else 404
            return {'message': message}, status_code
        except ProgrammingError:
            return Response(status=500)

    def delete(self, id) -> Dict[str, Any]:
        try:
            with MySQLConnection() as conn, conn.cursor() as cursor:
                query = f"DELETE FROM {self.table_name} WHERE {self.id_column} = %s"
                cursor.execute(query, (id,))
                conn.commit()
                if cursor.rowcount == 0:
                    return {'message': 'Item not found'}, 404
                else:
                    return {'message': f'Item {id} deleted successfully!'}, 200
        except ProgrammingError:
            return Response(status=500)
