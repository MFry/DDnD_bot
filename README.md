# DDnD_bot
Discord DnD Bot

##### Dependencies
Python 3.6

# Run
[HowTo: Required a token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

##### HowTo: Register on a discord server
1. Create a new app
2. Add `token` file to top level DDnD directory with the generated token pasted within.
2. Register as bot
3. Create permissions int
3. Add to the following url and navigate to it within the browser. url: https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}

# Install
```bash
pip install -r requirements.txt
```

# Test

```bash
python -m pytest
```
