# Stark Bank Backend Challenge

Implementation developed for the **Stark Bank Backend Developer Trial** challenge.

This project integrates with the Stark Bank API to automate invoice creation and process webhook events that automatically generate transfers when an invoice is credited.

---


# 🇺🇸 English Documentation

## Overview

This project was developed for the Stark Bank Backend Developer Trial.

The application integrates with the Stark Bank API to automate invoice generation and process webhook events that trigger transfers when an invoice is credited.

- Automation: The system periodically generates invoices with random values and customers.

- Webhooks: When the Stark Bank Sandbox simulates a payment, the application receives an event.

- Logic: If the event type is credited, the application automatically creates a transfer with the received amount (minus fees).

- Filtering: Events such as created or paid are logged but ignored.

---

## Technologies Used

Tecnologia	Versão
Python	3.14
FastAPI	0.116+
Stark Bank Python SDK	Latest
Pytest	9+
Ngrok	3+
Git	2+

---

## Project Structure

```
starkbank-backend-challenge
│
├── app
│   └── main.py
├── controllers
│   └── webhook_controller.py
├── services
│   └── transfer_service.py
├── jobs
│   └── invoice_generator_job.py
├── workers
│   └── invoice_worker.py
├── config
│   └── stark_setup.py
├── scripts
│   └── create_invoice.py
├── tests
│   ├── controllers
│   ├── services
│   ├── jobs
│   └── workers
├── docs
│   └── architecture.drawio.png
├── keys
│   └── public-key.pem
├── requirements.txt
├── pytest.ini
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
docs/architecture.drawio.png
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

O sistema gera invoices periodicamente e o ambiente Sandbox simula o pagamento. Se o evento for credited, o sistema cria a transferência. Eventos como created ou paid são apenas registrados em log**.

---

## Tecnologias Utilizadas

Tecnologia | Versão
Python | 3.14
FastAPI | 0.116+
Stark Bank Python SDK,Latest
Pytest | 9+
Ngrok | 3+
Git | 2+

---

## Estrutura do Projeto

```
starkbank-backend-challenge
│
├── app
│   └── main.py
├── controllers
│   └── webhook_controller.py
├── services
│   └── transfer_service.py
├── jobs
│   └── invoice_generator_job.py
├── workers
│   └── invoice_worker.py
├── config
│   └── stark_setup.py
├── scripts
│   └── create_invoice.py
├── tests
│   ├── controllers
│   ├── services
│   ├── jobs
│   └── workers
├── docs
│   └── architecture.drawio.png
├── keys
│   └── public-key.pem
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Arquitetura

Fluxo da aplicação:

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

Fluxograma detalhado disponível em:

```
docs/architecture.drawio.png
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


