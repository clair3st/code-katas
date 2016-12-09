# code-katas
Collection of Python katas completed during Codefellows 401.

### Even or Odd
**Module:** evenorodd.py

**Tests:** test_even-or-odd.py

**URL:** [Even or Odd](https://www.cyodewars.com/kata/53da3dbb4a5168369a0000fe/train/python)

**Most interesting solution**
```
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
```


### Max and min in a list
**Module:** max_min.py

**Tests:** test_max_min.py

**URL:** [Min and Max](https://www.codewars.com/kata/find-maximum-and-minimum-values-of-a-list)
**Most interesting solution**
```
import math

def min(arr):
    return (sorted(arr))[0]

def max(arr):
    return (sorted(arr))[len(arr)-1]
```


### Removing elements
**Module:** removing_elements.py

**Tests:** test_removing elements.py

**URL:** [Removing elements](https://www.codewars.com/kata/removing-elements/python)

**Most interesting solution**
```
def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
```


### Removing elements
**Module:** vowel_remover.py

**Tests:** test_vowel_remover.py

**URL:** [Removing vowels](https://www.codewars.com/kata/vowel-remover/train/python)

**Most interesting solution**
```
def shortcut(s):
    return s.translate(None, 'aeiou')
```


### Summation
**Module:** summation.py

**Tests:** test_summation.py

**URL:** [Summation](https://www.codewars.com/kata/grasshopper-summation/train/python)

**Most interesting solution**
```
def summation(num):
    return sum(xrange(num + 1))
```


### Reverse array of an integer
**Module:** reverse_array.py

**Tests:** test_reverse_array.py

**URL:** [Digitize](https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python)

**Most interesting solution**
```
def digitize(n):
    return map(int, str(n)[::-1])
```


### Powers of Two
**Module:** powers_of_two.py

**Tests:** test_powers_of_two.py

**URL:** [Powers of two](https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python)

**Most interesting solution**
```
def powers_of_two(n):
    return [1 << x for x in range(n + 1)]
```


### Double Character in a String
**Module:** double_char.py

**Tests:** test_double_char.py

**URL:** [Double Char](https://www.codewars.com/kata/double-char/train/python)

**Most interesting solution**
```
def double_char(s):
    return ''.join(c * 2 for c in s)
```


### Opposite Number
**Module:** opposite_number.py

**Tests:** test_opposite_number.py

**URL:** [opposite](https://www.codewars.com/kata/opposite-number/train/python)

**Most interesting solution**
```
def opposite(number):
    return -number
```
