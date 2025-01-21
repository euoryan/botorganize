# BotOrganize

O **BotOrganize** é um bot para Telegram, desenvolvido para facilitar a gestão de grupos, organizando mensagens por hashtags e títulos. Ele mantém os links organizados e acessíveis em tempo real, com atualizações dinâmicas.

## Descrição
O BotOrganize é uma ferramenta eficiente para organizar links utilizando hashtags. As mensagens são ordenadas automaticamente e atualizadas em tempo real, permitindo fácil acesso às informações mais relevantes.

## Funcionalidades
- Organização automática de links por hashtags
- Lista fixada e atualizada dinamicamente
- Ordem alfabética das hashtags
- Interface limpa e simples

## Tecnologias
- Python (100%)
- Biblioteca `python-telegram-bot`

## Como Usar

### Pré-requisitos
- Python 3.8+
- Biblioteca `python-telegram-bot`

### Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/euoryan/botorganize.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd botorganize
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install python-telegram-bot
   ```

### Configuração
No arquivo `botorganize.py`, altere duas informações importantes:
1. Substitua `TOKEN` pelo token do seu bot do **BotFather**.
2. Substitua `ALLOWED_USER_ID` pelo seu ID de usuário do Telegram.

### Uso
1. Envie mensagens no formato:
   ```text
   #hashtag Título da mensagem
   ```
   Exemplo:
   ```text
   #projetos Bot organizador de links
   #desenvolvimento Novo projeto interessante
   ```

2. O bot irá:
   - Criar uma lista fixada
   - Organizar hashtags em ordem alfabética
   - Manter um link para cada mensagem original

<br/>

<div align="center">
Feito com ☕ e código por Ryan ;) Se gostou, deixa uma estrela pra ajudar! ⭐
</div>
