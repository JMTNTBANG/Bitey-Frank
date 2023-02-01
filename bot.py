import discord
from dotenv import load_dotenv
from os import getenv
from random import choice as randItem

class buttonRole:
    def __init__(self, role: discord.Role, style, emoji: str):
        self.role = role
        self.label = role.name
        if style.lower() == 'primary' or style.lower() == 'blurple': self.style = discord.ButtonStyle.primary
        elif style.lower() == 'secondary' or style.lower() == 'gray': self.style = discord.ButtonStyle.secondary
        elif style.lower() == 'success' or style.lower() == 'green': self.style = discord.ButtonStyle.success
        elif style.lower() == 'danger' or style.lower() == 'red': self.style = discord.ButtonStyle.danger
        elif style.lower() == 'link' or style.lower() == 'url': self.style = discord.ButtonStyle.link
        else: raise NameError
        self.emoji = emoji

def start():
    # Load Token
    load_dotenv()
    TOKEN = getenv('TOKEN')

    # Set Bot Intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    
    # Set Client Variable
    global client
    client = discord.Client(intents=intents)

    # Set Dynamic Variables
    global channels
    global roles
    global emojis
    channels = []
    roles = {}
    emojis = {}

    # Set Static Variables
    global frankMojis
    frankMojis = [
        ':chonkfronk',
        ':frank3:',
        ':sneakyfrank:',
        ':hideyhole:',
        ':jpeg:'
    ]

    # Set Functions/Lambdas
    def printEmoji(emoji: str):
        return f'<:{emojis[emoji].name}:{emojis[emoji].id}>'



    # printEmoji = lambda emoji: f'<:{emojis[emoji].name}:{emojis[emoji].id}>'

    async def memberStatusUpdate(inServer: bool, member):
        for channel in client.get_all_channels:
            if channel.guild == member.guild and member.guild.system_channel == channel:
                if inServer:
                    await channel.send(printEmoji(randItem(frankMojis)))
                else:
                    await channel.send(f'{printEmoji(":frank:")}7 {member.mention}')
                break
    async def sendButtonRoles(buttonRole: list, channel, message: str):
        view=discord.ui.View
        async def button_callback(interaction:discord.Interaction, role):
            if interaction.user in role.members:
                await interaction.user.remove_roles(role)
                await interaction.response.send_message(f'Removed Role: `{role.name}`')
            else:
                await interaction.user.add_roles(role)
                await interaction.response.send_message(f'Added Role: `{role.name}`')

        for role in buttonRole:
            button = discord.ui.Button(
                label = role.label,
                style=role.style,
                emoji=role.emoji
            )
            button.callback = button_callback(interaction, role.role)
            view.add_item(button)
        await channel.send(message)

    # Set Events
    @client.event
    async def on_ready():
        print(f'{client.user} active')

        # Channel Detection
        for guild in client.guilds:
            for channel in guild.channels:
                channels.append(channel)

        # Role Detection
        for guild in client.guilds:
            for role in guild.roles:
                roles[f'@{role.name}'] = role

        # Emoji Detection
        for guild in client.guilds:
            for emoji in guild.emojis:
                emojis[f':{emoji.name}:'] = emoji
        print(emojis)
        # Send Button Roles
        for guild in client.guilds:
            print(f'checking {guild}')
            for channel in guild.text_channels:
                print(f'checking {channel}')
                if channel.topic != None:
                    if 'Button Roles' in channel.topic:
                        print('valid channel')
                        await channel.purge()
                        pingRoles = [
                            buttonRole(
                                role = roles['@General Announcement Ping'],
                                style = 'gray',
                                emoji='🔔'
                            ),
                            buttonRole(
                                role = roles['@DankPods Ping'],
                                style = 'gray',
                                emoji = printEmoji(':dankpods:')
                            ),
                            buttonRole(
                                role = roles['@Garbage Time Ping'],
                                style = 'gray',
                                emoji = printEmoji(':tony:')
                            ),
                            buttonRole(
                                role = roles['@Garbage Stream Morn Ping'],
                                style = 'gray',
                                emoji = printEmoji(':chonkfronk:')
                            ),
                            buttonRole(
                                role = roles['@Garbage Stream Arvo Ping'],
                                style = 'gray',
                                emoji = printEmoji(':shrek:')
                            ),
                            buttonRole(
                                role = roles['@The Drum Thing Ping'],
                                style = 'gray',
                                emoji = printEmoji(':drumthing:')
                            ),
                            buttonRole(
                                role = roles['@Poll Ping'],
                                style = 'gray',
                                emoji = '📊'
                            )
                        ]
                        tonaRoles = [
                            buttonRole(
                                role = roles['@OG Tona'],
                                style = 'gray',
                                emoji = printEmoji(':tonatime:')
                            ),
                            buttonRole(
                                role = roles['@Sky Hihi'],
                                style = 'gray',
                                emoji = '☁️'
                            ),
                            buttonRole(
                                role = roles['@Rollo Finito'],
                                style = 'gray',
                                emoji = '🏁'
                            )
                        ]
                        await sendButtonRoles(pingRoles, channel, 'Click a Button to choose from various *Ping Roles*')
                        await sendButtonRoles(tonaRoles, channel, 'Click a Button to choose from various *Tona Roles*')

    @client.event
    async def on_member_join(member):
        await memberStatusUpdate(True, member)

    @client.event
    async def on_member_remove(member):
        await memberStatusUpdate(False, member)
        
    # Finalize Bot
    client.run(TOKEN)