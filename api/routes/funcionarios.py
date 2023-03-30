import queue
from flask import Response, request, jsonify
from flask_restful import Resource
from config.mysql_config import MySQLConnection


class FuncionariosResource(Resource):
    """
     Class responsible for handling requests related to employees.
     """
    task = queue.Queue()

    def get(self, id=None):
        """
         Method that returns information for an employee or a list of all employees.

         Args:
             id (int, optional): Employee identifier. If not passed, returns a list of all employees.

         returns:
             Response: Response object with employee information or list of employees.
         """
        with MySQLConnection() as conn:
            cursor = conn.cursor(dictionary=True)
            if id is None:
                query = "SELECT id_funcionarios, nome FROM funcionarios"
                cursor.execute(query)
                funcionarios = cursor.fetchall()
            else:
                query = "SELECT * FROM funcionarios WHERE id_funcionarios=%s"
                cursor.execute(query, (id,))
                funcionarios = cursor.fetchone()
            if not funcionarios:  # verifica se a variável está vazia ou é None
                return Response(status=404)
            return jsonify(funcionarios)

    def post(self):
        """
         Method that creates a new employee.

         Args:
             None

         returns:
             dict: Dictionary with the success message and the ID of the new employee created.
         """
         
        data = request.json
        with MySQLConnection() as conn, conn.cursor() as cursor:
            query = """
                INSERT INTO funcionarios 
                (nome, cargo, senha, email, telefone, data_admissao, colaborador_externo, posição_externo, empresa) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, tuple(data.values()))
            new_funcionario_id = cursor.lastrowid
            conn.commit()
        return {'message': f'Funcionário criado com sucesso! ID: {new_funcionario_id}'}, 201

    def put(self, id):
        """
         Updates an employee's information in the MySQL database.

         :param id: The ID of the employee to be updated.
         :type id: int

         :return: A JSON object containing a message indicating that the employee was successfully updated and the corresponding HTTP status code.
         :rtype: dict

         :raises: There are no exceptions thrown by this function, but an exception may be thrown if there are database connection problems or if the employee ID is not found in the table.
         """
        data = request.json
        with MySQLConnection() as conn, conn.cursor() as cursor:
            cursor.execute("""
                UPDATE funcionarios
                SET nome=%s, cargo=%s, senha=%s, email=%s, telefone=%s, data_admissao=%s, colaborador_externo=%s, posição_externo=%s, empresa=%s
                WHERE id_funcionarios=%s
            """, (
                data['nome'], data['cargo'], data['senha'], data['email'], data['telefone'],
                data['data_admissao'], data['colaborador_externo'], data['posição_externo'], data['empresa'], id
            ))
            conn.commit()
            message = f'Funcionário atualizado com sucesso! ID: {id}'
            status_code = 200 if cursor.rowcount > 0 else 404
            return {'message': message}, status_code


    def patch(self, id):
        """
         Partially updates an employee's information in the MySQL database.

         :param id: The ID of the employee to be updated.
         :type id: int

         :return: A JSON object containing a message indicating whether the employee was updated successfully and the corresponding HTTP status code.
         :rtype: dict

         :raises: There are no exceptions thrown by this function, but an exception may be thrown if there are database connection problems or if the employee ID is not found in the table.
         """
        data = request.json
        with MySQLConnection() as conn:
            cursor = conn.cursor()
            updates = []
            for key, value in data.items():
                updates.append(f"{key}=%s")
            query = f"""
                UPDATE funcionarios SET {','.join(updates)} WHERE id_funcionarios = %s
            """
            values = list(data.values()) + [id]
            cursor.execute(query, values)
            conn.commit()
            if cursor.rowcount == 0:
                return {'message': 'Funcionário não encontrado'}, 404
            return {'message': f'Funcionário {id} atualizado com sucesso!'}, 200

    def delete(self, id):
        """
         Removes an employee from the MySQL database.

         :param id: The ID of the employee to be removed.
         :type id: int

         :return: A JSON object containing a message indicating whether the employee was successfully removed and the corresponding HTTP status code.
         :rtype: dict

         :raises: There are no exceptions thrown by this function, but an exception may be thrown if there are database connection problems or if the employee ID is not found in the table.
        """
        with MySQLConnection() as conn, conn.cursor() as cursor:
            query = "DELETE FROM funcionarios WHERE id_funcionarios = %s"
            cursor.execute(query, (id,))
            conn.commit()
            if cursor.rowcount == 0:
                return {'message': 'Funcionário não encontrado'}, 404
            else:
                return {'message': f'Funcionário {id} excluído com sucesso!'}, 200
