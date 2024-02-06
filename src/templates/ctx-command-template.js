const {
  ContextMenuCommandBuilder,
  ApplicationCommandType,
} = require("discord.js");

module.exports = {
  data: new ContextMenuCommandBuilder()
    .setName("INSERT NAME HERE")
    .setType(ApplicationCommandType), // Can be .Message or .User
  async execute(ctx) {
    // Insert Code Here
  },
};
