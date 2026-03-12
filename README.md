🏦 Stark Bank Backend Challenge
Este projeto foi desenvolvido para o Stark Bank Backend Developer Trial. A aplicação automatiza o ciclo de faturamento e transferência, integrando-se à API da Stark Bank no ambiente Sandbox.

English | Português

🇺🇸 English Documentation
📌 Overview
The application integrates with the Stark Bank API to:

Automatic Generation: Create 8 to 12 invoices with random values and customers.

Webhook Processing: Receive real-time events and trigger automatic transfers when an invoice is credited.

Sandbox Environment: Full flow validation using Stark Bank's testing environment.

🛠 Technologies

Technology,Version
Python,3.14
FastAPI,0.116+
Stark Bank SDK,Latest
Pytest,9+
Ngrok,3+

📂 Project Structure
app/: Core logic (FastAPI & Invoice Engine)

config/: SDK and Environment Setup

scripts/: Script to trigger batch invoice creation

tests/: Unit and integration tests

keys/: ECDSA Public Key

requirements.txt: Project dependencies

🚀 How to Run
Clone & Setup
git clone https://github.com/ArthurDon/starkbank-backend-challenge
cd starkbank-backend-challenge
python -m venv venv
source venv/bin/activate (ou venv\Scripts\activate no Windows)
pip install -r requirements.txt

Start API & Webhook
uvicorn app.main:app --reload
ngrok http 8000

Generate Invoices
python -m scripts.create_invoice

🇧🇷 Documentação em Português
📌 Visão Geral
Esta aplicação automatiza fluxos financeiros utilizando a API da Stark Bank:

Geração em Lote: Cria entre 8 e 12 faturas (invoices) com dados aleatórios.

Automação de Transferência: Ao receber a confirmação de crédito via Webhook, o sistema inicia automaticamente uma transferência do valor.

Segurança: Implementação preparada para validação de assinaturas e chaves ECDSA.

🧪 Testes
Para garantir a confiabilidade do fluxo, execute a suíte de testes:
pytest

Exemplo de saída: 4 passed in 1.90s

🧠 Aprendizados
Durante este desafio, foram consolidados conhecimentos em:

Arquiteturas baseadas em Webhooks.

Consumo de APIs bancárias de alta performance.

Desenvolvimento de APIs assíncronas com FastAPI.

Mocking e testes de integração com Pytest.

👤 Author
Arthur Donato
