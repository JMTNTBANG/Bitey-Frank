const {
  ContextMenuCommandBuilder,
  ApplicationCommandType,
  ModalBuilder,
  ActionRowBuilder,
  TextInputBuilder,
  TextInputStyle,
} = require("discord.js");

module.exports = {
  data: new ContextMenuCommandBuilder()
    .setName("Send Message As Frank")
    .setType(ApplicationCommandType.User), // Can be .Message or .User
  async execute(ctx) {
    const modal = new ModalBuilder()
      .setCustomId(`smaf-${ctx.user.id}`)
      .setTitle("Send Message As Frank")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("smaf_textbox")
            .setLabel("Message")
            .setStyle(TextInputStyle.Paragraph)
            .setPlaceholder("Frank is Dominance")
            .setRequired(true)
        )
      );
    await ctx.channel.sendTyping();
    await ctx.showModal(modal);
    const modalFilter = (ctx) => ctx.customId === `smaf-${ctx.user.id}`;
    ctx.awaitModalSubmit({ filter: modalFilter, time: 600_000 }).then((ctx) => {
      ctx.channel.send(ctx.fields.getTextInputValue("smaf_textbox"));
      ctx.reply({ content: "Message Sent!", ephemeral: true });
    });
  },
};
