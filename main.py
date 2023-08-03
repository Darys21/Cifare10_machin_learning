# Author: Joan Anguilet
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf
from PIL import Image


def main():
    """
    This is the main function of the Cifar10 Web classifier. It allows users to upload an image and see the prediction of the image's class. The function takes no parameters.

    Returns:
    None
    """
    st.title('Cifar10 Web classifier')
    st.write('upload any image that you think fits into one of the classes and see if the prediction is ...')

    file = st.file_uploader('please upload an image', type=['jpg','png'])
    if file:
        image= Image.open(file)
        st.image(image, use_column_width=True)

        resized_image = image.resize((32,32))
        image_array = np.array(resized_image) / 255
        image_array = image_array.reshape((1, 32, 32, 3))

        model = tf.keras.models.load_model('cifar10_model.h5')

        predictions = model.predict(image_array)

        cifar10_classes = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, predictions[0],align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis
        ax.set_xlabel("Probability")
        ax.set_title('CIFARE10 Predictions')

        st.pyplot(fig)
    else:
        st.text('you have not uploaded an image  yet')

#call the main function
if __name__ == '__main__':
    #run the app
    main()
