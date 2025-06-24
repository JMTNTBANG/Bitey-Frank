const { SlashCommandBuilder } = require("discord.js");
const GEMINI_API_KEY = require("../../config.json").geminiToken;

module.exports = {
  data: new SlashCommandBuilder()
    .setName("askfrankgpt")
    .setDescription("Ask Frank a question (Powered by Gemini)")
    .addStringOption((option) =>
      option
        .setName("query")
        .setDescription("What do you want to ask?")
        .setRequired(true)
    ),
  async execute(ctx) {
    ctx.reply({ content: "Frank is thinking...", flags: "Ephemeral" });
    ctx.channel.createWebhook({ name: "frankhook" }).then((webhook) => {
      webhook
        .send({
          content: ctx.options.getString("query"),
          username: ctx.user.displayName,
          avatarURL: ctx.user.avatarURL(),
        })
        .then((webhookMsg) => {
          webhook.delete();
          ctx.channel.sendTyping();
          fetch(
            `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}`,
            {
              headers: {
                "Content-Type": "application/json",
              },
              method: "POST",
              body: `{"system_instruction": {"parts": [{"text": "You are a snake named Frank who isn't very bright and has a snarky personality"}]},"contents": [{"parts": [{"text": "${ctx.options.getString("query")}"}]}]}`,
            }
          )
            .then((response) => response.json())
            .then((data) => {
              ctx.channel.send(data.candidates[0].content.parts[0].text);
            });
        });
    });
  },
};
