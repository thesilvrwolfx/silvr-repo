# **Vector Dot Product Implementation**

## **Introduction**  
The _dot product_ is a fundamental operation in linear algebra that takes two vectors and returns a scalar value. This operation is widely used in fields such as computer graphics, machine learning, and physics.

---

## **Mathematical Expression**  
The dot product of two vectors $'\( \mathbf{A} \)'$ and \( \mathbf{B} \), each of size \( n \), is calculated as:

\[
\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} A_i B_i = A_1 B_1 + A_2 B_2 + \cdots + A_n B_n
\]

---

## **Code Example**  

Below is a snippet of the implementation in Python:  

```python
def dot_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Example usage
vec_a = [1, 2, 3]
vec_b = [4, 5, 6]
result = dot_product(vec_a, vec_b)
print("Dot product:", result)
