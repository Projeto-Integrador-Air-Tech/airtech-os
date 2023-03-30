modelo_aeronave = {
    "table_name":"modelo_aeronave",
    "id_column": "id_modelo_aeronave",
    "columns": [
        "modelo",
        "fabricante",
        "ano_fabricacao",
        "tipo_aeronave",
        "capacidade_passageiros",
        "capacidade_carga",
        "alcance",
        "velocidade_maxima",
        "teto_servico",
        "tipo_motor",
        "quantidade_motores",
        "peso_maximo_decolagem",
        "sistema_combustivel",
        "sistema_eletrico",
        "sistema_hidraulico",
        "trem_de_pouso",
        "sistema_avionics",
        "certificacoes",
        "documentacao",
        "valor_mercado_atual",
        "historico_precos_venda",
        "valor_seguro",
        "historico_leasing",
        "imagem"
    ]
}
aeronaves = {
    "table_name":"aeronaves",
    "id_column": "id_aeronaves",
    "columns": [
        "modelo_id",
        "matricula",
        "numero_serie",
        "horas_voo",
        "ciclos_pouso_decolagem",
        "rotas_percorridas",
        "registro_voos",
        "proprietario_atual",
        "historico_proprietarios",
        "observacoes"
    ]
}

categorias_de_pecas = {
    "table_name":"categorias_de_pecas",
    "id_column": "id_categorias_de_pecas",
    "columns": [
        "categoria",
        "descricao"
    ]
}

pecas = {
    "table_name":"pecas",
    "id_column": "id_pecas",
    "columns": [
        "categoria_id",
        "nome",
        "numero_parte",
        "numero_serie",
        "descricao",
        "data_entrada",
        "preco",
        "fornecedor",
        "condicao",
        "quantidade"
    ]
}

localizacao_no_estoque = {
    "table_name":"localizacao_no_estoque",
    "id_column": "id_localizacao_no_estoque",
    "columns": [
        "id_da_peca",
        "id_da_prateleira",
        "corredor",
        "altura"
    ]
}

funcionarios = {
    "table_name":"funcionarios",
    "id_column": "id_funcionarios",
    "columns": [
        "nome",
        "cargo",
        "senha",
        "email",
        "telefone",
        "data_admissao",
        "colaborador_externo",
        "posição_externo",
        "empresa"
    ]
}


tarefas = {
    "table_name":"tarefas",
    "id_column": "id_tarefas",
    "columns": [
        "titulo",
        "descricao",
        "data_criacao",
        "data_conclusao",
        "status",
        "responsavel_id",
        "peca_id"
    ]
}


ordem_de_servico = {
    "table_name":"ordem_de_servico",
    "id_column": "id_ordem_de_servico",
    "columns": [
        "titulo",
        "descricao",
        "data_inicio",
        "data_fim",
        "status",
        "aeronave_id",
        "responsavel_id",
        "tarefas_ids"
    ]
}


