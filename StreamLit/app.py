import streamlit as st
import tensorflow as tf
import numpy as np

# Set Streamlit app title and page configuration
st.set_page_config(page_title="Road Condition Classifier", layout="wide")

# Custom CSS for dark mode
custom_css = """
<style>
/* Dark mode background */
body {
    background-color: #121212;
    color: white;
}

/* Custom CSS for progress bar */
.stProgressBar > div > div > div {
    background-color: #FFA500 !important;  /* Orange progress bar color */
    height: 20px;  /* Adjust height */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Add a title to the app
st.title("Road Condition Classifier")

# Add a subtitle to the app
st.subheader("Predict road conditions using Deep learning")

# Load the SavedModel
loaded_model = tf.saved_model.load('DENSEMODEL')

# Get the default serving signature
inference_function = loaded_model.signatures["serving_default"]

# Add a section heading for image upload
st.header("Upload Image")

# Allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Load and preprocess the image
    image = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(224, 224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array /= 255.0

    # Perform inference using the loaded model
    with st.spinner("Processing image..."):
        result = inference_function(tf.constant(image_array))['output_0']
        result_array = result.numpy()

    # Define class labels
    class_labels = ['fair', 'flooded', 'good', 'poor', 'unpaved']

    # Get the predicted label
    predicted_label_index = np.argmax(result_array)
    predicted_label = class_labels[predicted_label_index]

    # Display the predicted label
    st.subheader("Prediction")
    st.write("Predicted Road Condition:", predicted_label)

    # Explain the classes
    st.subheader("Explanation of Classes")
    st.markdown("""
    - **Good**: Roads with minimal surface imperfections, exhibiting optimal condition.
    - **Fair**: Roads showcasing minor cracking or superficial wear.
    - **Poor**: Roads characterized by significant surface deterioration, including deep potholes or cracks.
    - **Flooded**: Roads inundated with water, either due to natural calamities or poor drainage systems.
    - **Unpaved**: Roads composed of earth or gravel, lacking paved surfaces.
    """)

# Add a footer to mention the app developer
footer = """
---
<div class="footer">
<b>Developed by:</b><br>
Lisa Maina | Valerie Vinya | Stephen Kariuki | Wilkins Nzioka | Colins Wanjao
</div>
"""
st.markdown(footer, unsafe_allow_html=True)