# Bitey Frank

The official mascot of the unofficial Discord server of the Garbage Stream.

## Prerequisites

Have the following installed on your system:

1. **[Python 3.10+](https://www.python.org/downloads/)**
2. **[Pip](https://pip.pypa.io/en/stable/installation/)**

3. And an IDE of your own choice (**[VS-Code](https://code.visualstudio.com/)** is recommended)



## Required Pip Packages

Once Pip is installed use it to install the following:

1. discord.py - **[(PyPi Page)](https://pypi.org/project/python-discord/)**

2. python-dotenv - **[(PyPi Page)](https://pypi.org/project/python-dotenv/)**

2. google-api-python-client - **[(PyPi Page)](https://pypi.org/project/google-api-python-client/)**



## Configuration

In order to make the bot function, you will need a discord bot TOKEN (If you do not have a discord bot make one **[Here](https://discord.com/developers/applications)**)
<br />
<br />
Then with your newly aquired Bot Token, create a `.env` file to the top of the directory, then paste the following inside the file:
- `TOKEN=<Your Token Here>`

After that, add the dice emojis to the server where Frank will reside (These are located inside `/assets/die-emojis`)

## Development

When working on the bot, add an empty `debug` file to the top directory, to specify that the bot is running in debug mode.

