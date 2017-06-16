# code-katas [![Build Status](https://travis-ci.org/clair3st/code-katas.svg?branch=master)](https://travis-ci.org/clair3st/code-katas) [![Coverage Status](https://coveralls.io/repos/github/clair3st/code-katas/badge.svg?branch=master)](https://coveralls.io/github/clair3st/code-katas?branch=master)
Collection of Python katas completed during Codefellows 401.


#### Sum of Pairs
Level5
- *Module:* (src/sum_pairs.py)

- *Tests:* (src/test_katas.py)

- *URL:* [Sum of Pairs](https://www.codewars.com/kata/sum-of-pairs/python)

- *Most interesting solution*
```Python
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
```


#### Multi-tap Keypad Text Entry on an Old Mobile Phone
Level 6 
- *Module:* phone_touch.py

- *Tests:* test_katas.py

- *URL:* [Phone Touch](https://www.codewars.com/kata/multi-tap-keypad-text-entry-on-an-old-mobile-phone/python)


#### Array.Diff
Level6
- *Module:* (src/array_diff.py)

- *Tests:* (src/test_array_diff.py)

- *URL:* [Array.Diff](https://www.codewars.com/kata/array-dot-diff/python)

- *Most interesting solution*
```Python
def array_diff(a, b):
    return [x for x in a if x not in set(b)]
```

#### Longest Palindrome
Level 6
- *Module:* longest_palindrome.py

- *Tests:* test_longest_palindrome.py

- *URL:* [Longest Palindrome](https://www.codewars.com/kata/longest-palindrome/python)

- *Most interesting solution*
```Python
def longest_palindrome(s):
    for c in xrange(len(s), -1, -1):
        for i in xrange(len(s) - c + 1):
            if s[i:i + c] == s[i:i + c][::-1]:
                return c
```

#### Regex Password Validator
Level 5
- *Module:* regex_password.py

- *Tests:* test_regex_password.py

- *URL:* [Regex Password Validator](https://www.codewars.com/kata/regex-password-validation/python)

- *Most interesting solution*
```Python
from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)
```

#### String Incrementer
- *Module:* string_incrementer.py

- *Tests:* test_string_incrementer.py

- *URL:* [String Incrementer](https://www.codewars.com/kata/string-incrementer/python)

- *Most interesting solution*
```Python
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
```

#### String Pyramid
- *Module:* string_pyramid.py

- *Tests:* test_string_pyramid.py

- *URL:* [String Pyramid](http://www.codewars.com/kata/string-pyramid/python)

- *Most interesting solution*
```Python
def watch_pyramid_from_the_side(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


def watch_pyramid_from_above(characters):
    if not characters : return characters
    baseLen = len(characters)*2-1
    return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


def count_visible_characters_of_the_pyramid(characters):
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )
```


#### Disemvowel Trolls
- *Module:* disemvowel.py

- *Tests:* test_disemvowel.py

- *URL:* [Disemvowel Trolls](https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python)


#### Flight Path
- *Module:* forbes.py

- *Tests:* test_forbes.py

- *URL:* [The Forbes top 40](https://codefellows.github.io/sea-python-401d5/assignments/kata_forbes_billionaires.html)


#### Flight Path
- *Module:* flight_path.py

- *Tests:* test_flight_path.py

- *URL:* [Flight Paths](https://codefellows.github.io/sea-python-401d5/assignments/kata_flight_paths.html)

#### Sort Deck of cards
- *Module:* sort_cards.py

- *Tests:* test_sort_cards.py

- *URL:* [Sort Cards](https://www.codewars.com/kata/sort-deck-of-cards/python)

- *Most interesting solution*
```Python
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)
```


#### Proper Parenthetics
- *Module:* proper_parenthetics.py

- *Tests:* test_parenthetics

- *Resources:* https://interactivepython.org/runestone/static/pythonds/BasicDS/SimpleBalancedParentheses.html


#### Sum Series
- *Module:* sum_series.py

- *Tests:* test_sum_series.py

- *URL:* [Sum Series](http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python)

- *Most interesting solution*
```Python
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
```

#### Even or Odd
- *Module:* evenorodd.py

- *Tests:* test_even-or-odd.py

- *URL:* [Even or Odd](https://www.codewars.com/kata/even-or-odd)

- *Most interesting solution*
```Python
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
```


#### Max and min in a list
- *Module:* max_min.py

- *Tests:* test_max_min.py

- *URL:* [Min and Max](https://www.codewars.com/kata/find-maximum-and-minimum-values-of-a-list)

- *Most interesting solution*
```Python
import math

def min(arr):
    return (sorted(arr))[0]

def max(arr):
    return (sorted(arr))[len(arr)-1]
```


#### Removing elements
- *Module:* removing_elements.py

- *Tests:* test_removing elements.py

- *URL:* [Removing elements](https://www.codewars.com/kata/removing-elements/python)

- *Most interesting solution*
```Python
def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
```


#### Removing elements
- *Module:* vowel_remover.py

- *Tests:* test_vowel_remover.py

- *URL:* [Removing vowels](https://www.codewars.com/kata/vowel-remover/train/python)

- *Most interesting solution*
```Python
def shortcut(s):
    return s.translate(None, 'aeiou')
```


#### Summation
- *Module:* summation.py

- *Tests:* test_summation.py

- *URL:* [Summation](https://www.codewars.com/kata/grasshopper-summation/train/python)

- *Most interesting solution*
```Python
def summation(num):
    return sum(xrange(num + 1))
```


#### Reverse array of an integer
- *Module:* reverse_array.py

- *Tests:* test_reverse_array.py

- *URL:* [Digitize](https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python)

- *Most interesting solution*
```Python
def digitize(n):
    return map(int, str(n)[::-1])
```


#### Powers of Two
- *Module:* powers_of_two.py

- *Tests:* test_powers_of_two.py

- *URL:* [Powers of two](https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python)

- *Most interesting solution*
```Python
def powers_of_two(n):
    return [1 << x for x in range(n + 1)]
```


#### Double Character in a String
- *Module:* double_char.py

- *Tests:* test_double_char.py

- *URL:* [Double Char](https://www.codewars.com/kata/double-char/train/python)

- *Most interesting solution*
```Python
def double_char(s):
    return ''.join(c * 2 for c in s)
```


#### Opposite Number
- *Module:* opposite_number.py

- *Tests:* test_opposite_number.py

- *URL:* [opposite](https://www.codewars.com/kata/opposite-number/train/python)

- *Most interesting solution*
```Python
def opposite(number):
    return -number
```


#### Debug Jenny's greeting
- *Module:* jenny_greet.py

- *Tests:* test_jenny_greet.py

- *URL:* [Jenny's greeting](https://www.codewars.com/kata/jennys-secret-message/train/python)

- *Most interesting solution*
```Python
def greet(name):
    return "Hello, {name}!".format(name = ('my love' if name == 'Johnny' else name));
```

#### Make negative
- *Module:* make_negative.py

- *Tests:* make_negative.py

- *URL:* [Make negative](https://www.codewars.com/kata/return-negative/train/python)

- *Most interesting solution*
```Python
def make_negative( number ):
    return -abs(number)
```

#### Needle in a Haystack
- *Module:* needle.py

- *Tests:* test_needle.py

- *URL:* [Needle in Haystack](https://www.codewars.com/kata/a-needle-in-the-haystack/train/python)

- *Most interesting solution*
```Python
def find_needle(haystack):
    found = 'found the needle at position '
    needle = 'needle'
    found += str(haystack.index(needle))
    return found
```

#### Count by X
- *Module:* count_by_x.py

- *Tests:* test_count_by_x.py

- *URL:* [Count by X](https://www.codewars.com/kata/count-by-x/train/python)

- *Most interesting solution*
```Python
def count_by(x, n):
    return range(x, x * n + 1, x)
```

#### String to list
- *Module:* string_to_list.py

- *Tests:* test_string_to_list.py

- *URL:* [String to List](https://www.codewars.com/kata/convert-a-string-to-an-array/train/python)

- *Most interesting solution*
```Python
def string_to_array(string=''):
    return string.split() if string else ['']
```

#### Remove first and Last Character
- *Module:* first_last.py

- *Tests:* test_first_last.py

- *URL:* [Reomve first and Last](https://www.codewars.com/kata/remove-first-and-last-character/train/python)

- *Most interesting solution*
```Python
remove_char=lambda s: s[1:-1]
```

#### Square and Sum
- *Module:* square_sum.py

- *Tests:* test_square_sum.py

- *URL:* [Square and Sum](https://www.codewars.com/kata/square-n-sum/train/python)

- *Most interesting solution*
```Python
def square_sum(numbers):
    return sum(x * 2 for x in numbers)
```
