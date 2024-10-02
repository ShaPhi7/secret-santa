# secret-santa-combinatorics

Imagine an extended family pulling names out of a hat for [Secret Santa](https://en.wikipedia.org/wiki/Secret_Santa). They aren't going to want to draw their own name. They also aren't going to want to draw the name of their siblings, as they will already be buying a present for them anyway. If someone draws a valid name, they will have to put that name back in and draw a new name, but if they are the last person, there's no other names for them to draw, and the whole draw will need to be redone.

With what probability will they succeed in having a valid draw? It was this problem that a friend messaged me with a couple of Christmases ago. Some of the probabilities involved can be calculated, but a full mathematical proof of the more complex forms of the problem gets quite tricky, quickly.

So rather than looking for clever code or efficient solutions here, the purpose of this project is to provide a simple combinatorial fact-check of the answers to the questions above.

# Command Line

Run the program from the command line using `python secret_santa.py --people A1 A2 B1`.

Run `python secret_santa.py --help` for more details on the arguments that can be passed in:

Given a list of players, the program will compute the total number of valid permutations given the ruleset required.
```
options:
  -h, --help            show this help message and exit
  -p PEOPLE [PEOPLE ...], -P PEOPLE [PEOPLE ...], --people PEOPLE [PEOPLE ...]
                        Each person hould be of the from A#, where the first letter indicates the family they belong to. (e.g., A1 A2 B1 C1).
  -O, --allow-draw-own-name
                        Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).
  -F, --allow-draw-family-member
                        Permutations where someone has drawn their own name will be allowed (normally, they are disallowed).
  -2, --second-draw     Permutations shown for a second draw with the extra rule that nobody can have the same name they drew in the first draw (the results of which are not known, other than the fact that
                        they were valid).
  -V, --verbose         Prints out the permutations, in addition to the counts.
```
# Test Suite

Run the test suite from the command line using `python -m unittest tests/test_secret_santa.py`

# The Mathematics

### Derangements

When we apply only the rule that no peerson may draw their own name, what we're modeling is actually a **derangement**.

A derangement is a permutation of a set where no element appears in its original position. 

#### Example:
Consider the set \( \{1, 2, 3\} \). The **total permutations** of this set are:

```math
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

Of these, the **derangements** are the permutations where no element is in its original position:

```math
[(2, 3, 1), (3, 1, 2)]
```

So, there are **2 derangements** out of the **6 total permutations**.

Running our script several times with different values allows the keen eye to spot that the formula for derangements can be calculated as

```math
D(n) = n! \left( \frac{1}{0!} - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!} \right)
```
where $n$ is the number of items in a set (or people in a Secret Santa group). Derangements can be modelled as approximately

```math
D(n) \approx \frac{n!}{e}
```
When $n$ is large, the chance of a permutation being a derangement is **36.79%**, or 
```math
\frac{1}{e}
```
# Open Questions

- How does introducing families impact the results, where a family is two or more people who **can not** draw each other (and multiple families are possible)? Is there a formula to predict this? We have added this into the script, but have not been able to derive a formula - I suspect the way to approach this is through working out the reverse result (assume family members **must** draw each other).

- In a real Secret Santa, we may want to avoid people drawing the same name as in the previous year. How does this affect the results in the second year? This is now added to the program, but is there a formula we can derive to calculate it?

- In a real Secret Santa, if a person draws an invalid name, they might just put that name back in and draw another. How does this impact the results?
