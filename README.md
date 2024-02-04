# tsao pipeline summary
## set up
```sh
pip install requests
```

## running it
```
python main.py [DISCORD WEBHOOKS URL]
```

example
```
python main.py discord.com/...
```

## cron job
This tool is designed to be fired every 24 hours, at 8 AM Singapore time.

> [!Warning]
> As the GitHub API calls are done without a token, it is subject to a limit of 60 requests per hour.
>
> This will not be an issue for the GitHub Action, however, it might be an issue if you are doing local development.
>
> In that case, add an authorization token to increase the limit to 5000 per second.

## maintainers
- [Yee Jia Chen](https://github.com/jiachenyee) S10219344C
- [Isabelle Pak Yi Shan](https://github.com/isabellepakyishan) S10222456J
- [Ho Kuan Zher](https://github.com/Kuan-Zher) S10223870D
- [Cheah Seng Jun](https://github.com/DanielCheahSJ) S10227333K
- [Chua Guo Jun](https://github.com/GuojunLoser) S10227743H
