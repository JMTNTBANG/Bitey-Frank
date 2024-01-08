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
        await interaction.response.send_message("Calculating... (This may take awhile depending on how many messages there are)")
        result_msg = await interaction.channel.send(".")
        blank = "."
        channels = []
        total_message_count = 0
        for channel in interaction.guild.text_channels:
            message_count = 0
            async for message in channel.history(limit=None):
                message_count += 1
                total_message_count += 1
            channels.append({"mention": channel.mention, "count": message_count})
            blank += "."
            await result_msg.edit(content=blank)
        message = ""
        message += f"## Total Server Messages: {total_message_count}\n"

        def key(e):
            return e['count']
        channels.sort(key=key, reverse=True)
        for channel in channels:
            message += f"{channel['mention']}: {channel['count']} Messages\n"
        embed = discord.Embed(title="Channel Message Statistics", description=message)
        await result_msg.edit(content="Completed!", embed=embed)
        await result_msg.reply(content=interaction.user.mention)
