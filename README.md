![Bot Logo](images/logo.jpg)

# GeometryDashBot
A Telegram Bot that lets you see many GD stats, levels, info and more!  

## Telegram Bot
[Use it on Telegram!](https://t.me/geometrydashbot)  

## Special Thanks
A big shoutout to [Colon](https://www.youtube.com/channel/UCFDsxSlQXpLLpVScy2NmbcQ) for inspiring me to make this bot and for providing the awesome APIs from his [GD Browser website](https://gdbrowser.com)! They're SO much better than RobTop's...

## Crypting File
'modules/crypter.py', required by bot.py, is missing in the repo: that's because  
1. I don't want, for security reasons, to give the encryption key for my database, as it contains personal data of many users  
2. You can make your own information encryption method, by putting it in 'modules/crypter.py'. It must contain a "crypt" and a "decrypt" function, that will respectively encode and decode the password stored in the database.
