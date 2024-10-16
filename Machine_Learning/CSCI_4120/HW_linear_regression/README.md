# Regression to the Mean - Homework Assignment

This project contains the code and results for completing **Exercise 1 and 2** from the "Regression to the Mean" assignment. These exercises involve data manipulation with pandas and performing simple linear regression using numpy. The results are visualized through scatter plots and regression lines.

## Team Members

- **Jonathan Rogers**  
  Email: jrogers22@students.ecu.edu

- **Ryan Josh Villaluz**  
  Email: villaluzr20@students.ecu.edu

## Contents

- `homework.py`: Main script for Exercises 1 and 2.
- `data/gauss_R2.csv`: Dataset used for the exercises.
- `output1.png`: Scatter plot for Exercise 1.
- `output2.png`: Regression line plot for Exercise 2.

## Exercise 1: Create `y - x` Column in DataFrame

In this exercise, we add a new column `"y-x"` to the DataFrame, where the value of each row is computed as `y - x`.

- **Function**: `y_minus_x(HW)`
- **Output**: DataFrame updated with a new column `y-x`.

```python
def y_minus_x(HW):
    HW['y-x'] = HW['y'] - HW['x']
