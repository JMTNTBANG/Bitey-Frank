import bot
import discord


def import_command():
    class messageModal(discord.ui.Modal, title='Create a Poll'):
        message = discord.ui.TextInput(
            label = 'What would you like to send?',
            style = discord.TextStyle.long,
            placeholder = ':frank3:',
            required = True
        )
        async def on_submit(self,Interaction:discord.Interaction):
            if self.message.value.startswith(':') and self.message.value.endswith(':'):
                emoji = bot.emojis.get(self.message.value)
                if emoji:
                    await message.add_reaction(emoji)
                    await Interaction.response.send_message(content='Reacted!', ephemeral = True)
                else:
                    await Interaction.response.send_message(content='Emoji Not Found', ephemeral=True)
            else:
                try:
                    await message.add_reaction(self.message.value)
                    await Interaction.response.send_message(content='Reacted!', ephemeral = True)
                except:
                    await Interaction.response.send_message(content='Emoji Not Found', ephemeral=True)

    # Command Info
    @bot.tree.context_menu(
        name="React As Frank"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction, Message:discord.Message):
        global message
        message = Message
        modal = messageModal()
        await Interaction.response.send_modal(modal)