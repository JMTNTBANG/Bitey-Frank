import bot
import discord
global_message: discord.Message


def import_command():
    class MessageModal(discord.ui.Modal, title='Create a Poll'):
        message = discord.ui.TextInput(
            label='What would you like to send?',
            style=discord.TextStyle.long,
            placeholder=':frank3:'
        )

        async def on_submit(self, interaction: discord.Interaction):
            if self.message.value.startswith(':') and self.message.value.endswith(':'):
                emoji = bot.emojis.get(self.message.value)
                if emoji:
                    await global_message.add_reaction(emoji)
                    await interaction.response.send_message(content='Reacted!',
                                                            ephemeral=True)
                else:
                    await interaction.response.send_message(content='Emoji Not Found',
                                                            ephemeral=True)
            else:
                try:
                    await global_message.add_reaction(self.message.value)
                    await interaction.response.send_message(content='Reacted!',
                                                            ephemeral=True)
                except discord.errors.HTTPException as exception:
                    await interaction.response.send_message(content=exception.text,
                                                            ephemeral=True)

    # Command Info
    @bot.tree.context_menu(
        name="React As Frank"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, message: discord.Message):
        global global_message
        global_message = message
        modal = MessageModal()
        await interaction.response.send_modal(modal)
