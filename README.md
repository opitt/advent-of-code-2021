# advent-of-code-2021
My Python solutions for the advent of code 2021.
A nice challenge for everyday learning a coding language.
# Today I learned...
These are some things I learned along the way.

## Day 25
_General_
* I solved day 25 part 1 after Christmas. I got stuck with the other days ... and when I found out, that day 25 is a simulation ... I tried it. And it worked.

_Python_
* I started using lists to store the coordinates. But the search if a coordinate is in the list takes long. So I switched to dictionary. The performance is much better. There might be even better solutions with numpy and matrix operations ... but I am happy with the solution.

## Day 21
_General_
* Part 1 was easy and fun. But part 2 took a while. I found out about the grouping of 3 rolls ... but performance sucked.
* Found some inspiration in this repo: [marcodelmastro](https://github.com/marcodelmastro/AdventOfCode2021/blob/main/Day21.ipynb)

_Python_
* Learned **lru_cache** decorator from the **itertools** library. Great performance increase. It requires hashable parameters ... so my list did not work. Converting to a tuple made it immutable.


## Day 17
_General_
* A fun excercise. I like simulations.

_Python_
* I used a simple class to simulate the probe ... 
* Overkill but good to learn
```Python
class Probe:
    def __init__(self, velo_y, velo_x, min_y, max_y, min_x, max_x) -> None:

    def _update_velocity(self):

    def move_a_step(self):

    def is_in_target(self):

    def can_reach_target(self):
```

## Day 16
_General_
* Yesterday was tough. Today looks easier ... but I had problems with recursion. Stopped using recursion. 
* But now I am sitting with a list of operators, values and brackets. Could not solve part 2 yet ... but I know it's doable with a fresh brain.
* Part two is still running ... OMG.

_Python_
* I started to use pattern matching, **case-match**
* It's one thing to read about it .. but using it is bringing a lot of lightbulb moments.
  ```Python
  case d:
      match {"op": str, "id": int as id, "arguments": int } if id ==0:
          # sum found - having arguments
          pass
      match {"op": str, "id": int as id} if id ==0:
          # sum operator found with no argument specified
          pass
  ```
## Day 16
_General_
* This day took 4 days. Today I nearly cried by fixing the bugs, that kept me frustrated the last days.
* My approach: use a queue, put the current operator in, with the number of needed parameters ... -1 for "as many as the packet stream contains".
* For a given subpackets length, I used the function recursively.

_Python_
* Got to use the **queue** package and the **LifoQueue**. After four days, I can used it quite well know and understand it's basic struture. 

## Day 15
_General_
* This is going to be tough. My recursive solution broke very quickly. Now I try with Dijkstra ...
* Watch here: [youtube](https://www.youtube.com/watch?v=pVfj6mxhdMw&list=PLdWlRrByQZJ00x7n4v51Mtc-rU-UAicGB&index=3)
* Part two is still running ... OMG. It run all night ... and finally produced the right number.

_Python_
* Nothing really new. Maybe to mention that I use tupels as index for a dictionary ... boring, right?

## Day 14 
_General_
* This looked so easy for part 1. And then it timed out for part 2. Damn.
* Got inspired by an idea and it worked with test data. BUT NOT with input data ... Damn.
* Until I found my bug ... I was ignoring duplicate template input pairs ... 

_Python_
* I used today the first time **itertools.pairwise**. Nice to have so many batteries included.

## Day 13 
_General_
* Success. I worked today with the points - and not with a matrix. Proud of myself. This is faster than a matrix operation.
* A stupid bug made me think, one can't return a list ... until I found out, the returned list was correct, but my calculation was wrong.

_Python_
* Used **dictionary with lambda function** to keep the code flexible. 
* For x and y folding I can apply the same logic ... thanks to lambda dictionionary.

## Day 12 - Saturday 
_General_
* Success. Recursion was the theme for me. Still not so happy with performance ... too much copying and validating wrong paths.
* Ok, I looked into performance. The difference is: I count and store the number of visits per node. AND I store the small cave, that was visited twice. From 4 sec to 0.8 sec. Happy.

_Python_
* Used **Counter**, **deepcopy**, and recursion.
* I also used **timit** again, to measure execution time.

## Day 11 - Saturday 
_General_
* Success. I like simulations - as long as they are in 2 dimensions. I guess, one could use numpy or pandas for this simulations to make matrix handling easier. Need to recall how that worked ...

## Day 10 ## 
_General_
* Success. I remembered a similar challenge finding matching pairs. With a simple replacing algorithm the solution appeared pretty fast (for my personal stats).

_Python_
* Used **filter** to filter only negative or positive values from a list

## Day 9 ## 
_General_
* Today feels better. Managed to solve both parts in reasonable time. The challenge was to debug the recursive algorithm and trace the changes in the big map. The instructions were not really clear ... which caused some delays.

_Python_
* Used **math.prod**

## Day 8 ##
_General_
* After a brain heavy day, part 2 was too hard. Will need some rest to enjoy the next days of AoC

## Day 7 ##
_General_
* What a great start of the day. Not too difficult. Within 60 min I had both solutions.

_About Python_
* learned to use **timeit** to measure performance of my code

_General_
* also learned to use **time** on the command line 
```time python3 day7.py```

## Day 6
_General_
* 5.58 I was sitting at the screen. Family support made it possible to do AoC instead care taking. Big thanks! However ... I got trapped in mathematical thinking instead of logical ... and I am honestly not a math fan. The logic finally won.

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

## Day 4 - Saturday
_General_
* First frustration. My understanding of the bingo logic prevented a fast solution. My assumption was, that if one should return the last bingo card - a round should not have more than one bingo at once. Assume, there are 3 bingos at once - which would be the last??? ... I swallowed the bitter pill ... and fixed the code.

_About Python_
* Used **flatten** from the newly found library: **more_itertools** to merge a list of lists into one list. Nice.

## Day 3
_General_
* Can't remember ... what happened yesterday? :) 

## Day 2
_General_
* The early bird is catching the worm. (German proverb)

_About Python_
* I used the new **match case** construct for the first time. In it's simplest way, but it's more readable without many **if** statements.

## Day 1
_General_
* One need to wake up early to rank well on the leaderboard. Ok, that's old news.

_About Python_
* I changed the solution and use **windowed** from **[more_itertools](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.windowed)**. Amazing, that there is a library for "every" challenge ... 
