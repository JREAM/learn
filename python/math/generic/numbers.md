# Numbers
These are basic solutions to handling numbers.

### Fractions in Programming
This is very easy:

- .1: Tenths or 1/10
- .02: Hundredths or 2/100
- .003: Thousandths or 3/1000
- 1: One or 1/1


### Positive Int/Float To Negative

    a = 50.5
    print a * -1

### Negative Int/Float To Positive

    a = -20.23
    print abs(a) # Or an absolute value equivalent

### Using a Percentage Scale
Using a database as an example. In a column, It's nice to use a `Decimal(3,2)` rather than a `INT(3)`. Note that
MySQL uses decimal as: `Decimal(MaxDigits, AfterDecimal)`.

    percent_complete
    ----------------
    decimal(3,2): 0.00 to 1.00

This makes pulling the data in easier to use in an operation, if I retrieve a record that is `0.39`, I
can get the real percent by:

    0.39 * 10 = 39

I can also use it for other operations, such as a discount:

    full_price = 29.99
    percent_off = 0.25
    discounted_price = full_price - (full_price * percent_off)


### Computational Numbers
To count in these numbers, you count until it reaches its `Base - 1`, then you
move along, it's somewhat similar to Roman Numerals.

          Decimal | Binary | Octal | Hexidecimal
         ---------------------------------------
    Base  10      | 2      | 8     | 16
         ---------------------------------------
          0       | 0      | 0     | 0
          1       | 1      | 1     | 1
          2       | 10     | 2     | 2
          3       | 11     | 3     | 3
          4       | 100    | 4     | 4
          5       | 101    | 5     | 5
          6       | 110    | 6     | 6
          7       | 111    | 7     | 7
          8       | 1000   | 10    | 8
          9       | 1001   | 11    | 9
          10      | 1010   | 12    | A (.. B C D E F 10)

### Roman Numerals
These get weird after 18, but for reference sake here we are:

- 1: I
- 2: II
- 3: III
- 4: IV
- 5: V
- 6: VI
- 7: VII
- 8: VIII
- 9: IX
- 10: X
- 11: XI
- 12: XII
- 13: XIII
- 14: XIV
- 15: XV
- 16: XVI
- 17: XVII
- 18: XVIII
- 19: XIX
- 20: XX
- 30: XXX
- 40: XL
- 50: L
- 60: LX
- 70: LXX
- 80: LXXX
- 90: XC
- 99: XCIX