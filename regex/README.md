
This program takes contact information that was copied and extracts the name, phone numbers and emails that can be pasted to a new document.


I based this program on Al Sweigart's book *Automate the Boring Stuff with Python*. I have modified some of the exercise to meet my own needs, but it is largely based on the examples presented in the book. I highly recommend [the book](https://www.amazon.com/) and the [Udemy course](https://www.udemy.com/).

There are probably more clever ways to create regex lines than the ones I have modified for my own purposes, however, I feel that it is best to do your own so you know what it states. I feel that a longer regex line that is readable is better than a clever regex line that is unmodifiable.

Make sure that there are no spaces in the last name
          if count(\s) in last name > 2:
            del \s
