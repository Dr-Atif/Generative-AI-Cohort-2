import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Create a sidebar for navigation
st.sidebar.header("Operations")

# Define the operation selection
operation = st.sidebar.selectbox(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division", 
     "Square Root", "Power", "Logarithm")
)

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Perform the chosen operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
elif operation == "Square Root":
    result = math.sqrt(num1)
elif operation == "Power":
    result = math.pow(num1, num2)
elif operation == "Logarithm":
    if num1 > 0:
        result = math.log(num1, num2)  # Log base num2
    else:
        result = "Error: Logarithm of non-positive number"

# Display the result
st.subheader("Result:")
st.write(result)

