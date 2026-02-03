# 📦 VerOnline Estoque

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

> Sistema corporativo para gerenciamento de inventário e controle de estoque, desenvolvido com foco em performance, segurança e uma interface moderna e responsiva.

## 💻 Sobre o Projeto

O **VerOnline Estoque** é uma aplicação web desenvolvida para simplificar o controle de produtos em pequenas e médias empresas. 

Diferente de sistemas administrativos comuns, este projeto foca em uma **Experiência de Usuário (UX)** de alto nível, utilizando **Tailwind CSS** processado localmente para máxima performance e um design limpo e responsivo que funciona perfeitamente em desktops e dispositivos móveis.

---

## ✨ Funcionalidades

- **🔐 Autenticação Segura**: Sistema de login e proteção de rotas (apenas usuários logados acessam o sistema).
- **📦 Gestão de Produtos (CRUD)**:
  - Adicionar novos itens ao inventário.
  - Visualizar lista completa com indicadores visuais de estoque.
  - Editar informações de produtos existentes.
  - Exclusão segura com **Modal de Confirmação** (evita cliques acidentais).
- **🔍 Busca Inteligente**: Filtragem rápida de produtos por nome diretamente na dashboard.
- **🎨 Interface Moderna**: Layout construído do zero com Tailwind CSS, seguindo padrões de design system corporativo (Verde "Brand").
- **📱 Totalmente Responsivo**: Adaptação fluida para telas de celulares, tablets e computadores.

---

## 🛠 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Backend**: [Python](https://www.python.org/) e [Django Framework](https://www.djangoproject.com/) (v5/6).
- **Frontend**: HTML5 Semântico e [Tailwind CSS](https://tailwindcss.com/) (Configuração Standalone/Local).
- **Banco de Dados**: SQLite (Padrão de desenvolvimento) / Suporte a PostgreSQL.
- **Gerenciamento de Dependências**: Pip & Virtualenv.
- **Ícones**: Heroicons (SVG).

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com)

### 🎲 Instalação

# 1. Clone este repositório
$ git clone [https://github.com/HenriqueLiuti5/Estoque-Django.git](https://github.com/HenriqueLiuti5/Estoque-Django.git)

# 2. Acesse a pasta do projeto no terminal/cmd
$ cd Estoque-Django

# 3. Crie um ambiente virtual (Recomendado)
$ python -m venv venv

# 4. Ative o ambiente virtual
# No Windows:
$ venv\Scripts\activate
# No Linux/Mac:
$ source venv/bin/activate

# 5. Instale as dependências
$ pip install -r requirements.txt

# 6. Configure o Banco de Dados (Migrações)
$ python manage.py migrate

# 7. Crie um superusuário para acessar o sistema
$ python manage.py createsuperuser

# 8. Inicie o servidor
$ python manage.py runserver

O servidor iniciará na porta:8000 - acesse <http://127.0.0.1:8000>

---

## ⚙️ Configuração do Tailwind (Para Desenvolvedores)

Este projeto não utiliza CDN para o CSS em produção, garantindo performance e funcionamento offline. O CSS é gerado localmente.

Se você deseja alterar o design ou as classes CSS, siga os passos:

1. Certifique-se de ter o **Node.js** instalado (para usar o `npx`).
2. No terminal, rode o comando para "observar" alterações e gerar o CSS:

```bash
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

### 📝 Licença
# Este projeto está sob a licença MIT.
