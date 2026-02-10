# -------- FUNCTION DEFINITIONS --------
def read_numbers(filename):
    """File se numbers read karke list me return kare"""
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    return numbers

def calculate_sum(numbers):
    """Numbers ka sum return kare"""
    return sum(numbers)

def calculate_average(numbers):
    """Numbers ka average return kare"""
    return sum(numbers) / len(numbers)

def write_results(filename, total, average):
    """Results ko output file me write kare"""
    with open(filename, 'w') as f:
        f.write(f"Total: {total}\n")
        f.write(f"Average: {average}\n")

# -------- MAIN PROGRAM --------
input_file = "data.txt"
output_file = "results.txt"

# Step 1: Read numbers
numbers = read_numbers(input_file)

# Step 2: Calculate sum & average
total = calculate_sum(numbers)
average = calculate_average(numbers)

# Step 3: Write results
write_results(output_file, total, average)

print("Processing complete! Check results.txt for output.")
