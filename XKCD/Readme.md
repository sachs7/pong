# Automate the boring stuff!

  Isn't it a manual task to visit a website every day to view your favorite comic strip? Why not let a script do it for you every day? And may be send it as an email attachment at a specified time everyday of the week! Well, with the help of Python book, **'Automate the Boring Stuff'** let's create our small script to download and send that as an email attachment.

## Details

  I have created `download_xkcd.py` which scrapes https://xkcd.com for a comic and downloads it in a local folder. The `email_xkcd.py` contains code to send the downloaded comic as an email attachment. But you don't want to receive a duplicate comic if there is no new comic's, right!? So, for this I keep a record of previous comic in a text file called `comic_records.txt` which I will read before sending out an email.

### Cron Job

  I followed <a href='https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html'>Ole Michelsen's </a> article to create a _Cron Job_, which is straight forward in MacOS.
  
  To run your python script everyday of the week at 6 PM, you can do something like this:

  ```
  0 18 * * * cd /folder/where/your/script/resides/ && python <name of your script>
  ```


_Note:_ If you are using Gmail to send email then you will need to allow **less secure** apps to access gmail! The first time you try to access gmail using Python, your access will not be granted and you will receive an email from Google saying, **Review blocked sign-in attempt**, click _allowing access to less secure apps_ link and select **Turn on** option and there you go, you can access your gmail using Python!


