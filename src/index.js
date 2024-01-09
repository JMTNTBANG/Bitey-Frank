require("dotenv").config();
const { Client, IntentsBitField } = require("discord.js");

const frank = new Client({
  intents: [
    IntentsBitField.Flags.Guilds,
    IntentsBitField.Flags.GuildMembers,
    IntentsBitField.Flags.GuildMessages,
    IntentsBitField.Flags.MessageContent,
  ],
});

frank.on("ready", (ctx) => {
  console.log("Logged in as " + ctx.user.displayName);
});

frank.login(process.env.DEBUGTOKEN);
