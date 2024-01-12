const { token } = require("../config.json");
const { Client, Collection, Events, IntentsBitField } = require("discord.js");

const frank = new Client({
  intents: [
    IntentsBitField.Flags.Guilds,
    IntentsBitField.Flags.GuildMembers,
    IntentsBitField.Flags.GuildMessages,
    IntentsBitField.Flags.MessageContent,
  ],
});

const frank_emojis = [
  "<:chonkfronk:1040418775129927752>",
  "<:frank3:1040422477433675857>",
  "<:sneakyfrank:1040419659792515213>",
  "<:hideyhole:1042217416278692003>",
  "<:jpeg:1042214971460829326>",
];

frank.on(Events.ClientReady, (ctx) => {
  console.log(`Logged in as ${ctx.user.tag}`);
});

frank.on(Events.MessageCreate, (ctx) => {
  if (
    /f+r+a+n+k/i.test(ctx.content) ||
    ctx.content.includes(`<@${frank.user.id}>`)
  ) {
    if (ctx.author.bot == false) {
      ctx.channel.send(
        frank_emojis[Math.floor(Math.random() * frank_emojis.length)]
      );
    }
  }
});

frank.login(process.env.DEBUGTOKEN);
