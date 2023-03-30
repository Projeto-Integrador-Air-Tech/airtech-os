from queue import Queue
from typing import List, Dict, Any
from flask import request, jsonify, Response
from flask_restful import Resource
from mysql.connector.errors import ProgrammingError
from config.mysql_config import MySQLConnection


class GenericResource(Resource):
    """
    A generic resource class for handling CRUD operations on a MySQL database table.

    Args:
        Resource (flask_restful.Resource): The Flask-Restful Resource class.

    Attributes:
        task (Queue): A Queue object for managing tasks.

        table_name (str): The name of the database table to perform operations on.
        id_column (str): The name of the column in the database table that contains item IDs.
        columns (List[str]): A list of the names of the columns in the database table.

    Methods:
        get: Retrieve one or more items from the database.
        post: Insert a new item into the database.
        put: Update an existing item in the database.
        delete: Delete an item from the database.
    """

    task = Queue()

    def __init__(self, table_name: str, id_column: str, columns: List[str]) -> None:
        """
        Initialize a GenericResource instance.

        Args:
            table_name (str): The name of the table in the database.
            id_column (str): The name of the column that represents the ID of the items in the table.
            columns (List[str]): A list of the names of the columns in the table.

        Returns:
            None
        """
        super().__init__()
        self.table_name = table_name
        self.id_column = id_column
        self.columns = columns

    def get(self, item_id=None) -> Response:
        """
        Retrieve an item or a list of items from the database.

        Args:
            item_id (str): The ID of the item to retrieve. If not provided, all items are retrieved.

        Returns:
            Response: A Flask Response object containing the retrieved item or list of items.
        """
        try:
            with MySQLConnection() as conn:
                cursor = conn.cursor(dictionary=True)
                if item_id:
                    query = f"SELECT * FROM {self.table_name} WHERE {self.id_column} = %s"
                    cursor.execute(query, (item_id,))
                    result = cursor.fetchone()
                    if not result:
                        return {'message': 'Item not found'}, 404
                    return jsonify(result)
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                results = cursor.fetchall()
                return jsonify(results)
        except ProgrammingError:
            return Response(status=500)

    def post(self) -> Dict[str, Any]:
        """
        Create a new item in the database.

        Args:
            None

        Returns:
            Dict[str, Any]: A dictionary containing a message indicating if the item was created or not.
        """
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
                message = f'New item created! ID: {new_id}'
                if cursor.rowcount == 0:
                    return {'message': 'Item not found'}, 404
                return {'message': message}, 201

        except ProgrammingError:
            return Response(status=500)


    def put(self, item_id) -> Dict[str, Any]:
        """
        Update an existing item in the database.

        Args:
            item_id (str): The ID of the item to update.

        Returns:
            Dict[str, Any]: A dictionary containing a message indicating if the item was updated or not.
        """
        try:
            data = request.json
            with MySQLConnection() as conn, conn.cursor() as cursor:
                query = f"""
                    UPDATE {self.table_name}
                    SET {', '.join([f"{column}=%s" for column in self.columns])}
                    WHERE {self.id_column}=%s
                """
                values = [data[column] for column in self.columns] + [item_id]
                cursor.execute(query, values)
                conn.commit()
                message = f'Item updated! ID: {item_id}'
                if cursor.rowcount == 0:
                    return {'message': 'Item not found'}, 404
                return {'message': message}, 200

        except ProgrammingError:
            return Response(status=500)


    def delete(self, item_id) -> Dict[str, Any]:
        """
        Delete an item from the database.

        Args:
            item_id (str): The ID of the item to delete.

        Returns:
            Dict[str, Any]: A dictionary containing a message indicating if the item was deleted or not.
        """
        try:
            with MySQLConnection() as conn, conn.cursor() as cursor:
                query = f"DELETE FROM {self.table_name} WHERE {self.id_column} = %s"
                cursor.execute(query, (item_id,))
                conn.commit()
                if cursor.rowcount == 0:
                    return {'message': 'Item not found'}, 404
                return {'message': f'Item {item_id} deleted successfully!'}, 200
        except ProgrammingError:
            return Response(status=500)
