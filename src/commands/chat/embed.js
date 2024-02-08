const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("embed")
    .setDescription("Create an Embed")
    .addStringOption((option) =>
      option
        .setName("title")
        .setDescription("The Title of the Embed")
        .setRequired(true)
    )
    .addStringOption((option) =>
      option
        .setName("description")
        .setDescription("The Content of the Embed")
        .setRequired(true)
    ),
  async execute(ctx) {
    const embed = new EmbedBuilder()
      .setTitle(ctx.options.getString("title"))
      .setDescription(ctx.options.getString("description"))
      .setAuthor({
        name: ctx.user.username,
        iconURL: ctx.user.displayAvatarURL(),
      })
      .setTimestamp(new Date(Date.now()));
    await ctx.reply({embeds:[embed]})  
  },
};
