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
    .setName("React As Frank")
    .setType(ApplicationCommandType.Message), // Can be .Message or .User
  async execute(ctx) {
    const modal = new ModalBuilder()
      .setCustomId(`reaf-${ctx.user.id}`)
      .setTitle("React As Frank")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("reaf_textbox")
            .setLabel("Message")
            .setStyle(TextInputStyle.Paragraph)
            .setPlaceholder(
              "Use Unicode Emojis (😀) or Type in the escaped code (<:frank3:1040422477433675857>)"
            )
            .setRequired(true)
        )
      );
    await ctx.showModal(modal);
    const modalFilter = (ctx) => ctx.customId === `reaf-${ctx.user.id}`;
    ctx
      .awaitModalSubmit({ filter: modalFilter, time: 600_000 })
      .then(async (ctx2) => {
        try {
          await ctx.targetMessage.react(
            ctx2.fields.getTextInputValue("reaf_textbox")
          );
          await ctx2.reply({ content: "Reaction Sent!", ephemeral: true });
        } catch {
          await ctx2.reply({ content: "Not a Valid Emoji", ephemeral: true });
        }
      });
  },
};
