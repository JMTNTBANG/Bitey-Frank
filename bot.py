import discord
from dotenv import load_dotenv
from os import getenv
from random import choice as randItem
from random import randint
import os
from commands import *
import time
from youtube_tools import getLatestVideo
from threading import Thread
import asyncio
import requests


class buttonRole:
    def __init__(self, role: discord.Role, style, emoji: str):
        self.role = role
        self.label = role.name
        if style.lower() == 'primary' or style.lower() == 'blurple':
            self.style = discord.ButtonStyle.primary
        elif style.lower() == 'secondary' or style.lower() == 'gray':
            self.style = discord.ButtonStyle.secondary
        elif style.lower() == 'success' or style.lower() == 'green':
            self.style = discord.ButtonStyle.success
        elif style.lower() == 'danger' or style.lower() == 'red':
            self.style = discord.ButtonStyle.danger
        elif style.lower() == 'link' or style.lower() == 'url':
            self.style = discord.ButtonStyle.link
        elif style.lower() == 'dropdown':
            self.style = None
        else:
            raise NameError('Button Style Not Found')
        self.emoji = emoji

class webhook:
    def __init__(self, content, username, avatar, url, embeds=None, attachments=None,) -> None:
        self.content = content
        self.username = username
        self.avatar = avatar
        self.url = url
        if embeds != None: self.embeds = embeds
        if attachments != None: self.attachments = attachments
        self.json = {
            "content": self.content,
            "username": self.username,
            "avatar_url": self.avatar
        }

