from flask import Flask
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

class OrdemServico:
    def __init__(self, id, tarefas, pecas, data_inicio, data_termino, responsavel):
        self.id = id
        self.tarefas = tarefas
        self.pecas = pecas
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.responsavel = responsavel

ordens_servico = []
ordens_servico.append(OrdemServico(1, ["Tarefa 1", "Tarefa 2"], ["Peça 1", "Peça 2"], "2023-04-01", "2023-04-05", "Responsável 1"))
ordens_servico.append(OrdemServico(2, ["Tarefa 3", "Tarefa 4"], ["Peça 3", "Peça 4"], "2023-04-05", "2023-04-10", "Responsável 2"))



parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('tarefas', type=list)
parser.add_argument('pecas', type=list)
parser.add_argument('data_inicio', type=str)
parser.add_argument('data_termino', type=str)
parser.add_argument('responsavel', type=str)

class OrdemServicoResource(Resource):
    def get(self, os_id):
        for ordem_servico in ordens_servico:
            if ordem_servico.id == os_id:
                return ordem_servico.__dict__, 200
        return "Ordem de serviço não encontrada", 404

    def post(self):
        args = parser.parse_args()
        ordem_servico = OrdemServico(args['id'], args['tarefas'], args['pecas'], args['data_inicio'], args['data_termino'], args['responsavel'])
        ordens_servico.append(ordem_servico)
        return ordem_servico.__dict__, 201

    def put(self, os_id):
        args = parser.parse_args()
        for ordem_servico in ordens_servico:
            if ordem_servico.id == os_id:
                ordem_servico.tarefas = args['tarefas']
                ordem_servico.pecas = args['pecas']
                ordem_servico.data_inicio = args['data_inicio']
                ordem_servico.data_termino = args['data_termino']
                ordem_servico.responsavel = args['responsavel']
                return ordem_servico.__dict__, 200
        return "Ordem de serviço não encontrada", 404

    def delete(self, os_id):
        for ordem_servico in ordens_servico:
                if ordem_servico.id == os_id:
                    ordens_servico.remove(ordem_servico)
                    return "Ordem de serviço removida com sucesso", 200
                return "Ordem de serviço não encontrada", 404
        
api.add_resource(OrdemServicoResource, '/ordens_servico', '/ordens_servico/<int:os_id>')

if __name__ == '__main__':
    app.run(debug=True)