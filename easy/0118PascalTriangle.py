class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Define a recursive helper function that builds Pascal's Triangle
        def gen(triangle, rows_left):
            # Base case: no more rows left to generate
            if rows_left == 0:
                return triangle
            else:
                # Retrieve the last row to calculate the next row
                prev_row = triangle[-1]

                # Create the next row:
                # Start and end with 1, each intermediate number is the sum of adjacent pairs from the previous row
                new_row = [1] + [
                    prev_row[i] + prev_row[i + 1] 
                    for i in range(len(prev_row) - 1)
                ] + [1]

                # Append the newly created row to the triangle
                triangle.append(new_row)

                # Recursively call gen with one fewer row left to generate
                return gen(triangle, rows_left - 1)

        # Handle edge case: if no rows are requested, return empty list
        if numRows == 0:
            return []

        # Start generating Pascal's Triangle with the initial row [[1]]
        return gen([[1]], numRows - 1)