import asyncio
import os
import re
import time
from os import getenv
from random import choice
from typing import Any

import discord
import requests
from discord import Client
from discord.app_commands import CommandTree
from dotenv import load_dotenv
import csv

from lyricsgenius import Genius

GeniusAPI = None


# Set Classes
class ButtonRole:
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


class Webhook:
    def __init__(self, content, username, avatar, url, embeds=None, attachments=None,) -> None:
        self.content = content
        self.username = username
        self.avatar = avatar
        self.url = url
        if embeds is not None:
            self.embeds = embeds
        if attachments is not None:
            self.attachments = attachments
        self.json = {
            "content": self.content,
            "username": self.username,
            "avatar_url": self.avatar
        }


# Set Bot Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Set Client Variables
client = discord.Client(intents=intents)
tree: CommandTree[Client | Any] = discord.app_commands.CommandTree(client)

# Set Dynamic Variables
channels: list[
    discord.VoiceChannel |
    discord.StageChannel |
    discord.ForumChannel |
    discord.TextChannel |
    discord.CategoryChannel
    ] = []
roles: dict[str, discord.Role] = {}
emojis: dict[str, discord.Emoji] = {}
assets: list[str] = []
imported_commands: list[str] = []
rolesLoaded: bool = False
debug: bool = False
buffer = {
    "song_name": "",
    "song_artist": "",
    "song_lyrics": ""
}

# Set Static Variables
frank_emojis = [
    ':chonkfronk:',
    ':frank3:',
    ':sneakyfrank:',
    ':hideyhole:',
    ':jpeg:'
]


# Set Functions/Lambdas
def print_emoji(emoji: str):
    return f'<:{emojis[emoji].name}:{emojis[emoji].id}>'


async def member_status_update(in_server: bool, member):
    for channel in client.get_all_channels():
        if channel.guild == member.guild and member.guild.system_channel == channel:
            if isinstance(channel, discord.TextChannel):
                if in_server:
                    await channel.send(print_emoji(choice(frank_emojis)))
                else:
                    await channel.send(f'{print_emoji(":frank:")}7 {member.mention}')
                break


def strip_non_alpha(str):
    mod_string = ""
    for elem in str:
        if elem.isalnum() or elem == ' ' or elem == '\n':
            mod_string += elem
    return mod_string


# Regex to match frank with repeated characters
LONG_FRANK_REGEX = re.compile(r"f+r+a+n+k+")


