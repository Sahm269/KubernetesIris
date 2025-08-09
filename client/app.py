# client/app.py

import streamlit as st
import requests
import pandas as pd

# 🌟 Mise en page
st.set_page_config(page_title="🌸My beautiful App Iris", layout="centered")
st.title("🌸 Classificateur de Fleurs Iris")
st.markdown("Entrez les caractéristiques de votre fleur et découvrez son espèce !")

# 📊 Exemples à tester
examples = pd.DataFrame({
    "sepal_length": [5.1, 6.0, 6.3],
    "sepal_width":  [3.5, 2.2, 3.3],
    "petal_length": [1.4, 4.0, 6.0],
    "petal_width":  [0.2, 1.0, 2.5],
    "label": ["Setosa", "Versicolor", "Virginica"]
})

st.subheader("🌼 Exemples rapides à tester")
selected_row = st.radio("Choisissez un exemple :", options=examples.index, format_func=lambda i: f"{examples.iloc[i]['label']}")

example = examples.iloc[selected_row]

# 📥 Entrées utilisateur
st.subheader("🔧 Paramètres personnalisés")

sepal_length = st.slider("Longueur du sépale (cm)", 4.0, 8.0, float(example["sepal_length"]))
sepal_width = st.slider("Largeur du sépale (cm)", 2.0, 4.5, float(example["sepal_width"]))
petal_length = st.slider("Longueur du pétale (cm)", 1.0, 7.0, float(example["petal_length"]))
petal_width = st.slider("Largeur du pétale (cm)", 0.1, 2.5, float(example["petal_width"]))

# 📦 API + Affichage résultat
if st.button("🔍 Prédire la classe"):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    try:
        response = requests.post("http://mlops-server-service:8000/predict/v1", json=payload)
        result = response.json()
        prediction = result["prediction"]

        

        classes = ["Setosa", "Versicolor", "Virginica"]
        images = {
            "Setosa": "https://upload.wikimedia.org/wikipedia/commons/4/49/Iris_setosa_1.jpg",
            "Versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
            "Virginica": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
        }

        st.balloons()
        flower = classes[prediction]
        st.success(f"🌼 Prédiction : **{flower}**")
        st.image(images[flower], caption=f"{flower}", use_column_width=True)

    except Exception as e:
        st.error("Une erreur est survenue lors de la prédiction.")
        st.exception(e)
