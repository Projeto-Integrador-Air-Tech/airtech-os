import logging
from flask import Flask
from flask_restful import Api
from cheroot.wsgi import Server as WSGIServer
from api.util.dados import tarefas, aeronaves, modelo_aeronave, categorias_de_pecas, pecas ,localizacao_no_estoque, ordem_de_servico, funcionarios
from routes.select_route import Tarefas, Aeronaves, Modelo_aeronave, Categorias_de_pecas, Pecas ,Localizacao_no_estoque, Ordem_de_servico, Funcionarios

APP = Flask(__name__)
API = Api(APP)
PORT = 8080
SERVER = WSGIServer(('0.0.0.0', PORT), APP)



API.add_resource(Tarefas, '/tarefas', '/tarefas/<int:id>', resource_class_kwargs={
    'table_name': tarefas['table_name'],
    'id_column': tarefas['id_column'],
    'columns': tarefas['columns']
})
API.add_resource(Aeronaves, '/aeronaves', '/aeronaves/<int:id>', resource_class_kwargs={
    'table_name': aeronaves['table_name'],
    'id_column': aeronaves['id_column'],
    'columns': aeronaves['columns']
})
API.add_resource(Modelo_aeronave, '/modelo_aeronave', '/modelo_aeronave/<int:id>', resource_class_kwargs={
    'table_name': modelo_aeronave['table_name'],
    'id_column': modelo_aeronave['id_column'],
    'columns': modelo_aeronave['columns']
})
API.add_resource(Localizacao_no_estoque, '/localizacao_no_estoque', '/localizacao_no_estoque/<int:id>', resource_class_kwargs={
    'table_name': localizacao_no_estoque['table_name'],
    'id_column': localizacao_no_estoque['id_column'],
    'columns': localizacao_no_estoque['columns']
})
API.add_resource(Categorias_de_pecas, '/categorias_de_pecas', '/categorias_de_pecas/<int:id>', resource_class_kwargs={
    'table_name': categorias_de_pecas['table_name'],
    'id_column': categorias_de_pecas['id_column'],
    'columns': categorias_de_pecas['columns']
})

API.add_resource(Pecas, '/pecas', '/pecas/<int:id>', resource_class_kwargs={
    'table_name': pecas['table_name'],
    'id_column': pecas['id_column'],
    'columns': pecas['columns']
})
API.add_resource(Ordem_de_servico,'/ordem_de_servico', '/ordem_de_servico/<int:id>', resource_class_kwargs={
    'table_name': ordem_de_servico['table_name'],
    'id_column': ordem_de_servico['id_column'],
    'columns': ordem_de_servico['columns']
})

API.add_resource(Funcionarios, '/funcionarios', '/funcionarios/<int:id>', resource_class_kwargs={
    'table_name': funcionarios['table_name'],
    'id_column': funcionarios['id_column'],
    'columns': funcionarios['columns']
})


if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.INFO)
    logging.info('Running server on port %s', PORT)
    SERVER.safe_start()