def start():
    # Load Tokens
    load_dotenv()
    if 'debug' in os.listdir('./'):
        token = getenv('DEBUGTOKEN')
    else:
        token = getenv('TOKEN')
    if token is None:
        print('GIMMIE YO GODDAMN TOKEN B***CH')
        raise

    genius_token = getenv('GENIUS')
    if genius_token is None:
        print('Please add the Genius API Token in .env')
        raise
    try:
        GeniusAPI = Genius(genius_token, remove_section_headers=True, verbose=False)
    except TypeError:
        raise ValueError('Please try a new Access Token as this one did not work...')

    # Bot Code
    @client.event
    async def on_ready():
        print(f'{client.user} active')

        # Debug Mode Detection
        if 'debug' in os.listdir('./'):
            await client.change_presence(activity=discord.Game(name="Vet Simulator"), status=discord.Status.dnd)
            print('Bot Presence changed to \"Playing Vet Simulator\"')
            global debug
            debug = True
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'Github' in channel.topic:
                            await channel.send("```"
                                               "Applied previous commits"
                                               "```")
        else:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                   name="my stinky poos"))
            print('Bot Presence changed to \"Watching my stinky poos\"')
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'Github' in channel.topic:
                            await channel.send("```"
                                               "Applied previous commits"
                                               "```")

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
            if command.endswith('py'):
                if '__init__.py' not in command:
                    if 'template.py' not in command:
                        if command not in imported_commands:
                            exec(f'import commands.{command[:-3]}')
                            exec(
                                f'commands.{command[:-3]}.import_command()')
                            imported_commands.append(command)

        # Import Assets
        for asset in os.listdir('assets'):
            if asset.endswith(('jpg', 'jpeg', 'png', 'webp', 'gif')):
                assets.append(f'assets/{asset}')

        await tree.sync()

    ### MODULES ###
    # Member Announcements
    @client.event
    async def on_member_join(member):
        await member_status_update(True, member)

    @client.event
    async def on_member_remove(member):
        await member_status_update(False, member)

    # Message Based Modules
    @client.event
    async def on_message(message: discord.Message):

        # Respond to Pings to the Bot
        if client.user in message.mentions:
            if message.author != client.user:
                await message.channel.send(print_emoji(choice(frank_emojis)))

        # Respond to Mentions of Frank or Snark Triggers as defined in snarks.csv
        if LONG_FRANK_REGEX.search(message.content.casefold()) is not None:
            with open('snarks.csv', 'r') as file:
                snarks = csv.reader(file, delimiter=',')
                is_snark = False
                for snark in snarks:
                    if not snark[0] == 'Trigger' and not snark[1] == 'Response' and not snark[2] == 'User':
                        trigger = snark[0]
                        response = snark[1]
                        if trigger in message.content.lower():
                            if message.author != client.user:
                                async with message.channel.typing():
                                    await asyncio.sleep(len(response)/5)
                                if message.channel.last_message == message:
                                    await message.channel.send(f'{response}')
                                else:
                                    await message.reply(f'{response}')
                                is_snark = True
                if not is_snark:
                    if message.author != client.user:
                        await message.channel.send(print_emoji(choice(frank_emojis)))

        # Forward DMS to the bot to channel threads on server
        if message.guild is None and not message.author.bot:
            thread_exists = False
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'DMs' in channel.topic:
                            for thread in channel.threads:
                                if thread.name == f'{message.author.name}#{message.author.discriminator}':
                                    thread_exists = True
                                    break
                            if not thread_exists:
                                thread_message = await channel.send(f'`Beginning of Conversation with {message.author.name}`')
                                thread = await channel.create_thread(name=f'{message.author.name}#{message.author.discriminator}',
                                                                     message=thread_message)
                            dm_webhook = Webhook(content=message.content,
                                                 username=message.author.name,
                                                 avatar=message.author.avatar.url,
                                                 url=f'https://discord.com/api/webhooks/1072723874648690748/4lkka6Rs41p1xV5r8Jfq2Qbsh16tQ0hrJboMF73BiQwbEqJrmTrbdvACHVZFDMEu1bCC?thread_id={thread.id}')
                            requests.post(dm_webhook.url, dm_webhook.json)
        if not message.author.bot:
            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if 'DMs' in channel.topic:
                            for thread in channel.threads:
                                async for threadMessage in thread.history():
                                    if message == threadMessage:
                                        dm = await guild.get_member_named(thread.name).create_dm()
                                        async with dm.typing():
                                            await asyncio.sleep(len(message.content)/5)
                                        await dm.send(message.content)
                                        break

        # Frank Sing-Along Module
        if not message.author.bot:
            for guild in client.guilds:
                if guild == message.guild:
                    for channel in guild.text_channels:
                        if channel.topic is not None:
                            if "Current Song:" in channel.topic:
                                if message.channel == channel:
                                    title = channel.topic[15:channel.topic.find(" by ")]
                                    artist = channel.topic[channel.topic.find(" by ")+4:]
                                    if buffer["song_name"] != title or buffer["song_artist"] != artist:
                                        song = GeniusAPI.search_song(title, artist)
                                        lyrics = str(strip_non_alpha(song.lyrics).lower())
                                        buffer["song_name"] = title
                                        buffer["song_artist"] = artist
                                        buffer["song_lyrics"] = lyrics
                                    else:
                                        lyrics = buffer["song_lyrics"]
                                    query = str(strip_non_alpha(message.content).lower())

                                    spot1 = lyrics.find(query)
                                    lyric1 = lyrics[spot1:]
                                    spot2 = lyric1.find("\n") + spot1

                                    lyric1 = lyrics[spot2 + 1:]
                                    spot1 = spot2 + 1
                                    spot2 = lyric1.find("\n") + spot1

                                    next_lyric = lyrics[spot1:spot2]
                                    if next_lyric != "":
                                        async with message.channel.typing():
                                            await asyncio.sleep(len(next_lyric) / 5)
                                        await channel.send(next_lyric)
                                    buffer["song_lyrics"] = buffer["song_lyrics"][spot2:]

    client.run(token)
