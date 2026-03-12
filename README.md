# Stark Bank Backend Challenge

Implementation developed for the **Stark Bank Backend Developer Trial** challenge.

This project integrates with the Stark Bank API to automate invoice creation and process webhook events that automatically generate transfers when an invoice is credited.

---


# 🇺🇸 English Documentation

## Overview

This project was developed for the **Stark Bank Backend Developer Trial**.

The application integrates with the Stark Bank API to automate invoice generation and process webhook events that trigger transfers when an invoice is credited.

---

## Technologies Used

* Python
* FastAPI
* Stark Bank Python SDK
* Pytest
* Ngrok
* Git
* GitHub

---

## Project Structure

```
starkbank-backend-challenge
│
├── app
│   ├── main.py
│   └── invoice_generator.py
│
├── config
│   └── stark_setup.py
│
├── scripts
│   └── create_invoice.py
│
├── tests
│   ├── test_invoice_generator.py
│   └── test_webhook_logic.py
│
├── docs
│   └── architecture.png
│
├── keys
│   └── public-key.pem
│
├── requirements.txt
└── README.md
```

---

## Architecture

Application flow:

```
Invoice created
      ↓
Stark Bank Sandbox processes payment
      ↓
Webhook sent
      ↓
Application receives event
      ↓
If event == credited
      ↓
Transfer automatically executed
```

Full architecture diagram available at:

```
docs/architecture.png
```

---

## Running the Project

### Clone the repository

```
git clone https://github.com/ArthurDon/starkbank-backend-challenge
cd starkbank-backend-challenge
```

---

### Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### Install dependencies

```
pip install -r requirements.txt
```

---

### Run the API

```
uvicorn app.main:app --reload
```

---

### Expose webhook using ngrok

```
ngrok http 8000
```

Use the generated URL as the webhook endpoint:

```
https://xxxx.ngrok-free.dev/webhook
```

---

## Generate Invoices

```
python -m scripts.create_invoice
```

Each execution generates **8 to 12 invoices**.

---

## Running Tests

```
pytest
```

Example output:

```
2 passed in 0.58s
```

---


# 🇧🇷 Documentação em Português

## Visão Geral

Esta aplicação possui duas responsabilidades principais:

1. Gerar automaticamente **8 a 12 invoices** com valores e clientes aleatórios.
2. Receber **eventos via webhook** enviados pela Stark Bank e, quando uma invoice é **creditada**, enviar automaticamente uma **transferência** com o valor recebido (menos eventuais taxas).

Todo o fluxo foi desenvolvido utilizando o ambiente **Sandbox da Stark Bank**.

---

## Tecnologias Utilizadas

* Python
* FastAPI
* Stark Bank Python SDK
* Pytest
* Ngrok
* Git
* GitHub

---

## Estrutura do Projeto

```
starkbank-backend-challenge
│
├── app
│   ├── main.py
│   └── invoice_generator.py
│
├── config
│   └── stark_setup.py
│
├── scripts
│   └── create_invoice.py
│
├── tests
│   ├── test_invoice_generator.py
│   └── test_webhook_logic.py
│
├── docs
│   └── architecture.png
│
├── keys
│   └── public-key.pem
│
├── requirements.txt
└── README.md
```

---

## Arquitetura

Fluxo da aplicação:

```
Invoice criada
      ↓
Stark Bank Sandbox processa pagamento
      ↓
Webhook enviado
      ↓
Aplicação recebe evento
      ↓
Se evento == credited
      ↓
Transfer criada automaticamente
```

Fluxograma detalhado disponível em:

```
docs/architecture.png
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/ArthurDon/starkbank-backend-challenge
cd starkbank-backend-challenge
```

---

### 2. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

### 4. Executar a API

```
uvicorn app.main:app --reload
```

---

### 5. Expor o webhook usando ngrok

```
ngrok http 8000
```

Configure a URL gerada como webhook na Stark Bank:

```
https://xxxx.ngrok-free.dev/webhook
```

---

## Gerar Invoices

```
python -m scripts.create_invoice
```

Cada execução gera entre **8 e 12 invoices**.

---

## Executar Testes

```
pytest
```

Exemplo de saída:

```
2 passed in 0.58s
```

---

## Aprendizados Durante o Desafio

Durante o desenvolvimento deste projeto foram praticados:

* integração com a API da Stark Bank
* desenvolvimento de sistemas baseados em webhooks
* construção de APIs com FastAPI
* criação de testes unitários utilizando Pytest
* exposição de aplicações locais utilizando ngrok
* organização de projetos backend


# Author

Arthur Donato

GitHub
https://github.com/ArthurDon


