const fs = require("fs");
const { SlashCommandBuilder, EmbedBuilder, Embed } = require("discord.js");

module.exports = {
  data: new SlashCommandBuilder()
    .setName("birthday")
    .setDescription("Get Birthday Celebrations from Frank")
    .addSubcommand((subcommand) =>
      subcommand
        .setName("set")
        .setDescription("Get birthday celebrations from Frank")
        .addNumberOption((option) =>
          option.setName("mm").setRequired(true).setDescription("Birthmonth")
        )
        .addNumberOption((option) =>
          option.setName("dd").setRequired(true).setDescription("Birthday")
        )
        .addNumberOption((option) =>
          option
            .setName("yyyy")
            .setRequired(false)
            .setDescription("Birthyear (Optional)")
        )
    )
    .addSubcommand((subcommand) =>
      subcommand
        .setName("remove")
        .setDescription("No Longer Get Birthday Celebrations from Frank")
    )
    .addSubcommand((subcommand) =>
      subcommand.setName("list").setDescription("List Saved Birthdays")
    ),
  async set(ctx, mm, dd, yyyy) {
    if (yyyy == null) {
      yyyy = 100;
    }
    var configFile = JSON.parse(fs.readFileSync("./src/config.json").toString());
    const birthday = new Date(yyyy, mm - 1, dd);
    configFile.birthdays[ctx.user.id] = {
      timestamp: birthday.valueOf(),
      last_announced: 0,
    };
    fs.writeFileSync("./src/config.json", JSON.stringify(configFile, "", 2));
    if (yyyy == 100) {
      await ctx.reply({
        content: `Frank will now Celebrate you on \`${mm}/${dd}\``,
        ephemeral: true,
      });
    } else {
      await ctx.reply({
        content: `Frank will now Celebrate you being born in \`${yyyy}\` on \`${mm}/${dd}\``,
        ephemeral: true,
      });
    }
  },
  async remove(ctx) {
    var configFile = JSON.parse(fs.readFileSync("./src/config.json").toString());
    delete configFile.birthdays[ctx.user.id];
    fs.writeFileSync("./src/config.json", JSON.stringify(configFile, "", 2));
    await ctx.reply({
      content: "Frank will no longer Celebrate you",
      ephemeral: true,
    });
  },
  async list(ctx) {
    var configFile = JSON.parse(fs.readFileSync("./src/config.json").toString());
    const embed = new EmbedBuilder().setTitle("Birthdays");
    for (const birthday in configFile.birthdays) {
      const bday = new Date(configFile.birthdays[birthday].timestamp);
      let user = await ctx.client.users.fetch(birthday);
      if (bday.getFullYear() == 100) {
        embed.addFields({
          name: user.nickname,
          value: `${bday.getMonth() + 1}/${bday.getDate()}`,
          inline: true,
        });
      } else {
        embed.addFields({
          name: user.nickname,
          value: `${
            bday.getMonth() + 1
          }/${bday.getDate()}/${bday.getFullYear()}`,
          inline: true,
        });
      }
    }
    ctx.reply({ embeds: [embed] });
  },
  async execute(ctx) {
    let subcommand = ctx.options.getSubcommand();
    if (subcommand === "set") {
      await this.set(
        ctx,
        ctx.options.getNumber("mm"),
        ctx.options.getNumber("dd"),
        ctx.options.getNumber("yyyy")
      );
    } else if (subcommand === "remove") {
      await this.remove(ctx);
    } else if (subcommand === "list") {
      await this.list(ctx);
    }
  },
};
