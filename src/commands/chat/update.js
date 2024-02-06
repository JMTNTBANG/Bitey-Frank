const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("update")
    .setDescription("Update the Bot to latest commits"),
  async execute(ctx) {
    ctx.reply("Updating...");
    throw new Error("Admin Requested Bot Update");
  },
};
