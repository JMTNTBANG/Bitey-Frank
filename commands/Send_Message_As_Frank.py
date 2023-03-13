import bot
import discord


def import_command():

    class messageModal(discord.ui.Modal, title='Create a Poll'):
        message = discord.ui.TextInput(
            label = 'What would you like to send?',
            style = discord.TextStyle.long,
            placeholder = '\"Do you come from a land down under, Where women glow and men plunder?',
            required = True
        )
        async def on_submit(self,Interaction:discord.Interaction):
            await Interaction.channel.send(self.message)
            await Interaction.response.send_message(content='Message Sent!', ephemeral = True)

    # Command Info
    @bot.tree.context_menu(
        name="Send Message As Frank"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction, Member:discord.Member):
        async with Interaction.channel.typing():
            modal = messageModal()
            await Interaction.response.send_modal(modal)