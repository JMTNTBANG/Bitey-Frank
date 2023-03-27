import bot
import discord

global_message: discord.Message


def import_command():

    class MessageModal(discord.ui.Modal, title='Edit Message'):
        message = discord.ui.TextInput(
            label='What would you like to send?',
            style=discord.TextStyle.long,
            placeholder='\"Do you come from a land down under, Where women glow and men plunder?'
        )

        async def on_submit(self, interaction: discord.Interaction):
            await global_message.edit(content=self.message.value)
            await interaction.response.send_message(content='Message Edited!',
                                                    ephemeral=True)

    # Command Info
    @bot.tree.context_menu(
        name="Edit Frank Message"
    )
    # Code to Run Here
    async def edit_frank_message(interaction: discord.Interaction, message: discord.Message):
        if message.author == bot.client.user:
            global global_message
            global_message = message
            async with interaction.channel.typing():
                MessageModal.message.default = message.content
                modal = MessageModal()
                await interaction.response.send_modal(modal)
        else:
            await interaction.response.send_message('Not a Bot Message')
