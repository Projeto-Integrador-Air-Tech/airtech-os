from api.util.dados import tarefas, aeronaves, modelo_aeronave, categorias_de_pecas, pecas ,localizacao_no_estoque, ordem_de_servico, funcionarios
from api.util.base_crud import GenericResource


class rotas(GenericResource):
    def __init__(self, table_name, id_column, columns):
        super().__init__(table_name, id_column, columns)
        

#     def __init__(self, table_name, id_column, columns):
#         super().__init__(tarefas['table_name'], tarefas['id_column'], tarefas['columns'])
        

# class Aeronaves(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(aeronaves['table_name'], aeronaves['id_column'], aeronaves['columns'])
        
        
# class Modelo_aeronave(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(modelo_aeronave['table_name'], modelo_aeronave['id_column'], modelo_aeronave['columns'])
        
# class Localizacao_no_estoque(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(localizacao_no_estoque['table_name'], localizacao_no_estoque['id_column'], localizacao_no_estoque['columns'])
        

# class Categorias_de_pecas(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(categorias_de_pecas['table_name'], categorias_de_pecas['id_column'], categorias_de_pecas['columns'])
        
        
# class Pecas(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(pecas['table_name'], pecas['id_column'], pecas['columns'])
        
# class Funcionarios(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(funcionarios['table_name'], funcionarios['id_column'], funcionarios['columns'])
        
# class Ordem_de_servico(GenericResource):
#     def __init__(self, table_name, id_column, columns):
#         super().__init__(ordem_de_servico['table_name'], ordem_de_servico['id_column'], ordem_de_servico['columns'])
        
