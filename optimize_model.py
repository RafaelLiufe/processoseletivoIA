import tensorflow as tf
import os

model = tf.keras.models.load_model("model.h5")

convert = tf.lite.TFLiteConverter.from_keras_model(model)
convert.optimizations = [tf.lite.Optimize.DEFAULT]

dynamic = convert.convert()

with open("model.tflite", "wb") as f:
    f.write(dynamic)

print("Modelo salvo com sucesso.")

size = os.path.getsize("model.tflite") / 1024
print(f"Tamanho com Dynamic Range Quantization: {size: .2f}")
