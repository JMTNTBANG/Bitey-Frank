const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("INSERT NAME HERE")
    .setDescription("INSERT DESCRIPTION HERE"),
  async execute(ctx) {
    // Insert Code Here
  },
};
