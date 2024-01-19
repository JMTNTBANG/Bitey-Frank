const fs = require("fs");
const path = require("path");
const { assets } = require("../../index.js");
const { SlashCommandBuilder } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("beajpeg")
    .setDescription("Send a Random Image of Frank"),
  async execute(ctx) {
    let picture = path.join(
      __dirname,
      "../../../assets",
      assets[Math.floor(Math.random() * assets.length)]
    );
    await ctx.reply({ files: [{ attachment: picture }] });
  },
};
