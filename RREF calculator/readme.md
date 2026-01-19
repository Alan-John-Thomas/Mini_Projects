Matrix REF & RREF Calculator (Python)

This project computes the Row Echelon Form (REF) and Reduced Row Echelon Form (RREF) of a matrix using exact rational arithmetic via Python’s fractions.Fraction module.
It avoids floating-point errors by working entirely with fractions.

✨ Features

✅ Computes REF (Row Echelon Form)
✅ Computes RREF (Reduced Row Echelon Form)
✅ Uses exact fractions (no rounding errors)
✅ Optional step-by-step row operation printing
✅ Automatically arranges rows based on pivot positions
✅ Supports any matrix size

📦 Requirements

Python standard library only:
Python 3.x
(No external dependencies)

▶ How to Run

Clone the repository:

git clone <your-repo-link>
cd <your-project-folder>

Run the program:
python filename.py

📥 Input Format

Step 1: Enter Matrix Size
enter the number of rows: 3
enter the number of columns: 3

Step 2: Enter Matrix Rows

Enter space-separated values.
Fractions and integers are supported.

Example:

Enter row 1: 1 2 3
Enter row 2: 2 4 6
Enter row 3: 1 1 1

Step 3: Choose Operation
1. Find REF
2. Find RREF

Step 4 (RREF Only): Print Steps Option
1. Print steps
2. Don't print steps

📤 Output Example

For RREF:

the RREF of the matrix is:
['1', '0', '-1']
['0', '1', '2']
['0', '0', '0']


Fractions appear as:
3/2 , -5/4 , etc.

⚙ How It Works (Internals)

Algorithm Used

Gaussian Elimination (REF)
Gauss–Jordan Elimination (RREF)

Key Techniques

Pivot detection
Row normalization
Row swapping based on pivot position
Exact fraction arithmetic
Forward elimination (REF)
Forward + backward elimination (RREF)

🧠 Why Fractions Instead of Floats?

Floating-point arithmetic causes rounding errors:
Example:
0.1 + 0.2 ≠ 0.3 (exactly)
This project avoids that by using:
from fractions import Fraction
So results are mathematically exact ✅

📁 Project Structure

project-folder/
│
├── main.py (your file)
├── README.md

🚀 Future Improvements (Optional Ideas)

Add matrix determinant
Add inverse calculation
GUI version (Tkinter / Web)
Input from file
Matrix rank calculation

🧑‍💻 Author

Alan John Thomas
