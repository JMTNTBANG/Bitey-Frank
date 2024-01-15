const {
  StringSelectMenuBuilder,
  StringSelectMenuOptionBuilder,
  ActionRowBuilder,
  Events,
  ComponentType,
  ModalBuilder,
  TextInputBuilder,
  TextInputStyle,
  EmbedBuilder,
  SlashCommandBuilder,
} = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("poll")
    .setDescription("Create A Poll"),
  async execute(ctx) {
    const message_modal = new ModalBuilder()
      .setCustomId(`message-${ctx.user.id}`)
      .setTitle("Set Message")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("message_textbox")
            .setLabel("Message")
            .setStyle(TextInputStyle.Paragraph)
            .setPlaceholder("@Poll Ping")
            .setRequired(true)
        )
      );
    const question_modal = new ModalBuilder()
      .setCustomId(`question-${ctx.user.id}`)
      .setTitle("Set Question")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("question_textbox")
            .setLabel("Question")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Does Frank Rule All?")
            .setRequired(true)
        )
      );
    const description_modal = new ModalBuilder()
      .setCustomId(`description-${ctx.user.id}`)
      .setTitle("Set Description")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("description_textbox")
            .setLabel("Description")
            .setStyle(TextInputStyle.Paragraph)
            .setPlaceholder(
              "This Answer may or may not determine your status in this server......"
            )
            .setRequired(true)
        )
      );
    const options1_modal = new ModalBuilder()
      .setCustomId(`options-pg1-${ctx.user.id}`)
      .setTitle("Set Options 1-5")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option1_textbox")
            .setLabel("Option 1")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option2_textbox")
            .setLabel("Option 2")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(true)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option3_textbox")
            .setLabel("Option 3")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option4_textbox")
            .setLabel("Option 4")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option5_textbox")
            .setLabel("Option 5")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        )
      );
    const options2_modal = new ModalBuilder()
      .setCustomId(`options-pg2-${ctx.user.id}`)
      .setTitle("Set Options 6-10")
      .addComponents(
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option6_textbox")
            .setLabel("Option 6")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option7_textbox")
            .setLabel("Option 7")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option8_textbox")
            .setLabel("Option 8")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option9_textbox")
            .setLabel("Option 9")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        ),
        new ActionRowBuilder().addComponents(
          new TextInputBuilder()
            .setCustomId("option10_textbox")
            .setLabel("Option 10")
            .setStyle(TextInputStyle.Short)
            .setPlaceholder("Yes")
            .setRequired(false)
        )
      );
    const poll_element_selector = new ActionRowBuilder().addComponents(
      new StringSelectMenuBuilder()
        .setCustomId("poll_element_selector")
        .setPlaceholder("Choose An Option")
        .addOptions(
          new StringSelectMenuOptionBuilder()
            .setLabel("Set Message")
            .setValue("message")
            .setEmoji("🗨️"),
          new StringSelectMenuOptionBuilder()
            .setLabel("Set Question")
            .setValue("question")
            .setEmoji("❓"),
          new StringSelectMenuOptionBuilder()
            .setLabel("Set Description")
            .setValue("description")
            .setEmoji("📄"),
          new StringSelectMenuOptionBuilder()
            .setLabel("Set Options (1-5)")
            .setValue("options-pg1")
            .setEmoji("🔢"),
          new StringSelectMenuOptionBuilder()
            .setLabel("Set Options (6-10)")
            .setValue("options-pg2")
            .setEmoji("🔢"),
          new StringSelectMenuOptionBuilder()
            .setLabel("Send")
            .setValue("send")
            .setEmoji("✅")
        )
    );
    let poll_embed_preview = new EmbedBuilder()
      .setAuthor({
        name: ctx.user.username,
        iconURL: ctx.user.displayAvatarURL(),
      })
      .setTitle("null")
      .setDescription("null");
    const poll_builder = await ctx.reply({
      content: "```\nPoll Builder```\n### Preview:\nnull",
      components: [poll_element_selector],
      embeds: [poll_embed_preview],
      ephemeral: true,
    });
    const poll_info = {
      message: "null",
      question: "null",
      description: "null",
      fields1: [],
      fields2: [],
    };
    const poll_channel = ctx.channel;
    const collector = poll_builder.createMessageComponentCollector({
      componentType: ComponentType.StringSelect,
    });
    collector.on("collect", async (ctx2) => {
      const selection = ctx2.values[0];
      if (selection == "message") {
        await ctx2.showModal(message_modal);
      } else if (selection == "question") {
        await ctx2.showModal(question_modal);
      } else if (selection == "description") {
        await ctx2.showModal(description_modal);
      } else if (selection == "options-pg1") {
        await ctx2.showModal(options1_modal);
      } else if (selection == "options-pg2") {
        await ctx2.showModal(options2_modal);
      } else if (selection == "send") {
        ctx2.reply({ content: "Poll Sent!", ephemeral: true });
        poll = await poll_channel.send({
          content: poll_info.message,
          embeds: [poll_embed_preview],
        });
        for (const field of poll_info.fields1) {
          poll.react(field[0]);
        }
        for (const field of poll_info.fields2) {
          poll.react(field[0]);
        }
      }
      const modalFilter = (ctx) =>
        ctx.customId === `${selection}-${ctx.user.id}`;
      ctx
        .awaitModalSubmit({ filter: modalFilter, time: 600_000 })
        .then((ctx) => {
          if (selection == "message") {
            poll_info.message = ctx.fields.getTextInputValue("message_textbox");
            ctx.reply({ content: "Message Set!", ephemeral: true });
          } else if (selection == "question") {
            poll_info.question =
              ctx.fields.getTextInputValue("question_textbox");
            ctx.reply({ content: "Question Set!", ephemeral: true });
          } else if (selection == "description") {
            poll_info.description = ctx.fields.getTextInputValue(
              "description_textbox"
            );
            ctx.reply({ content: "Description Set!", ephemeral: true });
          } else if (selection == "options-pg1") {
            const fields = [
              ["1️⃣", ctx.fields.getTextInputValue("option1_textbox"), false],
              ["2️⃣", ctx.fields.getTextInputValue("option2_textbox"), false],
            ];
            if (ctx.fields.getTextInputValue("option3_textbox").length > 0) {
              fields.push([
                "3️⃣",
                ctx.fields.getTextInputValue("option3_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option4_textbox").length > 0) {
              fields.push([
                "4️⃣",
                ctx.fields.getTextInputValue("option4_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option5_textbox").length > 0) {
              fields.push([
                "5️⃣",
                ctx.fields.getTextInputValue("option5_textbox"),
                false,
              ]);
            }
            poll_info.fields1 = fields;
            ctx.reply({ content: "Options 1-5 Set!", ephemeral: true });
          } else if (selection == "options-pg2") {
            const fields = [];
            if (ctx.fields.getTextInputValue("option6_textbox").length > 0) {
              fields.push([
                "6️⃣",
                ctx.fields.getTextInputValue("option6_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option7_textbox").length > 0) {
              fields.push([
                "7️⃣",
                ctx.fields.getTextInputValue("option7_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option8_textbox").length > 0) {
              fields.push([
                "8️⃣",
                ctx.fields.getTextInputValue("option8_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option9_textbox").length > 0) {
              fields.push([
                "9️⃣",
                ctx.fields.getTextInputValue("option9_textbox"),
                false,
              ]);
            }
            if (ctx.fields.getTextInputValue("option10_textbox").length > 0) {
              fields.push([
                "🔟",
                ctx.fields.getTextInputValue("option10_textbox"),
                false,
              ]);
            }
            poll_info.fields2 = fields;
            ctx.reply({ content: "Options 6-10 Set!", ephemeral: true });
          }
          poll_embed_preview
            .setTitle(`Poll: ${poll_info.question}`)
            .setDescription(poll_info.description)
            .setFields();
          for (const field of poll_info.fields1) {
            poll_embed_preview.addFields({
              name: field[0],
              value: field[1],
              inline: field[2],
            });
          }
          for (const field of poll_info.fields2) {
            poll_embed_preview.addFields({
              name: field[0],
              value: field[1],
              inline: field[2],
            });
          }
          poll_builder.edit({
            content: `\`\`\`\nPoll Builder\`\`\`\n### Preview:\n${poll_info.message}`,
            embeds: [poll_embed_preview],
          });
        });
    });
  },
};
