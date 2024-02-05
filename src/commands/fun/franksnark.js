const fs = require("fs");
const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("franksnark")
    .setDescription("Make Frank Snarky")
    .addSubcommand((subcommand) =>
      subcommand
        .setName("set")
        .setDescription("Create a phrase that Frank will snarkily respond to")
        .addStringOption((option) =>
          option
            .setName("trigger")
            .setRequired(true)
            .setDescription("The Phrase Frank will Respond to")
        )
        .addStringOption((option) =>
          option
            .setName("response")
            .setRequired(true)
            .setDescription("The Phrase Frank will Respond with")
        )
    )
    .addSubcommand((subcommand) =>
      subcommand
        .setName("list")
        .setDescription("List all of the phrases Frank responds Snarkily to")
        .addNumberOption((option) =>
          option.setName("page").setRequired(true).setDescription("Page Number")
        )
    ),

  async set(ctx, trigger, response) {
    var configFile = JSON.parse(fs.readFileSync("./config.json").toString());
    configFile.frankSnarks.push({
      trigger: trigger,
      response: response,
      creator: ctx.user.id,
    });
    fs.writeFileSync("./config.json", JSON.stringify(configFile, "", 2));
    await ctx.reply({
      content: `Frank will now respond to \`${trigger}\` with \`${response}\``,
      ephemeral: true,
    });
  },

  async list(ctx, page) {
    var configFile = JSON.parse(fs.readFileSync("./config.json").toString());
    if (page <= Math.ceil(configFile.frankSnarks.length / 20)) {
      const embed = new EmbedBuilder().setTitle(
        `Frank Snarks: Page ${page}/${Math.ceil(
          configFile.frankSnarks.length / 20
        )}`
      );
      for (const snark of configFile.frankSnarks.slice(
        page * 20 - 20,
        page * 20
      )) {
        embed.addFields({
          name: `Trigger: \`${snark.trigger}\``,
          value: `Response: \`${snark.response}\`\nCreator: <@${snark.creator}>`,
          inline: false,
        });
      }
      await ctx.reply({ embeds: [embed] });
    } else {
      ctx.reply({
        content: `Theres only ${Math.ceil(
          configFile.frankSnarks.length / 20
        )} Pages`,
        ephemeral: true,
      });
    }
  },

  async execute(ctx) {
    let subcommand = ctx.options.getSubcommand();
    if (subcommand === "set") {
      await this.set(
        ctx,
        ctx.options.getString("trigger"),
        ctx.options.getString("response")
      );
    } else if (subcommand === "list") {
      await this.list(ctx, ctx.options.getNumber("page"));
    }
  },
};
