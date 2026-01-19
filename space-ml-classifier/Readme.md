# Astronomical Object Classification using Machine Learning

This project uses real astronomical data from the Sloan Digital Sky Survey (SDSS) to classify space objects such as Stars, Galaxies, and Quasars using Machine Learning techniques.

The goal of this project is to demonstrate how ML models can be applied to real-world scientific datasets for classification tasks.

---

## Dataset

The dataset is sourced from an open astronomy dataset containing spectral features of space objects.

Features used:
- u (Ultraviolet magnitude)
- g (Green band magnitude)
- r (Red band magnitude)
- i (Infrared magnitude)
- z (Near-infrared magnitude)

Target Classes:
- STAR
- GALAXY
- QSO (Quasar)

Dataset source: [Hugging Face – Allanatrix/Astro](https://huggingface.co/datasets/Allanatrix/Astro)

---

## Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  
- VS Code  

---

## Project Workflow

1. Loaded and explored the astronomical dataset  
2. Selected relevant spectral features (`u, g, r, i, z`)  
3. Preprocessed data using standard scaling  
4. Split dataset into training and testing sets  
5. Trained Logistic Regression classifier  
6. Evaluated model performance using accuracy and classification report  
7. Visualized classification results with a confusion matrix  

---

## How to Run

Install dependencies
pip install pandas scikit-learn matplotlib

Run the program
Make sure the dataset file star_classification.csv is in the same folder as model.py.
python model.py

You should see:
Printed dataset information
Model accuracy
Classification report
Confusion matrix visualization

---

## Output example

Dataset Loaded Successfully!
Shape: (100000, 17)
Columns: ['u', 'g', 'r', 'i', 'z', 'class', ...]
Class distribution:
STAR     60000
GALAXY   30000
QSO      10000
Model Accuracy: 0.95
Confusion Matrix:
[[...]]

---

## Future Improvements

Use advanced ML models like Random Forest, SVM, or Neural Networks
Perform hyperparameter tuning for better accuracy
Implement cross-validation
Enhance visualization techniques for more insight

---

# Author

Alan John Thomas
MCA Student, CUSAT
