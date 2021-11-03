# Regex Maths

Regexes can be used to evaluate numeric sets

`N = {0, 1, 2, 3, 4}`
`Z = {-2, -1, 0, 1, 2}`

## Set Comprehension

$\{ x \mid x \in \mathbb{N} \land \ge 1\} $

This set holds all values of x where x is a natural number and x >= 1

### Types of Sets

- Finite sets have a fixed number of elements with a $ |S| \in \mathbb{N} $
- Infinite sets have an infinite amount of elements, for example $\mathbb{N} $
- Countably Infinite sets are infinite, but countable

**Cardinality** = the size of a set, $ |S| $

### Cartesian Product

The product of joining 2 sets together.
$$ 
     X = \{1, 2, \3}
     Y = \{a, b, c\}

     cartProd = \{(1, a), (1, b) (1, c), (2, a), (2, b), (2, c), (3, a), (3, b), (3, c)\}
$$

### Subset

If all the elements of set A  are present in set B, $a \subset b$
A proper subset has fewer elements than the main subset, i.e $a \neq b$
A countable set has the same number of elements as a subset of natural numbers

### Union

This joins two sets together to form a new set containing both

### Intersection

Joining two sets together keeping only the elements contained in both

### Difference

Joining sets together, keeping only the unique ones
