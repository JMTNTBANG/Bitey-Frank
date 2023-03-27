import bot
import discord
global_message: discord.Message


def import_command():
    class MessageModal(discord.ui.Modal,
                       title='Reply as Frank'):
        message = discord.ui.TextInput(
            label='What would you like to send?',
            style=discord.TextStyle.long,
            placeholder='\"Do you come from a land down under, Where women glow and men plunder?'
        )

        async def on_submit(self, interaction: discord.Interaction):
            await global_message.reply(self.message.value)
            await interaction.response.send_message(content='Message Sent!',
                                                    ephemeral=True)

    # Command Info
    @bot.tree.context_menu(
        name="Reply As Frank"
    )
    # Code to Run Here
    async def reply_as_frank(interaction: discord.Interaction, message: discord.Message):
        global global_message
        global_message = message
        async with interaction.channel.typing():
            modal = MessageModal()
            await interaction.response.send_modal(modal)
