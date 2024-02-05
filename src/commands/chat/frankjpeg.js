const path = require("path");
const { assets } = require("../../index.js");
const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("frankjpeg")
    .setDescription("Choose a specific Frank jpeg")
    .addSubcommand((subcommand) =>
      subcommand
        .setName("num")
        .setDescription("Choose a Frank jpeg by number")
        .addNumberOption((option) =>
          option
            .setName("number")
            .setRequired(true)
            .setDescription(
              "Type in the number based on entries in /frankjpeg list"
            )
        )
    )
    .addSubcommand((subcommand) =>
      subcommand
        .setName("name")
        .setDescription("Choose a Frank jpeg by name")
        .addStringOption((option) =>
          option
            .setName("name")
            .setRequired(true)
            .setDescription(
              "Type the name you found in /frankjpeg list (including extension)"
            )
        )
    )
    .addSubcommand((subcommand) =>
      subcommand.setName("list").setDescription("List Frank jpegs")
    ),

  async num(ctx, num) {
    let picture = path.join(__dirname, "../../../assets/images", assets[num]);
    await ctx.reply({ files: [{ attachment: picture }] });
  },

  async name(ctx, name) {
    let picture = path.join(__dirname, "../../../assets/images", name);
    await ctx.reply({ files: [{ attachment: picture }] });
  },

  async list(ctx) {
    let message = "```\nFrank Jpegs:";
    let number = 0;
    for (let asset in assets) {
      message += `\n${number}. ${assets[asset]}`;
      number += 1;
    }
    message += "\n```";
    await ctx.reply(message);
  },

  async execute(ctx) {
    let subcommand = ctx.options.getSubcommand();
    if (subcommand === "num") {
      await this.num(ctx, ctx.options.getNumber("number"));
    } else if (subcommand === "name") {
      await this.name(ctx, ctx.options.getString("name"));
    } else if (subcommand === "list") {
      await this.list(ctx);
    }
  },
};
