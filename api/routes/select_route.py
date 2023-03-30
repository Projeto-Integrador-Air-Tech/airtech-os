"""
This module defines classes that represent various resources in an API, such as tasks, aircraft, parts, and employees.
Each class inherits from the `GenericResource` class in `api.util.base_crud`.

Classes:
- Tarefas: Represents a resource for tasks.
- Aeronaves: Represents a resource for aircraft.
- Modelo_aeronave: Represents a resource for aircraft models.
- Localizacao_no_estoque: Represents a resource for parts storage locations.
- Categorias_de_pecas: Represents a resource for part categories.
- Pecas: Represents a resource for parts.
- Funcionarios: Represents a resource for employees.
- Ordem_de_servico: Represents a resource for service orders.

Each resource class has an `__init__` method that takes in the name of the database table, the name of the ID column,
and a list of column names for the respective resource.

Example usage:
    # create a resource instance for tasks
    tasks = Tarefas('tasks', 'id', ['name', 'description', 'completed'])

    # fetch a specific task
    task = tasks.get_by_id(1)

    # update a task
    task['completed'] = True
    tasks.update(1, task)

For more information, refer to the `GenericResource` class in `api.util.base_crud`.
"""
from api.util.dados import tarefas, aeronaves, modelo_aeronave, categorias_de_pecas, pecas, localizacao_no_estoque, ordem_de_servico, funcionarios
from api.util.base_crud import GenericResource


class Tarefas(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(tarefas['table_name'],
                         tarefas['id_column'], tarefas['columns'])


class Aeronaves(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(aeronaves['table_name'],
                         aeronaves['id_column'], aeronaves['columns'])


class ModeloAeronave(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(
            modelo_aeronave['table_name'], modelo_aeronave['id_column'], modelo_aeronave['columns'])


class LocalizacaoEstoque(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(localizacao_no_estoque['table_name'],
                         localizacao_no_estoque['id_column'], localizacao_no_estoque['columns'])


class CategoriasPecas(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(categorias_de_pecas['table_name'],
                         categorias_de_pecas['id_column'], categorias_de_pecas['columns'])


class Pecas(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(pecas['table_name'],
                         pecas['id_column'], pecas['columns'])


class Funcionarios(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(
            funcionarios['table_name'], funcionarios['id_column'], funcionarios['columns'])


class OrdemDeServico(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(ordem_de_servico['table_name'],
                         ordem_de_servico['id_column'], ordem_de_servico['columns'])
