import bot
import discord


def import_command():

    class MessageModal(discord.ui.Modal, title='Create a Poll'):
        message = discord.ui.TextInput(
            label='What would you like to send?',
            style=discord.TextStyle.long,
            placeholder='\"Do you come from a land down under, Where women glow and men plunder?'
        )

        async def on_submit(self, interaction: discord.Interaction):
            await interaction.channel.send(self.message)
            await interaction.response.send_message(content='Message Sent!',
                                                    ephemeral=True)

    # Command Info
    @bot.tree.context_menu(
        name="Send Message As Frank"
    )
    # Code to Run Here
    async def send_message_as_frank(interaction: discord.Interaction, member: discord.Member):
        async with interaction.channel.typing():
            modal = MessageModal()
            await interaction.response.send_modal(modal)
