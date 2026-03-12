Stark Bank Backend Challenge

Implementation developed for the Stark Bank Backend Developer Trial.

This project integrates with the Stark Bank API to automatically generate invoices and process webhook events to trigger transfers when invoices are credited.

🇺🇸 English Documentation
Overview

This project was developed for the Stark Bank Backend Developer Trial.

The application integrates with the Stark Bank API to:

Generate 8 to 12 invoices with random values and customers.

Receive webhook events from Stark Bank and automatically trigger a transfer when an invoice is credited.

The entire flow was built using the Stark Bank Sandbox environment.

Technologies Used

Technology | Version
Python | 3.14
FastAPI | 0.116+
Stark Bank Python SDK | Latest
Pytest | 9+
Ngrok | 3+
Git | 2+

Architecture

Application flow:

Project Structure

starkbank-backend-challenge

app
    main.py
    invoice_generator.py

config
    stark_setup.py

scripts
    create_invoice.py

tests
    test_invoice_generator.py
    test_webhook_logic.py
    test_webhook_ignore.py
    test_transfer_amount.py

docs
    architecture.drawio.png

keys
    public-key.pem

requirements.txt
README.md

Running the Project

Clone repository

git clone https://github.com/ArthurDon/starkbank-backend-challenge

cd starkbank-backend-challenge

Create virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the API

uvicorn app.main:app --reload

Expose webhook using ngrok

ngrok http 8000

Use the generated URL as the webhook endpoint

https://xxxx.ngrok-free.dev/webhook

Generate Invoices

python -m scripts.create_invoice

Each execution generates 8 to 12 invoices.

Running Tests

pytest

Example output

4 passed in 1.90s

What I Learned During This Challenge

During the development of this project I practiced and improved skills related to:

Stark Bank API integration

webhook-based backend architectures

building APIs with FastAPI

unit testing with Pytest

exposing local services using ngrok

backend project organization

🇧🇷 Documentação em Português
Visão Geral

Este projeto foi desenvolvido para o Stark Bank Backend Developer Trial.

A aplicação integra com a API da Stark Bank para:

Gerar automaticamente 8 a 12 invoices com valores e clientes aleatórios.

Receber eventos via webhook enviados pela Stark Bank e, quando uma invoice é creditada, enviar automaticamente uma transferência com o valor recebido (menos eventuais taxas).

Todo o fluxo foi desenvolvido utilizando o ambiente Stark Bank Sandbox.

Tecnologias Utilizadas

Tecnologia | Versão
Python | 3.14
FastAPI | 0.116+
Stark Bank Python SDK | Latest
Pytest | 9+
Ngrok | 3+
Git | 2+

Arquitetura

Fluxo da aplicação:

Estrutura do Projeto

starkbank-backend-challenge

app
    main.py
    invoice_generator.py

config
    stark_setup.py

scripts
    create_invoice.py

tests
    test_invoice_generator.py
    test_webhook_logic.py
    test_webhook_ignore.py
    test_transfer_amount.py

docs
    architecture.drawio.png

keys
    public-key.pem

requirements.txt
README.md

Como Executar o Projeto

Clonar o repositório

git clone https://github.com/ArthurDon/starkbank-backend-challenge

cd starkbank-backend-challenge

Criar ambiente virtual

python -m venv venv
venv\Scripts\activate

Instalar dependências

pip install -r requirements.txt

Rodar a API

uvicorn app.main:app --reload

Expor o webhook usando ngrok

ngrok http 8000

Configure a URL gerada como webhook na Stark Bank

https://xxxx.ngrok-free.dev/webhook

Gerar Invoices

python -m scripts.create_invoice

Cada execução cria 8 a 12 invoices.

Executar Testes

pytest

Exemplo de saída

4 passed in 1.90s

Author

Arthur Donato
https://github.com/ArthurDon
