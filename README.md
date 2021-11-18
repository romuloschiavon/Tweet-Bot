# Tweet-Bot
Bot created to delete my 1+ year old tweets. But you can set-up it to delete yours, with the chosen date.

## Set-Up

### Twitter Data-Archive
You'll need your **twitter data archive** that twitter provides for those who want to download it. The download will take you at least 12+ hours, so make sure to download it beforehand.

You can download it clicking **[here](https://twitter.com/settings/your_twitter_data)** and cliking download archive.

After you download it you'll need to set-up the file. Find your tweet.js file inside the data folder and open it.
![TweetJs image](https://user-images.githubusercontent.com/49570622/142493841-f47461fd-1e69-4cf6-8832-e6ada60b1378.png)

You should see something like this:
```  window.YTD.tweet.part0 = [ { ```
Change it to:
```{"data": [ { ```
And remember that in the end of the folder you'll need to add another **}**, it should look like this:
``` }]} ```

Save the file as tweets.json and put it in the root folder (where you cloned the repo)

### API Keys
This project requires **Twitter API Credentials**, if you have no existing app create one **[here](https://developer.twitter.com/en/portal/projects-and-apps)**, after creation go to details and assign more permissions to your aplication. The application requires **Read, Write and Direct Messages** level of permissions to do what it's intended.

After generating Consumer and Api Access Keys, change them in the apikeys.py folder.

### Imports
You'll probably need to install tweepy if you never used it. Remember to do: ```pip install tweepy```, and if you alreade have tweepy just update it: ```pip install tweepy --update```

### Choosing date
In the main.py folder you'll see that there's a variable called **endRange**, ```endRange = datetime.now(timezone.utc) - timedelta(days = 365)```.
The 365 indicates that you want to delete every tweet that is 1 year or older as of the day you're running the code. But you can change the 365 to any number you would like.

## Running
Now that everything is set-up, and you didn't mess up anything, you can run the code ```python main.py``` with any prompt you want, and it should work.
