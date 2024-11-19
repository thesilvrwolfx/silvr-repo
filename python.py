def dot_product(vector_a, vector_b):
    """
    Calculate the dot product of two vectors.
    
    Args:
        vector_a (list or tuple): First vector.
        vector_b (list or tuple): Second vector.
    
    Returns:
        float: The dot product of the two vectors.
        
    Raises:
        ValueError: If the vectors are not of the same length.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    
    # Calculate the dot product using list comprehension
    return sum(a * b for a, b in zip(vector_a, vector_b))


# Example usage:
if __name__ == "__main__":
    vec_a = [1, 2, 3]
    vec_b = [4, 5, 6]
    try:
        result = dot_product(vec_a, vec_b)
        print(f"Dot product of {vec_a} and {vec_b} is: {result}")
    except ValueError as e:
        print(e)
