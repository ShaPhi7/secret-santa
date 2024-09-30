# secret-santa

Imagine an extended family pulling names out of a hat for [Secret Santa](https://en.wikipedia.org/wiki/Secret_Santa). They aren't going to want to draw their own name. They also aren't going to want to draw the name of their siblings, as they will already be buying a present for them anyway. If someone draws a valid name, they will have to put that name back in and draw a new name, but if they are the last person, there's no other names for them to draw, and the whole draw will need to be redone.

With what probability will they succeed in having a valid draw? It was this problem that a friend messaged me with a couple of Christmases ago. Some of the probabilities involved can be calculated, but a full mathematical proof of the more complex forms of the problem gets quite tricky, quickly.

So rather than looking for clever code or efficient solutions here, the purpose of this project is to provide a simple combinatorial fact-check of the answers to the questions above.

# Test Suite

Run the test suite from the command line using `python -m unittest tests/test_secret_santa.py`
