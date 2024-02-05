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
    .setName("Edit Frank Message")
    .setType(ApplicationCommandType.Message), // Can be .Message or .User
  async execute(ctx) {
    if (ctx.targetMessage.author !== ctx.client.user) {
      ctx.reply("Not a Frank Message");
    } else {
      const modal = new ModalBuilder()
        .setCustomId(`efm-${ctx.user.id}`)
        .setTitle("Reply As Frank")
        .addComponents(
          new ActionRowBuilder().addComponents(
            new TextInputBuilder()
              .setCustomId("efm_textbox")
              .setLabel("Message")
              .setStyle(TextInputStyle.Paragraph)
              .setPlaceholder("Frank is Dominance")
              .setValue(ctx.targetMessage.content)
              .setRequired(true)
          )
        );
      await ctx.channel.sendTyping();
      await ctx.showModal(modal);
      const modalFilter = (ctx) => ctx.customId === `efm-${ctx.user.id}`;
      ctx
        .awaitModalSubmit({ filter: modalFilter, time: 600_000 })
        .then((ctx2) => {
          ctx.targetMessage.edit(ctx2.fields.getTextInputValue("efm_textbox"));
          ctx2.reply({ content: "Message Edited!", ephemeral: true });
        });
    }
  },
};
