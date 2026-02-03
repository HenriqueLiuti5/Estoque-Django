<div align="center">

# 📦 VerOnline Estoque

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
<br>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p align="center">
  <b>Sistema corporativo para gerenciamento de inventário e controle de estoque.</b><br>
  Foco em performance, segurança e UX moderna.
</p>

</div>

---

## 💻 Sobre o Projeto

O **VerOnline Estoque** é uma aplicação web desenvolvida para simplificar o controle de produtos em pequenas e médias empresas. 

Diferente de sistemas administrativos comuns, este projeto foca em uma **Experiência de Usuário (UX)** de alto nível, utilizando **Tailwind CSS** processado localmente para máxima performance e um design limpo e responsivo.

---

## ✨ Funcionalidades

- **🔐 Autenticação Segura**: Login e proteção de rotas (@login_required).
- **📦 Gestão de Produtos (CRUD)**: Adicionar, Listar, Editar e Excluir.
- **🛡️ Segurança Extra**: Exclusão com **Modal de Confirmação** para evitar erros.
- **🔍 Busca Inteligente**: Filtragem rápida na dashboard com botão de limpeza (UX).
- **🎨 UI Profissional**: Design System próprio com cores da marca ("Verde Verdão").
- **📱 Responsividade**: Funciona no Desktop e Mobile.

---

## 🚀 Como Executar

```bash
# 1. Clone o repositório
$ git clone https://github.com/HenriqueLiuti5/Estoque-Django.git

# 2. Entre na pasta
$ cd Estoque-Django

# 3. Crie e ative o ambiente virtual
$python -m venv venv$ venv\Scripts\activate  # Windows

# 4. Instale as dependências
$ pip install -r requirements.txt

# 5. Prepare o Banco de Dados
$ python manage.py migrate

# 6. Crie o Administrador
$ python manage.py createsuperuser

# 7. Rode o servidor
$ python manage.py runserver
```
Acesse: `http://127.0.0.1:8000`

---

## ⚙️ Tailwind (Desenvolvimento)

O CSS é gerado localmente (sem dependência de CDN online). Para editar os estilos:

```bash
# Instale as dependências do Node (se necessário)
$ npm install

# Rode o observador do Tailwind
$ npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

## 📝 Licença

Este projeto está sob a licença MIT.

---

<div align="center">
  <sub>Feito por Henrique Liuti</sub>
</div>