def start():
    # Load Token
    load_dotenv()
    TOKEN = getenv('TOKEN')
    if TOKEN is None:
        print('GIMMIE YO GODDAMN TOKEN B***CH')
        exit(1)

    async def checkChannels():
        async def checker(YTchannel):
            newLatestVideo = getLatestVideo(f'@{YTchannel}')
            if f'{YTchannel}.txt' not in os.listdir('./youtube'):
                open(f'youtube/{YTchannel}.txt', 'x')
            if f'Title: {newLatestVideo.title} | URL: {newLatestVideo.url} | Timestamp: {newLatestVideo.published}' != open(f'youtube/{YTchannel}.txt', 'r').readline():
                open(f'youtube/{YTchannel}.txt', 'w').write(f'Title: {newLatestVideo.title} | URL: {newLatestVideo.url} | Timestamp: {newLatestVideo.published}')
                response = f'{roles[f"@{newLatestVideo.channel} Ping"].mention} New video by {newLatestVideo.channel}! `{newLatestVideo.title}`\nUploaded <t:{int(newLatestVideo.published.timestamp())}:R>\n{newLatestVideo.url}'
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.topic != None:
                            if 'YouTube Ping' in channel.topic:
                                await channel.send(response)

        await checker('DankPods')
        await checker('GarbageTime420')
        await checker('the.drum.thing.')
        await checker('JMTNTBANG')
        await checker('joshdoesntplaydrums')
        

    # Set Bot Intents
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    # Set Client Variables
    global client
    global tree
    client = discord.Client(intents=intents)
    tree = discord.app_commands.CommandTree(client)

    # Set Dynamic Variables
    global channels
    global roles
    global emojis
    global assets
    global importedCommands
    global rolesLoaded
    global debug
    channels = []
    roles = {}
    emojis = {}
    assets = []
    importedCommands = []
    rolesLoaded = False
    debug = False

    # Set Static Variables
    global frankMojis
    frankMojis = [
        ':chonkfronk:',
        ':frank3:',
        ':sneakyfrank:',
        ':hideyhole:',
        ':jpeg:'
    ]

    # Set Functions/Lambdas
    def printEmoji(emoji: str):
        return f'<:{emojis[emoji].name}:{emojis[emoji].id}>'

    async def memberStatusUpdate(inServer: bool, member):
        for channel in client.get_all_channels():
            if channel.guild == member.guild and member.guild.system_channel == channel:
                if isinstance(channel, discord.TextChannel):
                    if inServer:
                        await channel.send(printEmoji(randItem(frankMojis)))
                    else:
                        await channel.send(f'{printEmoji(":frank:")}7 {member.mention}')
                    break

    async def sendButtonRoles(buttonRole, channel, message: str, dropdown: bool = False):
        def gen_callback(role):
            async def button_callback(interaction: discord.Interaction):
                if interaction.user in role.members:
                    await interaction.user.remove_roles(role)  # type: ignore
                    await interaction.response.send_message(f'Removed Role: `{role.name}`', ephemeral=True)
                else:
                    await interaction.user.add_roles(role)  # type: ignore
                    await interaction.response.send_message(f'Added Role: `{role.name}`', ephemeral=True)
            return button_callback
        def gen_select_callback(select: discord.ui.Select):
            async def select_callback(interaction: discord.Interaction):
                response=''
                for role in buttonRole:
                    if interaction.user in role.role.members:
                        await interaction.user.remove_roles(role.role)  # type: ignore
                        response+=f'Removed Role: `{role.role.name}`\n'
                for role in buttonRole:
                    if select.values[0] == role.label:
                        if interaction.user in role.role.members:
                            await interaction.user.remove_roles(role.role)  # type: ignore
                            response+=f'Removed Role: `{role.role.name}`\n'
                        else:
                            await interaction.user.add_roles(role.role)  # type: ignore
                            response+=f'Added Role: `{role.role.name}`\n'
                await interaction.response.send_message(response, ephemeral=True)
            return select_callback

        view = discord.ui.View(timeout=None)
        if dropdown:
            select = discord.ui.Select()
            for role in buttonRole:
                option = discord.SelectOption(
                    label=role.label,
                    emoji=role.emoji
                )
                select.append_option(option)
            view.add_item(select)
            select.callback = gen_select_callback(select)
        else:
            for role in buttonRole:
                button = discord.ui.Button(
                    label=role.label,
                    style=role.style,
                    emoji=role.emoji
                )
                button.callback = gen_callback(role.role)
                view.add_item(button)

        await channel.send(message, view=view)

    # Set Events
    @client.event
    async def on_ready():
        print(f'{client.user} active')
        if 'debug' in os.listdir('./'):
            await client.change_presence(activity=discord.Game(name="Vet Simulator"),status=discord.Status.dnd)
            print('Bot Presence changed to \"Playing Vet Simulator\"')
            global debug
            debug = True
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic != None:
                        if 'Bot Info' in channel.topic:
                            await channel.send(embed=discord.Embed(
                                title='Online Status',
                                description=f'Bitey Frank Online Since <t:{str(int(time.time()))}:R> <@&1065773538281259009>',
                                color=discord.Color.green()
                                ))
        else:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my stinky poos"))
            print('Bot Presence changed to \"Watching my stinky poos\"')
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic != None:
                        if 'Bot Info' in channel.topic:
                            await channel.send(embed=discord.Embed(
                                title='Online Status',
                                description=f'Bitey Frank Online Since <t:{str(int(time.time()))}:R>',
                                color=discord.Color.green()
                                ))

        # Channel Detection
        for guild in client.guilds:
            for channel in guild.channels:
                channels.append(channel)

        # Role Detection
        for guild in client.guilds:
            for role in guild.roles:
                roles[f'@{role.name}'] = role
        global rolesLoaded
        rolesLoaded = True

        # Emoji Detection
        for guild in client.guilds:
            for emoji in guild.emojis:
                emojis[f':{emoji.name}:'] = emoji

        # Command Import
        for command in os.listdir('commands'):
            for command in os.listdir('commands'):
                if command.endswith('py'):
                    if '__init__.py' not in command:
                        if 'template.py' not in command:
                            if command not in importedCommands:
                                exec(f'import commands.{command[:-3]}')
                                exec(
                                    f'commands.{command[:-3]}.import_command()')
                                importedCommands.append(command)

        # Send Button Roles
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.topic != None:
                    if 'Button Roles' in channel.topic:
                        await channel.purge()
                        pingRoles = [
                            buttonRole(
                                role=roles['@General Announcement Ping'],
                                style='gray',
                                emoji='🔔'
                            ),
                            buttonRole(
                                role=roles['@DankPods Ping'],
                                style='gray',
                                emoji=printEmoji(':dankpods:')
                            ),
                            buttonRole(
                                role=roles['@Garbage Time Ping'],
                                style='gray',
                                emoji=printEmoji(':tony:')
                            ),
                            buttonRole(
                                role=roles['@Garbage Stream Morn Ping'],
                                style='gray',
                                emoji=printEmoji(':chonkfronk:')
                            ),
                            buttonRole(
                                role=roles['@Garbage Stream Arvo Ping'],
                                style='gray',
                                emoji=printEmoji(':shrek:')
                            ),
                            buttonRole(
                                role=roles['@The Drum Thing Ping'],
                                style='gray',
                                emoji=printEmoji(':drumthing:')
                            ),
                            buttonRole(
                                role=roles['@JMTNTBANG Ping'],
                                style='gray',
                                emoji=printEmoji(':JMTNTBANG:')
                            ),
                            buttonRole(
                                role=roles['@Josh Doesn\'t Play Drums Ping'],
                                style='gray',
                                emoji=printEmoji(':joshdoesntplaydrums:')
                            ),
                            buttonRole(
                                role=roles['@Poll Ping'],
                                style='gray',
                                emoji='📊'
                            )
                        ]
                        tonaRoles = [
                            buttonRole(
                                role=roles['@OG Tona'],
                                style='gray',
                                emoji=printEmoji(':tonatime:')
                            ),
                            buttonRole(
                                role=roles['@Sky Hihi'],
                                style='gray',
                                emoji='☁️'
                            ),
                            buttonRole(
                                role=roles['@Rollo Finito'],
                                style='gray',
                                emoji='🏁'
                            )
                        ]
                        regionRoles = [
                            buttonRole(
                                role=roles['@Freedom Eagles'],
                                style='Dropdown',
                                emoji='🇺🇸'
                            ),
                            buttonRole(
                                role=roles['@Tea Sippers'],
                                style='Dropdown',
                                emoji='🇬🇧'
                            ),
                            buttonRole(
                                role=roles['@Kangaroos'],
                                style='Dropdown',
                                emoji='🇦🇺'
                            ),
                            buttonRole(
                                role=roles['@Meatball Kings'],
                                style='Dropdown',
                                emoji='🇸🇪'
                            ),
                            buttonRole(
                                role=roles['@pain'],
                                style='Dropdown',
                                emoji='🇪🇸'
                            )
                        ]
                        await sendButtonRoles(pingRoles, channel, 'Click a Button to choose from various *Ping Roles*')
                        await sendButtonRoles(tonaRoles, channel, 'Click a Button to choose from various *Tona Roles*')
                        await sendButtonRoles(regionRoles, channel, 'Choose an item from the Dropdown to choose from various *Region Roles*', dropdown=True)

        # Import Assets
        for asset in os.listdir('assets'):
            if asset.endswith(('jpg', 'jpeg', 'png', 'webp', 'gif')):
                assets.append(f'assets/{asset}')

        await tree.sync()

    @client.event
    async def on_member_join(member):
        await memberStatusUpdate(True, member)

    @client.event
    async def on_member_remove(member):
        await memberStatusUpdate(False, member)

    @client.event
    async def on_message(message: discord.Message):
        if client.user in message.mentions:
            if message.author != client.user:
                await message.channel.send(printEmoji(randItem(frankMojis)))
        
        if 'frank' in message.content.lower():
                snarks = open('snarks.txt', 'r')
                global yes
                yes = False
                for snark in snarks:
                    trigger = snark[snark.find('t:')+2:snark.find('r:')-1]
                    response = snark[snark.find('r:')+2:snark.find('u:')-1]
                    if trigger in message.content.lower():
                        if message.author != client.user:
                            async with message.channel.typing():
                                await asyncio.sleep(len(response)/5)
                            if message.channel.last_message == message:
                                await message.channel.send(f'{response}')
                            else:
                                await message.reply(f'{response}')
                            yes = True
                if not yes:
                    if message.author != client.user:
                        await message.channel.send(printEmoji(randItem(frankMojis)))
                snarks.close()

        if message.guild is None and not message.author.bot:
            global threadExists
            threadExists = False
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic != None:
                        if 'DMs' in channel.topic:
                            for thread in channel.threads:
                                if thread.name == f'{message.author.name}#{message.author.discriminator}':
                                    threadExists = True
                                    global threadd
                                    threadd = thread
                            if threadExists == False:
                                newThread = await channel.send(f'`Beginning of Conversation with {message.author.name}`')
                                threadd = await channel.create_thread(name=f'{message.author.name}#{message.author.discriminator}',message=newThread)
                            DMWebhook = webhook(content=message.content, username=message.author.name, avatar=message.author.avatar.url, url=f'https://discord.com/api/webhooks/1072723874648690748/4lkka6Rs41p1xV5r8Jfq2Qbsh16tQ0hrJboMF73BiQwbEqJrmTrbdvACHVZFDMEu1bCC?thread_id={threadd.id}')
                            requests.post(DMWebhook.url,DMWebhook.json)
        if not message.author.bot:
            for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.topic != None:
                            if 'DMs' in channel.topic:
                                for thread in channel.threads:
                                    async for threadMessage in thread.history():
                                        if message == threadMessage:
                                            dm=await guild.get_member_named(thread.name).create_dm()
                                            async with dm.typing():
                                                await asyncio.sleep(len(message.content)/5)
                                            await dm.send(message.content)
                                            break



        if rolesLoaded and not debug:
            await checkChannels()


    # Finalize Bot
    client.run(TOKEN)
