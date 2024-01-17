const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("winners")
    .setDescription(
      "Calculate who guessed correctly on what the iPod has chosen"
    )
    .addStringOption((option) =>
      option
        .setName("poll_message_id")
        .setDescription("Message ID of the Poll")
        .setRequired(true)
    )
    .addIntegerOption((option) =>
      option
        .setName("ipod_winning_number")
        .setDescription("The Winning Number")
        .setRequired(true)
    )
    .addIntegerOption((option) =>
      option
        .setName("reroll_winning_number")
        .setDescription("The Winning Number Following a Re-Roll")
        .setRequired(false)
    ),
  async execute(ctx) {
    // await ctx.deferReply();
    let emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"];
    const poll_message_id = ctx.options.getString("poll_message_id");
    const ipod_winning_number = ctx.options.getInteger("ipod_winning_number");
    const reroll_winning_number = ctx.options.getInteger(
      "reroll_winning_number"
    );
    const embed = new EmbedBuilder().setTitle("Winners");
    let message;
    try {
      message = await ctx.channel.messages.fetch(poll_message_id);
    } catch {
      await ctx.reply("Message Not Found");
    }
    // await ctx.deferReply();
    try {
      for (const emoji of emojis) {
        if (ipod_winning_number == emojis.indexOf(emoji) + 1) {
          const reaction = message.reactions.cache.get(emoji);
          let value = " ";
          reaction.users.cache
            .filter((user) => user.bot == false)
            .each((user) => (value += `${user}\n`));
          embed.addFields({
            name: `iPod Readers! (Number: ${emoji})`,
            value: value,
            inline: false,
          });
        }
        if (reroll_winning_number === emojis.indexOf(emoji) + 1) {
          const reaction = message.reactions.cache.get(emoji);
          let value = " ";
          reaction.users.cache
            .filter((user) => user.bot == false)
            .each((user) => (value += `${user}\n`));
          embed.addFields({
            name: `Re-roll Readers! (Number: ${emoji})`,
            value: value,
            inline: false,
          });
        }
      }
      await ctx.reply({ embeds: [embed] });
    } catch (error) {
      await ctx.reply("Error Has Ocurred")
      console.log(error)
    }
  },
};
