const fs = require("fs");
const path = require("path");
const { createCanvas, registerFont } = require("canvas");
const { token, guildId, specialChannels } = require("./config.json");
const {
  Client,
  Collection,
  Events,
  GatewayIntentBits,
  ActivityType,
} = require("discord.js");

const frank = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildMessageReactions,
    GatewayIntentBits.MessageContent,
  ],
});

const frank_emojis = [
  "<:chonkfronk:1040418775129927752>",
  "<:frank3:1040422477433675857>",
  "<:sneakyfrank:1040419659792515213>",
  "<:hideyhole:1042217416278692003>",
  "<:jpeg:1042214971460829326>",
];

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}
function calcTime(offset) {
  var d = new Date();
  var utc = d.getTime() + d.getTimezoneOffset() * 60000;
  var nd = new Date(utc + 3600000 * offset);
  return nd;
}
function aussie_clock() {
  registerFont("./assets/fonts/fixedsys.ttf", { family: "FixedSys" });
  const width = 1920;
  const height = 1080;
  const picture = createCanvas(width, height);
  const edit = picture.getContext("2d");
  edit.fillStyle = "#000";
  edit.fillRect(0, 0, width, height);
  edit.font = '200pt "FixedSys"';
  edit.textAlign = "center";
  edit.textBaseline = "middle";
  const time = calcTime("+10.5");
  let hours = "";
  let minutes = "";
  if (time.getHours() > 9) {
    hours = time.getHours();
  } else {
    hours = `0${time.getHours()}`;
  }
  if (time.getMinutes() > 9) {
    minutes = time.getMinutes();
  } else {
    minutes = `0${time.getMinutes()}`;
  }
  const text = `${hours}:${minutes}`;
  edit.fillStyle = "#fff";
  edit.fillText(text, width / 2, height / 2);
  frank.guilds.cache
    .get(guildId)
    .setBanner(picture.toBuffer("image/png"), "Aussie Clock Update");
}
function birthdays() {
  var configFile = JSON.parse(fs.readFileSync("./src/config.json").toString());
  const todaysBirthdays = [];
  for (const birthday in configFile.birthdays) {
    const birthDate = new Date(configFile.birthdays[birthday].timestamp);
    const today = new Date(Date.now());
    if (
      birthDate.getMonth() == today.getMonth() &&
      birthDate.getDate() == today.getDate()
    ) {
      todaysBirthdays.push(birthday);
    }
  }
  const channel = frank.guilds
    .resolve(guildId)
    .channels.resolve(specialChannels["youtube_ping"]);
  todaysBirthdays.forEach((birthday) => {
    if (
      new Date(Date.now()).valueOf() -
        configFile.birthdays[birthday].last_announced >
      86400000
    )
      if (
        new Date(configFile.birthdays[birthday].timestamp).getFullYear() == 100
      ) {
        channel.send(`Merry Birthmas <@${birthday}>`);
      } else {
        const age =
          new Date(Date.now()).getFullYear() -
          new Date(configFile.birthdays[birthday].timestamp).getFullYear();
        channel.send(`Merry ${age}th Birthmas <@${birthday}>`);
      }
    configFile.birthdays[birthday].last_announced = new Date(
      Date.now()
    ).valueOf();
    fs.writeFileSync("./src/config.json", JSON.stringify(configFile, "", 2));
  });
}

const assets = fs
  .readdirSync("./assets/images/")
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
console.log("Commands Loaded!");

// Client Events
frank.on(Events.ClientReady, (ctx) => {
  console.log(`Logged in as ${ctx.user.tag}`);
  frank.user.setActivity({
    name: "FRANK.JS BETA",
  });
  const time1 = calcTime("+10.5");
  const time2 = calcTime("+10.5");
  time2.setSeconds(0);
  time2.setMinutes(time2.getMinutes() + 1);
  aussie_clock();
  setTimeout(function () {
    setInterval(aussie_clock, 60_000);
  }, time2.getTime() - time1.getTime());
  birthdays();
  setInterval(birthdays, 60_000);
  console.log("Ready!");
});

frank.on(Events.InteractionCreate, async (ctx) => {
  const command = ctx.client.commands.get(ctx.commandName);
  if (command == null) return;
  await command.execute(ctx);
});

frank.on(Events.MessageCreate, async (ctx) => {
  if (
    /f+r+a+n+k/i.test(ctx.content) ||
    ctx.content.includes(`<@${frank.user.id}>`)
  ) {
    if (ctx.author.bot == false) {
      var configFile = JSON.parse(fs.readFileSync("./config.json").toString());
      let isSnark = false;
      for (const snark of configFile.frankSnarks) {
        if (ctx.content.toLowerCase().includes(snark.trigger)) {
          isSnark = true;
          ctx.channel.sendTyping();
          await sleep((ctx.content.length * 1000) / 5);
          if (ctx == ctx.channel.lastMessage) {
            ctx.channel.send(snark.response);
          } else {
            ctx.reply(snark.response);
          }
        }
      }
      if (isSnark === false) {
        ctx.channel.send(
          frank_emojis[Math.floor(Math.random() * frank_emojis.length)]
        );
      }
    }
  }
});

frank.login(token);
