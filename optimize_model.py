import tensorflow as tf
import os

model = tf.keras.models.load_model("model.h5")

convert = tf.lite.TFLiteConverter.from_keras_model(model)
convert.optimizations = [tf.lite.Optimize.DEFAULT]

dynamic = convert.convert()

with open("model.tflite", "wb") as f:
    f.write(dynamic)

print("Modelo salvo com sucesso. (Dynamic Range Quantization)")

convert_float16 = tf.lite.TFLiteConverter.from_keras_model(model)
convert_float16.optimizations = [tf.lite.Optimize.DEFAULT]
convert_float16.target_spec.supported_types = [tf.float16]

tflite_float16 = convert_float16.convert()

with open("model_float16.tflite", "wb") as f:
    f.write(tflite_float16)

print("Modelo salvo com sucesso. (Float16)")

sizeDNQ = os.path.getsize("model.tflite") / 1024
sizeF16 = os.path.getsize("model_float16.tflite") / 1024

print(f"Tamanho com Dynamic Range Quantization: {sizeDNQ: .2f}KB.")
print(f"Tamanho com Float16: {sizeF16: .2f}KB.")
print(f"Diferença de tamanho: {(sizeF16 - sizeDNQ): .2f}KB.")
