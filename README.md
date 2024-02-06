# Bitey Frank

The official mascot of the unofficial Discord server of the Garbage Stream.

## Prerequisites

Have the following installed on your system:

1. **[node.js](https://nodejs.org/en/download)**
2. An IDE of your own choice (**[VS-Code](https://code.visualstudio.com/)** is recommended)
3. A version of ffmpeg in your top directory (Folder must be named `ffmpeg` and only linux version is supported at the moment)

## Configuration

In order to make the bot function, you will need a discord bot token (If you do not have a discord bot make one **[Here](https://discord.com/developers/applications)**)

Next create a `config.json` file to the top of the directory, then paste the following inside the file:
```json
{
  "guildId": "Main Guild ID",
  "clientId": "Client ID (Found in Dev Portal)",
  "token": "Discord Bot Token",
  "specialChannels": {
    "youtube_ping": "YouTube Ping Channel ID"
  },
  "frankSnarks": [],
  "birthdays": {}
}
```

## Development

If you would like to create your own server for testing, this template of the Garbage Stream Server is available **[Here](https://discord.new/wBSWQw9dgMfV)**

## FAQs

(Any questions asked either on github or on the Garbage Stream discord about the bot will be added here for future reference)


