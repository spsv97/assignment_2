#!/usr/bin/python3

import sys
import datetime

# Check if all parameters are provided
if len(sys.argv) != 4:
    print("Content-type: text/html\n")
    print("Error: Missing parameters. Please provide 'a', 'b', and 'c' in the URL.")
    sys.exit()

# Read parameters from command line arguments
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except ValueError:
    print("Content-type: text/html\n")
    print("Error: Parameters must be numeric.")
    sys.exit()

# Calculate steps
c_cubed = c ** 3
sqrt_c_cubed = c_cubed ** 0.5
division = sqrt_c_cubed / a
multiplication = division * 10
result = multiplication + b

# Display output
print("Assignment 2 Steven Sandoval\n")
print(f"<h2>Final Result: {result}</h2>")
print(f"<p>Step 1: c = {c} , c³ = {c_cubed}</p>")
print(f"<p>Step 2: √(c³) = {sqrt_c_cubed}</p>")
print(f"<p>Step 3: {sqrt_c_cubed} / {a} = {division}</p>")
print(f"<p>Step 4: {division} * 10 = {multiplication}</p>")
print(f"<p>Step 5: {multiplication} + {b} = {result}</p>")
print(f"<p>Calculation completed at {datetime.datetime.now()}</p>")
