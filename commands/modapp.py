import bot
import discord
import datetime


def import_command():
    class ModAppModal(discord.ui.Modal, title="Garbage Stream Discord Mod Application"):
        activity = discord.ui.TextInput(
            label="How often are you online in the server?"
        )
        reasoning = discord.ui.TextInput(
            label="Why do you think you should become a mod?"
        )
        reasoning2 = discord.ui.TextInput(
            label="Why do you want to become a mod?"
        )
        scenario = discord.ui.TextInput(
            label="Scenario: A New user starts spamming slurs in",
            default="general, what do you do to de-escalate the situation?"
        )
        comments = discord.ui.TextInput(
            label="Any extra comments for the mod team?",
            required=False
        )

        async def on_submit(self, interaction: discord.Interaction):
            report = discord.Embed(
                title="Mod Application",
                timestamp=datetime.datetime.now()
            )
            report.set_author(name=interaction.user.display_name, url=interaction.user.avatar.url, icon_url=interaction.user.avatar.url)
            report.add_field(name=self.activity.label, value=self.activity.value, inline=False)
            report.add_field(name=self.reasoning.label, value=self.reasoning.value, inline=False)
            report.add_field(name=self.reasoning2.label, value=self.reasoning2.value, inline=False)
            report.add_field(name=self.scenario.label + " " + self.scenario.default, value=self.scenario.value, inline=False)
            report.add_field(name=self.comments.label, value=self.comments.value, inline=False)
            for guild in bot.client.guilds:
                for channel in guild.text_channels:
                    if channel.topic and "Mods" in channel.topic:
                        await channel.send(embed=report)
            await interaction.response.send_message("Mod Application sent! A Mod will contact you soon if they have good news.", ephemeral=True)

    # Command Info
    @bot.tree.command(
        name="modapp",
        description="Description here"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        mod_app = ModAppModal()
        await interaction.response.send_modal(mod_app)
