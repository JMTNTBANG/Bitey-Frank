const fs = require("fs")
const { Events } = require("discord.js");

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

const frank_emojis = [
  "<:chonkfronk:1040418775129927752>",
  "<:frank3:1040422477433675857>",
  "<:sneakyfrank:1040419659792515213>",
  "<:hideyhole:1042217416278692003>",
  "<:jpeg:1042214971460829326>",
];

module.exports = {
  name: Events.MessageCreate,
  async execute(ctx) {
    if (
      /f+r+a+n+k/i.test(ctx.content) ||
      ctx.content.includes(`<@${ctx.client.user.id}>`)
    ) {
      if (ctx.author.bot == false) {
        var configFile = JSON.parse(
          fs.readFileSync("./src/config.json").toString()
        );
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
  },
};
