# Vectors

A vector is a quantity with direction and magnitude. They can be represented geometrically or as a column matrix.

Vectors are used to define geometric shapes, and as a data structure, and as a function to map one value to another.

## Representing Vectors

- List of numbers
- Dictionary
- Function
- Arrow

### Dictionaries

Dictionary is an abstract data type storing values in the form of key-value pairs, and an unordered collection of associations between key and value.
In python they use `{}` - `{1: a, 2: b, 3: c}`

### Functions

A function maps a set of inputs to a set of outputs. Vectors can represent functions.

Consider `f(x) = x + 4`, if `S` is the set of inputs and `R` is the set of outputs, the mapping is `f: S -> R`
`f(x) = x + 4` as a vector is `[4, 5, 6, 7]`. In this vector, `0 -> 4`, `1 -> 5`, etc (based on the indices).

### Arrows

Vectors can also represent arrows. The size of the arrow is the magnitude, and the direction is the direction of the vector.
The length of the vector, `|A|` is calculated with Pythagoras's Theorem, direction is calculated with trigonometry.

## Vector Addition

Vectors can be added together and represented diagrammatically.
Vector addition is equivalent to translation.
The resultant vector C is drawn by joining the tail of A to the head of B

$$\begin{bmatrix} a\\ b \end{bmatrix} + \begin{bmatrix}  c \\ d \end{bmatrix} =
    \begin{bmatrix} a+b \\ c+d \end{bmatrix}
    \quad $$

## Vector Multiplication

Vectors can multiply by a scalar by multiplying each component of the vector by the scalar.

$$\begin{bmatrix} a\\ b \end{bmatrix} \cdot c =
    \begin{bmatrix} ac \\ bc \end{bmatrix}
    \quad $$

## Dot Product

Dot product, or scalar product multiplies 2 vectors to a single number

(A, B) . (C, D) = AC + BD

$$\begin{bmatrix} a\\ b \end{bmatrix} \cdot \begin{bmatrix}  c \\ d \end{bmatrix} = ac + bd
    \quad $$

## Angle between 2 Vectors

$$cos(\theta) = \frac{A \cdot B}{|A|\cdot|B|} $$

## Convex Combination

2 vectors also combine to form a third vector, which always lies at a right angle.

$(α \cdot u) + (β \cdot v) = αu + βv$ where $u$ and $v$ are each vectors, 
$α + β = 1, α, β \ge 0$

![Convex Combination](https://isaaccomputerscience.org/api/v2.18.2/api/images/content/computer_science/data_structures_and_algorithms/data_structures/figures/vector_convex_combinations_3.svg)

## Question Answers

1. $|A| = 2\sqrt{5} \\ |B| = \sqrt{10} \\ C = A + B = (5, 5) \therefore  |C| = 5\sqrt{2} $
2. $ A = (2, -1) \\ B = 2A = (4, -2) \\ A.B = (2\cdot4) + (-1\cdot-2) = 8 + 2 = 10 $
