### Automate the Boring Stuff with Python Exercises ###

I used an older edition of the book by [Al Sweigart](https://www.https://automatetheboringstuff.com/),
so I had to do some workarounds to complete some of the exercises. Below are a
few of the notes that I did not want to include as comments and clutter the
code.

This is meant as a notepad of sorts for me to come back as a reference.
I would encourage people interested in learning more to take Al's
[Udemy course](https://www.udemy.com/course/automate) and/or read the book.

**Email**

I had to use pyzmail36 as a fork used to install pyzmail.

I modified the exercise by adding in input statements because I didn't want to
put in the raw password in. I also followed the instruction in the email to
create a type of temporary application email which worked quite successfully.

**Regex**

This program takes contact information that was copied and extracts the name,
phone numbers and emails that can be pasted to a new document.

I based this program on Al Sweigart's book *Automate the Boring Stuff
with Python*. I have modified some of the exercises to meet my own needs, but
it is largely based on the examples presented in the book.

**Web Scraping**

In the exercise located under *soup.py* I was Getting a 503 error when using
the Amazon site. Through the Udemy FAQ forum it was suggested the use of
headers to make it seem as though the request was coming from a browser.
I was then having trouble with retrieving results. The instructor stated that
this was because of Amazon, which was true. So I used another suggestion for
a different site.

Also, under *soup.py*, the way to identify the browser you are using in order
to make it seem as though the program you are running is coming from a browser
is to use the following site: [What is My Browser](https://www.whatismybrowser.com/detect/what-is-my-user-agent)

For the *selenium_python.py* file, a copy of the file for
[chromedrive.exe](https://chromedriver.chromium.org/downloads) will
need to be downloaded to utilize the webdriver function for Chrome.

**Word**

Insert the path to document on the computer using *insert_path* assignment.

## The Final Project ##

I assigned myself a final project that combines all, or at least most of, the
methods used in this lesson. The project will need to:

  - Collect a count of emails that are unread and populate spreadsheet with those numbers
  - Assign a count of those emails
  - Order those emails by count from largest to smallest
  - Use that list to unsubscribe from those emails with higher counts
