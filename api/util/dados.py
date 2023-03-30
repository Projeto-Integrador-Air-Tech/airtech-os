aircraft_model = {
    "table_name":"aircraft_model",
    "id_column": "id_aircraft_model",
    "columns": [
        "model",
        "manufacturer",
        "manufacturing_year",
        "aircraft_type",
        "passenger_capacity",
        "cargo_capacity",
        "range",
        "maximum_speed",
        "service_ceiling",
        "engine_type",
        "number_of_engines",
        "maximum_takeoff_weight",
        "fuel_system",
        "electrical_system",
        "hydraulic_system",
        "landing_gear",
        "avionics_system",
        "certifications",
        "documentation",
        "current_market_value",
        "sales_price_history",
        "insurance_value",
        "leasing_history",
        "image"
    ]
}

aircraft = {
    "table_name":"aircraft",
    "id_column": "id_aircraft",
    "columns": [
        "model_id",
        "registration",
        "serial_number",
        "flight_hours",
        "landing_takeoff_cycles",
        "routes_flown",
        "flight_log",
        "current_owner",
        "owner_history",
        "notes"
    ]
}

part_categories = {
    "table_name":"part_categories",
    "id_column": "id_part_categories",
    "columns": [
        "category",
        "description"
    ]
}

parts = {
    "table_name":"parts",
    "id_column": "id_parts",
    "columns": [
        "category_id",
        "name",
        "part_number",
        "serial_number",
        "description",
        "entry_date",
        "price",
        "supplier",
        "condition",
        "quantity"
    ]
}

part_location = {
    "table_name":"part_location",
    "id_column": "id_part_location",
    "columns": [
        "part_id",
        "shelf_id",
        "corridor",
        "height"
    ]
}

position ={
    "table_name":"position",
    "id_column": "id_position",
    "columns": [
        "name",
        "description"
    ]
}

person = {
    "table_name":"person",
    "id_column": "id_person",
    "columns": [
        "name",
        "email",
        "phone",
        "address",
        "date_of_birth",
        "gender",
        "cpf"
    ]
}

employees = {
    "table_name":"employees",
    "id_column": "id_employees",
    "columns": [
        "id_person",
        "id_position",
        "employee_email",
        "password"
    ]
}

external_employees = {
    "table_name":"employees",
    "id_column": "id_external_employee",
    "columns": [
        "id_person",
        "id_position",
        "employee_email",
        "password"
        "external_company"
    ]
}

accesses ={
    "table_name":"accesses",
    "id_column": "id_accesses",
    "columns": [
        "id_position",
        "name",
        "description"
    ]
}

tasks = {
    "table_name":"tasks",
    "id_column": "id_tasks",
    "columns": [
        "id_task_template",
        "creation_date",
        "completion_date",
        "status",
        "responsible_id",
        "additional_parts"
    ]
}
task_templates = {
    "table_name":"task_templates",
    "id_column": "id_task_template",
    "columns": [
        "title",
        "description",
        "part_id"
    ]
}

work_order = {
    "table_name":"work_order",
    "id_column": "id_work_order",
    "columns": [
        "title",
        "description",
        "start_date",
        "end_date",
        "status",
        "aircraft_id",
        "responsible_id",
        "tasks_ids"
    ]
}
