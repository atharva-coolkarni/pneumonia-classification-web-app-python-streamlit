import base64
import streamlit as st

def set_background(image_file):
    """
    This function sets the background of a streamlit app to an image specified by the given image file.
    
    Parameters:
        image_file (str): The path to the image file to be used as the background
        
    Returns:
        None
    """
    pass

def classify(image, model, class_names):    
    """
    This function takes an image, a model, and a list of class names and returns the predicted class and confidence
    score of the image.
    
    Parameters:
        image (PIL.Image.Image): An image to be classified.
        model (tensorflow.keras.Model): A trained machine learning model for image classification.
        class_names (list): A list of class names corresponding to the classes that the model can predict.
        
    Returns:
        A tuple of the predicted class name and the confidence score for the prediction
    """
    
    # convert image to (224, 224)
    
    #  convert image to numpy array
    
    # normalize image
    
    # set model input
    
    # make prediction
    
    pass