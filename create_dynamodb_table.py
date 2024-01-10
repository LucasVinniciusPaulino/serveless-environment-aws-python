import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='color_table',
    KeySchema=[
        {
            'AttributeName': 'Cor',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Cor',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='color_table')

# Dados da Tabela, Lista de cores de A-Z Referência (https://www.dicio.com.br/alfabeto-de-cores-lista-de-cores-de-a-z/)
cores = [
    'Amarelo', 'Âmbar', 'Ametista', 'Azul', 'Bege', 'Bordô', 'Branco', 'Bronze', 'Caramelo', 'Castanho', 'Cereja', 'Chocolate', 'Ciano', 'Cinza', 'Cobre', 'Coral',
    'Creme', 'Damasco', 'Dourado', 'Escarlate', 'Esmeralda', 'Ferrugem', 'Gelo', 'Jambo', 'Laranja', 'Lavanda', 'Lilás', 'Limão', 'Loiro', 'Malva', 'Marfim', 'Marrom',
    'Mostarda', 'Negro', 'Ouro', 'Prata', 'Preto', 'Púrpura', 'Rosa', 'Roxo', 'Rubro', 'Salmão', 'Tijolo', 'Verde', 'Vermelho', 'Vinho', 'Violeta'
]

for cor in cores:
    table.put_item(Item={'Cor': cor})