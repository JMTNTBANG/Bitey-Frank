const { patreonToken } = require("../../config.json");
const { patreon } = require("patreon");
const { SlashCommandBuilder, EmbedBuilder } = require("discord.js");
const patreonClient = patreon(patreonToken);

module.exports = {
  data: new SlashCommandBuilder()
    .setName("patreon")
    .setDescription("See Patreon Based Things")
    .addSubcommand((subcommand) =>
      subcommand
        .setName("link")
        .setDescription("Get the link to my Patreon Page")
    )
    .addSubcommand((subcommand) =>
      subcommand
        .setName("members")
        .setDescription("Show the List of Patrons and their usernames")
    ),
  async link(ctx) {
    patreonClient("/current_user/campaigns").then(async ({ store }) => {
      const campaign = store
        .findAll("campaign")
        .map((campaign) => campaign.serialize());
      await ctx.reply({
        content: `Patreon:\n${campaign[0].data.attributes.url}`,
        ephemeral: true,
      });
    });
  },
  async members(ctx) {
    patreonClient("/current_user/campaigns").then(async ({ store }) => {
      const campaign = store
        .findAll("campaign")
        .map((campaign) => campaign.serialize());
      patreonClient(
        `/campaigns/${campaign[0].data.id}/pledges?include=patron.null`
      ).then(async ({ store }) => {
        const pledges = store
          .findAll("campaign")
          .map((pledges) => pledges.serialize());
        const embed = new EmbedBuilder()
          .setTitle("Patrons")
          .setDescription("List of Patrons");
        if (pledges.included) {
          pledges.included.forEach((pledge) => {
            var value = "No Discord";
            if (pledge.attributes.discord_id) {
              value = `<@${pledge.attributes.discord_id}`;
            }
            embed.addFields({
              name: pledge.attributes.full_name,
              value: value,
            });
          });
        }
        await ctx.reply({ embeds: [embed] });
      });
    });
  },
  async execute(ctx) {
    let subcommand = ctx.options.getSubcommand();
    if (subcommand === "link") {
      await this.link(ctx);
    } else if (subcommand === "members") {
      await this.members(ctx);
    }
  },
};
