# Máquina Enigma em Python: Uma Aplicação de Gramática Livre de Contexto para a Criptografia

## Sobre o Projeto

Este projeto é uma implementação da Máquina Enigma em Python, desenvolvido para a disciplina de Autômatos, do curso de Ciência da Computação na FACOMP/ICEN/UFPA. O objetivo principal é simular o funcionamento da Máquina Enigma, associando suas operações de criptografia e descriptografia a conceitos de Gramáticas Livres de Contexto (GLC).

O projeto inclui a implementação do código, a elaboração de um artigo técnico e a preparação de uma apresentação em slides.

## Integrantes

* Enya Araújo
* Leonardo da Rocha
* Matheus Diniz
* Caio Barbosa

## Funcionalidades

A aplicação possui uma interface gráfica (UI) baseada em Tkinter que simula uma máquina de escrever. As principais funcionalidades são:

* **Criptografar/Descriptografar:** Permite ao usuário inserir uma palavra e uma chave para realizar a criptografia ou descriptografia.
* **Modo Debug:** Exibe as transições (regras de produção) relacionadas à chave utilizada, o que ajuda a visualizar a lógica de criptografia/descriptografia e a conexão com a teoria de GLC.

## Estrutura do Código

O código é modularizado para facilitar a organização e o desenvolvimento. Os módulos principais são:

* **`Main`:** Controla o fluxo principal do programa, integrando os demais módulos.
* **`Front` (Interface):** Responsável pela interface com o usuário (UI), permitindo entrada de dados e exibição dos resultados.
* **`Módulo de Computação`:** Recebe a chave, a palavra e o modo de operação e retorna a palavra processada ou imprime as transições no modo debug.
* **`Módulo de Transições`:** Gera um dicionário que mapeia as transições de cada letra, sendo central para a conexão com a teoria de GLC e o modo debug.

## Instalação e Execução

Para rodar o projeto, é necessário ter o Python instalado. O projeto utiliza a biblioteca Pillow para a interface gráfica, que deve ser instalada.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Leonardo08x/-EN05215---AUTOMATOS---2025---Projeto-da-maquina-enigma-em-python.git](https://github.com/Leonardo08x/-EN05215---AUTOMATOS---2025---Projeto-da-maquina-enigma-em-python.git)
    ```
2.  **Instale a dependência:**
    ```bash
    pip install Pillow
    ```
3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```
