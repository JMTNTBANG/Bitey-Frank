const { Events } = require("discord.js");

module.exports = {
  name: Events.InteractionCreate,
  async execute(ctx) {
    const command = ctx.client.commands.get(ctx.commandName);
    if (command == null) return;
    await command.execute(ctx);
  },
};
