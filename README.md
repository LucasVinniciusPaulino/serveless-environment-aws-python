# Projeto de Integração AWS - DynamoDB, API Gateway e Lambda

## Descrição
Este projeto demonstra a integração de recursos da AWS, utilizando DynamoDB para armazenar informações, API Gateway para fornecer acesso autorizado e uma Função Lambda para notificar em tempo real por e-mail sempre que houver acesso ao DynamoDB.

## Objetivo
Demonstrar uma aplicação desenvolvida em Python para criar, configurar e gerenciar serviços da AWS para consulta de informações no DynamonDB.

## Funcionalidades
- Banco de Dados DynamoDB: Armazena informações sobre cores para exemplo.
- API Gateway: Fornece um endpoint seguro para acessar informações sobre as cores armazenadas no DynamoDB. A autenticação é baseada em AWS Identity and Access Management (IAM).
- Função Lambda: Notifica em tempo real por e-mail (exemplo_lambda@gmail.com) sempre que houver acesso ao DynamoDB.

## Conteúdo do Projeto

1. **create_dynamodb_table.py**: Script para criar o banco de dados DynamoDB e adicionar dados iniciais sobre cores.

2. **create_api_gateway.py**: Script para configurar a API Gateway, criando um endpoint seguro para acessar informações sobre cores.

3. **create_lambda_function.py**: Script para criar a Função Lambda responsável por notificar em tempo real por e-mail sempre que houver acesso ao DynamoDB.
