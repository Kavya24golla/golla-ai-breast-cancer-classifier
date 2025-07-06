# Breast Cancer Detection Web App

This is a deep learning web app using **Flask** and **TensorFlow**.
It predicts breast cancer category: **Benign**, **Malignant**, or **Normal**.

## Project Structure

```
cancer_detection/
├── app.py
├── cancer_model.h5
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

##  How to Run
1. Install required libraries:
   ```
   pip install -r requirements.txt
   ```
2. Run the Flask app:
   ```
   python app.py
   ```
3. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

##  Model
`cancer_model.h5` must be in the same folder as `app.py`. This is your trained CNN model.

##  Built With
- Flask
- TensorFlow
- NumPy
- Pillow (for image processing)

##  Created by Kavya 
