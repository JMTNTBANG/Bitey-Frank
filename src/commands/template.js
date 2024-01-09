const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder().setName("Name").setDescription("Description"),
  async execute(ctx) {},
};
