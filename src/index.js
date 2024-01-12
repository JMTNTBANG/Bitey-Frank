const fs = require("node:fs");
const path = require("node:path");
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

const assets = fs
  .readdirSync("../assets/")
  .filter((file) => file.endsWith(".png") || file.endsWith(".gif"));
module.exports = { assets };

// Command Loader
frank.commands = new Collection();

const foldersPath = path.join(__dirname, "commands");
const commandFolders = fs.readdirSync(foldersPath);

for (const folder of commandFolders) {
  const commandsPath = path.join(foldersPath, folder);
  const commandFiles = fs
    .readdirSync(commandsPath)
    .filter((file) => file.endsWith(".js"));
  for (const file of commandFiles) {
    const filePath = path.join(commandsPath, file);
    const command = require(filePath);
    if ("data" in command && "execute" in command) {
      frank.commands.set(command.data.name, command);
    } else {
      console.log(
        `[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`
      );
    }
  }
}

// Client Events
frank.on(Events.ClientReady, (ctx) => {
  console.log(`Logged in as ${ctx.user.tag}`);
});

frank.on(Events.InteractionCreate, async (ctx) => {
  const command = ctx.client.commands.get(ctx.commandName);

  if (!command) {
    console.error(`No command matching ${ctx.commandName} was found.`);
    return;
  }

  try {
    await command.execute(ctx);
  } catch (error) {
    console.error(error);
    if (ctx.replied || ctx.deferred) {
      await ctx.followUp({
        content: "There was an error while executing this command!",
        ephemeral: true,
      });
    } else {
      await ctx.reply({
        content: "There was an error while executing this command!",
        ephemeral: true,
      });
    }
  }
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

frank.login(token);
