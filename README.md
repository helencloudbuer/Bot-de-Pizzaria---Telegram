# 🍕 Bot de Pizzaria - Telegram

Bot simples para Telegram, desenvolvido em Python com a biblioteca [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), que simula o atendimento de uma pizzaria: recebe pedidos, reclamações e elogios através de comandos.

## ✨ Funcionalidades

- Menu interativo com opções de pedido, reclamação e elogio
- Escolha entre pizza, hambúrguer ou salada
- Responde automaticamente a qualquer mensagem que não seja um comando válido, orientando o usuário

## 🤖 Comandos disponíveis

| Comando       | Descrição                          |
|---------------|-------------------------------------|
| `/opcao1`     | Fazer um pedido                     |
| `/opcao2`     | Reclamar de um pedido               |
| `/opcao3`     | Enviar um elogio                    |
| `/pizza`      | Pedir pizza                         |
| `/hamburguer` | Pedir hambúrguer                    |
| `/salada`     | Pedir salada                        |

## 🚀 Como executar

### Pré-requisitos

- Python 3.8 ou superior
- Uma conta no Telegram
- Um bot criado através do [@BotFather](https://t.me/BotFather)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install pyTelegramBotAPI
```

### 3. Configure o token do bot

Crie seu bot com o [@BotFather](https://t.me/BotFather) e copie o token gerado. **Nunca coloque o token diretamente no código** — use uma variável de ambiente:

```bash
export TELEGRAM_BOT_TOKEN="seu_token_aqui"
```

No Windows (PowerShell):

```powershell
$env:TELEGRAM_BOT_TOKEN="seu_token_aqui"
```

### 4. Execute o bot

```bash
python bot.py
```

## 🔒 Segurança

Este projeto usa variáveis de ambiente para proteger o token do bot. **Nunca** faça commit do seu token diretamente no código-fonte. Caso ele seja exposto acidentalmente, revogue-o imediatamente pelo [@BotFather](https://t.me/BotFather) usando o comando `/revoke`.

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## 📄 Licença

Este projeto é livre para uso e modificação.
