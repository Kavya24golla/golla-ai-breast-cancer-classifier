
from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model("model.h5")

def preprocess(image):
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        image = Image.open(file).convert("RGB")
        input_data = preprocess(image)
        prediction = model.predict(input_data)
        class_names = ["Benign", "Malignant", "Normal"]
        result = class_names[np.argmax(prediction)]
        return render_template("index.html", prediction=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
