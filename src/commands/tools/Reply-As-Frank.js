const {
  ContextMenuCommandBuilder,
  ApplicationCommandType,
  ModalBuilder,
  ActionRowBuilder,
  TextInputBuilder,
  TextInputStyle
} = require("discord.js");

module.exports = {
  data: new ContextMenuCommandBuilder()
    .setName("Reply As Frank")
    .setType(ApplicationCommandType.Message), // Can be .Message or .User
  async execute(ctx) {
    const modal = new ModalBuilder()
      .setCustomId(`raf-${ctx.user.id}`)
      .setTitle("Reply As Frank")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("raf_textbox")
            .setLabel("Message")
            .setStyle(TextInputStyle.Paragraph)
            .setPlaceholder("Frank is Dominance")
            .setRequired(true)
        )
      );
    await ctx.channel.sendTyping()
    await ctx.showModal(modal)
    const modalFilter = (ctx) => ctx.customId === `raf-${ctx.user.id}`;
    ctx.awaitModalSubmit({ filter: modalFilter, time: 600_000 }).then((ctx2) => {
      ctx.targetMessage.reply(ctx2.fields.getTextInputValue("raf_textbox"));
      ctx2.reply({ content: "Message Sent!", ephemeral: true });
    });
  },
};
