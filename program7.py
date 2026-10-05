# Input matrix from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row-wise:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Remove negative values
filtered_matrix = list(
    map(lambda row: list(filter(lambda x: x >= 0, row)), matrix)
)

# Sort each row
sorted_matrix = list(map(lambda row: sorted(row), matrix))

# Square each element
squared_matrix = list(
    map(lambda row: list(map(lambda x: x * x, row)), matrix)
)

# Input tuple data
n = int(input("Enter number of tuples: "))
tuples_data = []

for i in range(n):
    a, b = map(int, input(f"Enter tuple {i+1} (two numbers): ").split())
    tuples_data.append((a, b))

# Sort tuples by second element
sorted_tuples = sorted(tuples_data, key=lambda x: x[1])

# Display results
print("\nOriginal Matrix:", matrix)
print("Matrix after removing negative values:", filtered_matrix)
print("Sorted Matrix:", sorted_matrix)
print("Matrix after squaring elements:", squared_matrix)
print("Original Tuples:", tuples_data)
print("Tuples sorted by second element:", sorted_tuples)