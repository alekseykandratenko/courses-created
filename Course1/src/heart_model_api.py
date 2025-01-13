from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Cargar el modelo serializado
model_path = 'models/RandomForestClassifier/best_heart_disease_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Crear la aplicación Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener datos del JSON enviado en la solicitud
    data = request.get_json(force=True)
    # Convertir a DataFrame
    input_data = pd.DataFrame([data])
    # Realizar predicción
    prediction = model.predict(input_data)
    # Devolver resultado
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)

# desplegar el modelo mediante comando python src/heart_model_api.py desde carpeta raiz del proyecto