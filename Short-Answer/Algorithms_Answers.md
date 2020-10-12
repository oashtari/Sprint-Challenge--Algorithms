#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```
a)  a = 0                       # O(1)
    while (a < n * n * n):      # O(n)
      a = a + n * n             # O(n)
```
a) There is one loop (the a < n), run up to n times, giving us an O(n).


```
b)  sum = 0                     # O(1)
    for i in range(n):          # O(n)
      j = 1                     # O(1)
      while j < n:              # O(n)
        j *= 2                  # O(1)
        sum += 1                # O(1)
```
b) There are two for loops that are run n times, one is nested inside the other, so the 'n's are multiplied, giving is an O(n**2)


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:                  # O(1)
        return 0                        # O(1)

      return 2 + bunnyEars(bunnies-1)   # O(n)
```
c) There is a recursive call here on bunnies, counting down from n to 0, so the recursion is run n times, giving us an O(n).


## Exercise II

n stories

-1 egg if off floor f and higher

egg = egg if lower than floor f 

The ideal solution would be to use a binary search, dropping an egg from the middle floor, and halving the choices until you find floor f-1 where the egg does not break, this is a O(log n) operation. 
You could of course run a simple for loop counting up from 1, but if f is really high, you would break a lot of eggs.
