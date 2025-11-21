import streamlit as st
from backend.encryption import cesar_cipher
from backend.encryption import vigenere_cipher
from backend.watermarking_logic import decode_text_from_image
from backend.watermarking_logic import encode_text_in_image, save_image
from PIL import Image
import numpy as np

st.title("Image Watermarking Messaging App")
st.write("This app encodes a hidden text message into an image using LSB steganography.")
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
text_message = st.text_area("Enter the text message to encode:")
password = st.text_input("Enter the password for encryption/decryption:", type="password")

col1, col2 = st.columns(2)

with col1:
    encode_button = st.button("Encode Message")

with col2:
    decode_button = st.button("Decode Message")

if encode_button:
    if uploaded_image is not None and text_message:
        img = Image.open(uploaded_image)
        img_array = np.array(img)

        encrypted_message = vigenere_cipher(text_message, "password", True)
        encoded_array = encode_text_in_image(img_array, encrypted_message)
        encoded_img = Image.fromarray(encoded_array.astype('uint8'))

        output_path = "encoded_image.png"
        save_image(encoded_img, output_path)

        st.success("Message encoded successfully!")
        st.image(encoded_img, caption="Encoded Image")
    else:
        st.error("Please upload an image and enter a text message.")

if decode_button:
    if uploaded_image is not None:

        img = Image.open(uploaded_image)
        hidden_message = decode_text_from_image(img)
        decrypted_message = vigenere_cipher(hidden_message, "password", False)

        st.success("Message decoded successfully!")
        st.write("Hidden Message:")
        st.write(decrypted_message)
    else:
        st.error("Please upload an image to decode.")

try:
    with open("encoded_image.png", "rb") as file:
        st.download_button(
            label="Download Encoded Image",
            data=file,
            file_name="encoded_image.png",
            mime="image/png"
        )
except FileNotFoundError:
    pass