# advent-of-code-2021
My Python solutions for the advent of code 2021.
A nice challenge for everyday learning a coding language.
# Today I learned...
These are some things I learned along the way.
## Day 1
_General_
* One need to wake up early to rank well on the leaderboard. Ok, that's old news.

_About Python_
* I changed the solution and use **windowed** from **[more_itertools](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed)**. Amazing, that there is a library for "every" challenge ... 

## Day 2
_General_
* The early bird is catching the worm. (German proverb)

_About Python_
* I used the new **match case** construct for the first time. In it's simplest way, but it's more readable without many **if** statements.

## Day 3
_General_
* Can't remember ... what happened yesterday? :) 

## Day 4 - Saturday
_General_
* First frustration. My understanding of the bingo logic prevented a fast solution. My assumption was, that if one should return the last bingo card - a round should not have more than one bingo at once. Assume, there are 3 bingos at once - which would be the last??? ... I swallowed the bitter pill ... and fixed the code.

_About Python_
* Used **flatten** from the newly found library: **more_itertools** to merge a list of lists into one list. Nice.

## Day 5 - Sunday
_General_
* Waking up 5.45 on a Sunday to get fun stuff done. Expecting big challenge ... and was happily surprised, that the challenge today was quite streight forward

_About Python_
* I was suprised to not find a simple **sign** function (there are some in **numpy** and in **math** (copysign). But reading about it would not have helped me. **sign(0)** would result in 0 ... and I wanted a 1. So it became a lambda: 
```python
sign=lambda n: 1 if n>=0 else -1
```
_Others_
* Learned to format code blocks with markdown ... ```python does the trick above
