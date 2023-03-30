import logging
from flask import Flask
from flask_restful import Api
from cheroot.wsgi import Server as WSGIServer
from api.util.dados import tasks, aircraft, aircraft_model, part_categories, parts, part_location, work_order, employees,external_employees, position, person,accesses
from api.routes.select_route import Tasks, Aircraft, Aircraft_model, Part_categories, Parts, Part_location, Work_order, Employees,ExternalEmployees, Position,Person,Accesses

APP = Flask(__name__)
API = Api(APP)
PORT = 8080
SERVER = WSGIServer(('0.0.0.0', PORT), APP)


API.add_resource(Tasks, '/tasks', '/tasks/<int:id>', resource_class_kwargs={
    'table_name': tasks['table_name'],
    'id_column': tasks['id_column'],
    'columns': tasks['columns']
})
API.add_resource(Aircraft, '/aircraft', '/aircraft/<int:id>', resource_class_kwargs={
    'table_name': aircraft['table_name'],
    'id_column': aircraft['id_column'],
    'columns': aircraft['columns']
})
API.add_resource(Aircraft_model, '/aircraft_model', '/aircraft_model/<int:id>', resource_class_kwargs={
    'table_name': aircraft_model['table_name'],
    'id_column': aircraft_model['id_column'],
    'columns': aircraft_model['columns']
})
API.add_resource(Part_location, '/part_location', '/part_location/<int:id>', resource_class_kwargs={
    'table_name': part_location['table_name'],
    'id_column': part_location['id_column'],
    'columns': part_location['columns']
})
API.add_resource(Part_categories, '/part_categories', '/part_categories/<int:id>', resource_class_kwargs={
    'table_name': part_categories['table_name'],
    'id_column': part_categories['id_column'],
    'columns': part_categories['columns']
})

API.add_resource(Parts, '/parts', '/parts/<int:id>', resource_class_kwargs={
    'table_name': parts['table_name'],
    'id_column': parts['id_column'],
    'columns': parts['columns']
})
API.add_resource(Work_order, '/work_order', '/work_order/<int:id>', resource_class_kwargs={
    'table_name': work_order['table_name'],
    'id_column': work_order['id_column'],
    'columns': work_order['columns']
})

API.add_resource(Employees, '/employees', '/employees/<int:id>', resource_class_kwargs={
    'table_name': employees['table_name'],
    'id_column': employees['id_column'],
    'columns': employees['columns']
})

API.add_resource(ExternalEmployees, '/external_employees', '/external_employees/<int:id>', resource_class_kwargs={
    'table_name': external_employees['table_name'],
    'id_column': external_employees['id_column'],
    'columns': external_employees['columns']
})

API.add_resource(Position, '/position', '/position/<int:id>', resource_class_kwargs={
    'table_name': position['table_name'],
    'id_column': position['id_column'],
    'columns': position['columns']
})

API.add_resource(Person, '/person', '/person/<int:id>', resource_class_kwargs={
    'table_name': person['table_name'],
    'id_column': person['id_column'],
    'columns': person['columns']
})

API.add_resource(Accesses, '/accesses', '/accesses/<int:id>', resource_class_kwargs={
    'table_name': accesses['table_name'],
    'id_column': accesses['id_column'],
    'columns': accesses['columns']
})


if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.INFO)
    logging.info('Running server on port %s', PORT)
    SERVER.safe_start()
