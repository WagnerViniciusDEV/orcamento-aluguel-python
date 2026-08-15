# Orçamento de Aluguel — Imobiliária R.M

Projeto acadêmico desenvolvido em Python e Flask para gerar orçamentos mensais de aluguel.

## Objetivo

Automatizar o cálculo de orçamentos para apartamentos, casas e estúdios, considerando valores-base, quartos, garagem, vagas, descontos e parcelamento do contrato imobiliário.

## Funcionalidades

* Orçamento para apartamentos, casas e estúdios
* Adicional para imóveis com dois quartos
* Inclusão de garagem
* Vagas de estacionamento para estúdios
* Desconto de 5% para apartamentos quando o cliente não possui crianças
* Contrato imobiliário de R$ 2.000,00
* Parcelamento do contrato em até cinco vezes
* Projeção dos valores durante 12 meses
* Download do orçamento em arquivo CSV
* Preservação das opções selecionadas após o cálculo
* Interface adaptada para computadores e celulares

## Tecnologias utilizadas



* Python
* Flask
* HTML
* CSS
* Programação orientada a objetos
* CSV

## Estrutura do projeto

```text
orcamento-aluguel-python/
├── app.py
├── imobiliaria.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── css/
        └── style.css
```

## Como executar

1. Tenha o Python instalado no computador.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no terminal.
4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação:

```bash
python app.py
```

6. Abra no navegador:

```text
http://127.0.0.1:5000
```

## Orientação a objetos

O projeto utiliza a classe base `Imovel` e as classes derivadas `Apartamento`, `Casa` e `Estudio`. Cada tipo de imóvel possui suas próprias regras para calcular o aluguel.

A classe `Orcamento` controla o valor do contrato, o parcelamento e a projeção dos pagamentos.
## Repositório

O código-fonte completo está disponível em:

https://github.com/WagnerViniciusDEV/orcamento-aluguel-python
## Autor

Wagner Vinicius

Projeto desenvolvido para a disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**.
