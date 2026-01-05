# Organizador de Pastas em Python

## Objetivo

Este projeto tem como objetivo organizar automaticamente arquivos dentro de uma pasta, separando-os em subpastas de acordo com suas extensões.  
Além disso, o projeto oferece a funcionalidade inversa, permitindo restaurar a estrutura original dos arquivos.

O foco é facilitar a organização de diretórios com muitos arquivos desordenados, de forma simples e rápida.

## Tecnologias

- **Python 3.14.2**
- **Módulo OS** (biblioteca padrão do Python)

## Estrutura de pastas
```text
.
├── archives/
│   ├── app.py
│   ├── presentation.pptx
│   ├── document.txt
│   ├── example.txt
│   └── sales.xlsx
├── in.py
├── out.py
└── README.md
```

## Como executar o projeto

Certifique-se de ter o **Python 3.14.2** instalado em sua máquina.

1. Clone este repositório ou baixe os arquivos do projeto.
2. Coloque os arquivos que deseja organizar dentro da pasta `archives/`.

### Organizar os arquivos

Execute o comando abaixo no terminal, a partir do diretório raiz do projeto:

```bash
python in.py
```

### Restaurar a estrutura original

Para desfazer a organização e retornar os arquivos ao estado anterior, execute:

```bash
python out.py
```
