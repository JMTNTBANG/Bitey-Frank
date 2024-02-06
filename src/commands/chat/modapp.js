const fs = require("fs");
const { specialChannels } = require("../../config.json")
const {
  SlashCommandBuilder,
  ActionRowBuilder,
  ModalBuilder,
  TextInputBuilder,
  TextInputStyle,
  EmbedBuilder,
} = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("modapp")
    .setDescription("Apply to be a mod for Garbage Stream Discord"),
  async execute(ctx) {
    const modapp_modal = new ModalBuilder()
      .setCustomId(`modapp-${ctx.user.id}`)
      .setTitle("Garbage Stream Discord Mod Application")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("activity-textbox")
            .setLabel("How often are you online in the server?")
            .setStyle(TextInputStyle.Paragraph)
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("reasoning-textbox")
            .setLabel("Why do you think you should become a mod?")
            .setStyle(TextInputStyle.Paragraph)
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("reasoning2-textbox")
            .setLabel("Why do you want to become a mod?")
            .setStyle(TextInputStyle.Paragraph)
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("scenario-textbox")
            .setLabel("Scenario: A New user starts spamming slurs in")
            .setValue("general, what do you do to de-escalate the situation?")
            .setStyle(TextInputStyle.Paragraph)
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("comments-textbox")
            .setLabel("Any extra comments for the mod team?")
            .setStyle(TextInputStyle.Paragraph)
            .setRequired(false)
        )
      );
    await ctx.showModal(modapp_modal);
    const modalFilter = (ctx) => ctx.customId === `modapp-${ctx.user.id}`;
    ctx
      .awaitModalSubmit({ filter: modalFilter, time: 600_000 })
      .then(async (modal) => {
        await ctx.guild.channels
          .fetch(specialChannels.modapps)
          .then((channel) =>
            channel.send({
              embeds: [
                new EmbedBuilder()
                  .setTitle("Mod Application")
                  .setAuthor({
                    name: ctx.user.username,
                    iconURL: ctx.user.displayAvatarURL(),
                  })
                  .setTimestamp(new Date(Date.now()))
                  .addFields(
                    {
                      name: "How often are you online in the server?",
                      value: modal.fields.getTextInputValue("activity-textbox"),
                      inline: false,
                    },
                    {
                      name: "Why do you think you should become a mod?",
                      value:
                        modal.fields.getTextInputValue("reasoning-textbox"),
                      inline: false,
                    },
                    {
                      name: "Why do you want to become a mod?",
                      value:
                        modal.fields.getTextInputValue("reasoning2-textbox"),
                      inline: false,
                    },
                    {
                      name: "Scenario: A New user starts spamming slurs in general, what do you do to de-escalate the situation?",
                      value: modal.fields.getTextInputValue("scenario-textbox"),
                      inline: false,
                    },
                    {
                      name: "Any extra comments for the mod team?",
                      value: modal.fields.getTextInputValue("comments-textbox"),
                      inline: false,
                    }
                  ),
              ],
            })
          );
        modal.reply({content: "Mod App Sent!", ephemeral: true})
      });
  },
};
