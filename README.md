# irrigacao-python
# FarmTech Solutions - Armazenamento de Dados com Python + SQLite

## Objetivo
Simular o armazenamento de dados agrícolas coletados pelo sistema de irrigação inteligente, usando banco de dados SQLite e implementando operações CRUD.

## Estrutura do Banco de Dados

| Campo     | Tipo    | Descrição                          |
|-----------|---------|------------------------------------|
| id        | INTEGER | Identificador único (auto)         |
| umidade   | REAL    | Umidade do solo (sensor DHT22)     |
| ph        | REAL    | pH do solo (simulado por LDR)      |
| fosforo   | INTEGER | Presença de fósforo (1=sim, 0=não) |
| potassio  | INTEGER | Presença de potássio (1=sim, 0=não)|
| bomba     | INTEGER | Status da bomba (1=ligada, 0=não)  |

## Funcionalidades do Script

- Inserção de novos dados (`INSERT`)
- Leitura de dados cadastrados (`SELECT`)
- Atualização de registros (`UPDATE`)
- Exclusão de registros (`DELETE`)

## Justificativa da Estrutura

A tabela simula os dados que seriam recebidos dos sensores físicos utilizados no ESP32, e corresponde ao MER desenvolvido na fase anterior. Os dados permitem realizar análises futuras, como ativação da bomba, histórico de irrigação, etc.

## Simulação

O script insere dois registros com dados simulados, imprime os dados e pode ser expandido para atualizações e exclusões.

## Requisitos

- Python 3.x
- Biblioteca padrão `sqlite3`

## Como Executar

1. Clone ou baixe o repositório
2. Execute: `python crud_irrigacao.py`
