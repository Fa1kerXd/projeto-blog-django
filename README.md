# Projeto Blog para Portfólio

## 📌 Visão Geral

Este é um projeto web desenvolvido com o framework **Django**, utilizando **Python** como linguagem principal e executado em containers **Docker**.

O objetivo foi criar um blog dinâmico, onde o autor pode:

- Publicar posts com editor avançado;
- Adicionar e gerenciar links externos;
- Configurar diferentes seções do site, como header, footer, entre outras;
- Permitir que outras pessoas também publiquem no blog.

---

## ⚙️ Estrutura do Projeto

O sistema é organizado dentro da pasta `djangoapp`, que contém:

```text
djangoapp/
├── project/       # Núcleo do Django: settings, urls, wsgi
├── blog/          # App responsável pela criação e exibição dos posts
└── site_setup/    # App para configuração das seções do site: header, footer e links
└── utils/         # Pasta com arquivos utils para o projeto.
```

## Arquivos .sh para automatizar comandos.

```text
collectstatic.sh    
commands.sh         
createsuperuser.sh
makemigrations.sh
migrate.sh
runserver.sh
``` 
### Arquivos principais

```text
Dockerfile          # Configuração da imagem Docker
docker-compose.yml  # Orquestração dos serviços
requirements.txt    # Dependências do projeto
```

---

## 🛠️ Funcionalidades

- **Administração de Posts:** editor Summernote integrado para criar e editar posts com formatação rica.
- **Gestão de Links:** menu dedicado para adicionar e remover links externos.
- **Configuração do Site:** opção de remover ou personalizar header e footer.
- **Publicação colaborativa:** possibilidade de outras pessoas também publicarem no blog.

---

## 📸 Capturas de Tela

### Seção Admin

![Foto da seção Admin](djangoapp/blog/static/Pictures_for_readme/Pictures_admin.png)

### Seção Post no Admin

![Foto da seção Post no Admin](djangoapp/blog/static/Pictures_for_readme/Pictures_admin_one.png)

![Foto da seção Post no Admin](djangoapp/blog/static/Pictures_for_readme/Pictures_admin_two.png)

### Site Setup

![Foto do Site Setup](djangoapp/blog/static/Pictures_for_readme/Pictures_site_setup_one.png)

![Foto do Site Setup](djangoapp/blog/static/Pictures_for_readme/Pictures_site_setup_two.png)


---

## 🚀 Tecnologias Utilizadas

- Python 3
- Django Framework
- Summernote Editor
- HTML / CSS
- Docker
- Docker Compose

---

## 🐳 Instalação e Execução com Docker

### Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

- Docker
- Docker Compose

---

## Passo a passo

### 1. Clonar o repositório

```bash
git clone https://github.com/Fa1kerXd/projeto-blog-django.git
cd projeto-blog-django
```

---

### 2. Construir a imagem Docker

```bash
docker-compose up --build
```

---

### 3. Rodar os containers

```bash
docker-compose up
```

---

### 4. Aplicar migrações do banco de dados

> Observação: o arquivo `makemigrations.sh` está acoplado ao próprio arquivo `migrate.sh`.

```bash
docker-compose run --rm djangoapp migrate.sh
```

---

### 5. Criar superusuário para acessar o admin

```bash
docker-compose run --rm djangoapp createsuperuser.sh
```

---

### 6. Acessar no navegador

```text
Admin: http://localhost:8000/admin
Blog:  http://localhost:8000/
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido para compor meu portfólio, demonstrando habilidades em:

- Desenvolvimento web com Django;
- Estruturação de aplicações modulares;
- Integração de editores ricos no admin;
- Customização de seções de um site dinâmico;
- Utilização de containers Docker para desenvolvimento e deploy.
