# [cite_start]Máquina Enigma em Python: Uma Aplicação de Gramática Livre de Contexto para a Criptografia [cite: 2]

## Sobre o Projeto

[cite_start]Este projeto é uma implementação da Máquina Enigma em Python, desenvolvido para a disciplina de Autômatos, do curso de Ciência da Computação na FACOMP/ICEN/UFPA[cite: 7, 8]. [cite_start]O objetivo principal é simular o funcionamento da Máquina Enigma [cite: 16][cite_start], associando suas operações de criptografia e descriptografia a conceitos de Gramáticas Livres de Contexto (GLC)[cite: 16].

[cite_start]O projeto inclui a implementação do código, a elaboração de um artigo técnico e a preparação de uma apresentação em slides[cite: 17].

## [cite_start]Integrantes [cite: 3]

* [cite_start]Enya Araújo [cite: 3]
* [cite_start]Leonardo da Rocha [cite: 4]
* [cite_start]Matheus Diniz [cite: 5]
* [cite_start]Caio Barbosa [cite: 6]

## Funcionalidades

[cite_start]A aplicação possui uma interface gráfica (UI) baseada em Tkinter que simula uma máquina de escrever[cite: 33]. As principais funcionalidades são:

* [cite_start]**Criptografar/Descriptografar:** Permite ao usuário inserir uma palavra e uma chave para realizar a criptografia ou descriptografia[cite: 33, 34].
* [cite_start]**Modo Debug:** Exibe as transições (regras de produção) relacionadas à chave utilizada, o que ajuda a visualizar a lógica de criptografia/descriptografia e a conexão com a teoria de GLC[cite: 31, 34, 35].

## [cite_start]Estrutura do Código [cite: 29]

[cite_start]O código é modularizado para facilitar a organização e o desenvolvimento[cite: 30]. Os módulos principais são:

* [cite_start]**`Main`:** Controla o fluxo principal do programa, integrando os demais módulos[cite: 32].
* [cite_start]**`Front` (Interface):** Responsável pela interface com o usuário (UI), permitindo entrada de dados e exibição dos resultados[cite: 33].
* [cite_start]**`Módulo de Computação`:** Recebe a chave, a palavra e o modo de operação e retorna a palavra processada ou imprime as transições no modo debug[cite: 34].
* [cite_start]**`Módulo de Transições`:** Gera um dicionário que mapeia as transições de cada letra, sendo central para a conexão com a teoria de GLC e o modo debug[cite: 35, 36].

## Instalação e Execução

[cite_start]Para rodar o projeto, é necessário ter o Python instalado[cite: 47]. O projeto utiliza a biblioteca Pillow para a interface gráfica, que deve ser instalada.

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