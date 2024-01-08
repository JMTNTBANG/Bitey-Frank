import bot
import discord


def import_command():
    # Command Info
    @bot.tree.command(
        name="channelstat",
        description="Get the total messages of each channel"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        response = "Calculating"
        await interaction.response.send_message(response)
        channels = []
        for channel in interaction.guild.text_channels:
            message_count = 0
            async for message in channel.history(limit=None):
                message_count += 1
            channels.append({"mention": channel.mention, "count": message_count})
            response += "."
            await interaction.edit_original_response(content=response)
        message = ""

        def key(e):
            return e['count']
        channels.sort(key=key, reverse=True)
        for channel in channels:
            message += f"{channel['mention']}: {channel['count']} Messages\n"
        embed = discord.Embed(title="Channel Message Statistics", description=message)
        await interaction.edit_original_response(content="Completed!", embed=embed)
