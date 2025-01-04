# Pneumonia Classification Web App

A Streamlit-based web application for classifying chest X-ray images as pneumonia or normal using a pre-trained deep learning model.

## Table of Contents
- Features
- Directory Structure
- Installation
- Usage
- Credits

---

## Features
- **Pneumonia Classification**: Upload a chest X-ray image, and the app predicts whether the image indicates pneumonia or is normal.
- **Interactive Interface**: A user-friendly interface was created with Streamlit.
- **Confidence Scores**: Displays confidence scores for each prediction.
- **Background Customization**: Custom background image for a polished UI.

---

## Directory Structure
pneumonia-classification-web-app-python-streamlit/  
├── main.py                  # Main Streamlit app script  
├── util.py                  # Utility functions for classification and background setting  
├── requirements.txt         # Python dependencies  
├── models/  
│   ├── labels.txt           # Class labels for the model  
│   └── classifier.h5        # Pre-trained model  
├── bgs/  
│   └── bg5.png              # Background image  


---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pneumonia-classification-web-app-python-streamlit.git
   cd pneumonia-classification-web-app-python-streamlit
2. Install dependencies
   ```bash
   pip install -r requirements.txt

---

## Usage
1. Run the application
   ```bash
   streamlit run main.py
3. Open the app in your browser at http://localhost:8501.
4. Upload a chest X-ray image in JPEG, PNG, or JPG format. The app will display the image and classify it as either:
   * Normal
   * Pneumonia

---

## Credits
* Model: Pre-trained deep learning model (classifier.h5) for pneumonia classification.
* Streamlit: Framework for building interactive web apps with Python.
* Dependencies: All required libraries are listed in requirements.txt.

---

Feel free to report issues or contribute enhancements to the repository! 😊
