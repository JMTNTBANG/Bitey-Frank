const fs = require("fs");
const { Events } = require("discord.js");
const { guildId, specialChannels, patreonToken, defaultStatus } = require("../config.json");
const { createCanvas, registerFont } = require("canvas");
const { patreon } = require("patreon");
const { defaultMaxListeners } = require("events");
const patreonClient = patreon(patreonToken);

function aussie_clock(ctx) {
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
  const time = new Date();
  const timeText = time.toLocaleTimeString(
    "en-AU",
    {
      hour: "2-digit",
      minute: "2-digit",
      timeZone: "Australia/Adelaide",
      hourCycle: "h23"
    }
  );
  edit.fillStyle = "#fff";
  edit.fillText(timeText, width / 2, height / 2);
  ctx.guilds.cache
    .get(guildId)
    .setBanner(picture.toBuffer("image/png"), "Aussie Clock Update");
}

function birthdays(ctx) {
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
  const channel = ctx.guilds
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

function patronsInStatus(ctx) {
  setInterval(function () {
  const statuses = [defaultStatus];
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
      if (pledges.included) {
        pledges.included.forEach((pledge) => {
          statuses.push(`Thanks ${pledge.attributes.full_name}!`);
        });
      }
    });
  });
    statuses.forEach((status) => {
      setTimeout(function () {
        ctx.user.setActivity({
          name: status,
        });
      }, 10_000);
    });
  }, 10_000);
}

module.exports = {
  name: Events.ClientReady,
  async execute(ctx) {
    console.log(`Logged in as ${ctx.user.tag}`);
    const time1 = calcTime("+10.5");
    const time2 = calcTime("+10.5");
    time2.setSeconds(0);
    time2.setMinutes(time2.getMinutes() + 1);
    aussie_clock(ctx);
    setTimeout(function () {
      setInterval(function () {
        aussie_clock(ctx);
      }, 60_000);
    }, time2.getTime() - time1.getTime());
    birthdays(ctx);
    setInterval(function () {
      birthdays(ctx);
    }, 60_000);
    patronsInStatus(ctx);
    console.log("Ready!");
  },
};
