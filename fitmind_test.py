import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="FitMind App", page_icon=":brain:")

# Set app title
st.title("FitMind - Holistische Gesundheits-App")

# Add description
st.markdown("""
FitMind ist eine ganzheitliche Gesundheits-App, die Fitness und mentales Wohlbefinden kombiniert, um Benutzern zu helfen, ein ausgewogenes und gesundes Leben zu führen.
""")

# Sidebar layout
st.sidebar.title("Navigation")
page = st.sidebar.radio("Seiten", ["Startseite", "Fitness Tracker", "Mental Health"])

# Startseite
if page == "Startseite":
    st.image(Image.open("fitness_mind.jpg"), use_column_width=True)

    st.subheader("Willkommen bei FitMind!")
    st.write("FitMind unterstützt dich dabei, deine Fitnessziele zu erreichen und gleichzeitig dein mentales Wohlbefinden zu verbessern.")

# Fitness Tracker
elif page == "Fitness Tracker":
    st.subheader("Fitness Tracker")

    # Input Widgets
    age = st.slider("Alter", 18, 100, 25)
    weight = st.number_input("Gewicht (kg)", min_value=20.0, max_value=500.0, value=70.0, step=0.1)
    height = st.number_input("Größe (cm)", min_value=100, max_value=300, value=170, step=1)
    activity_level = st.selectbox("Aktivitätslevel", ["Sedentär", "Leicht aktiv", "Mäßig aktiv", "Sehr aktiv", "Extrem aktiv"])

    # Data elements
    bmi = weight / ((height/100) ** 2)
    st.write(f"Ihr BMI beträgt: {bmi:.2f}")

    # Chart elements
    data = pd.DataFrame({
        'Kategorie': ['Untergewicht', 'Normalgewicht', 'Übergewicht', 'Adipositas'],
        'BMI-Bereich': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '≥ 30.0'],
        'Empfehlung': ['Zunehmen', 'Normalgewicht halten', 'Abnehmen', 'Stark abnehmen']
    })
    st.write("BMI-Klassifikation:")
    st.dataframe(data)

    sns.barplot(x='Kategorie', y='BMI-Bereich', data=data)
    st.pyplot()

# Mental Health
elif page == "Mental Health":
    st.subheader("Mental Health")

    # Text elements
    st.write("Wie geht es dir heute?")

    # Input Widgets
    mood = st.slider("Stimmung", 0, 10, 5)
    stress_level = st.slider("Stresslevel", 0, 10, 5)

    # Chart elements
    mood_data = pd.DataFrame({
        'Datum': pd.date_range(start='2024-01-01', periods=30),
        'Stimmung': np.random.randint(0, 11, size=30),
        'Stresslevel': np.random.randint(0, 11, size=30)
    })
    st.write("Verlauf der Stimmung und des Stresslevels:")
    st.line_chart(mood_data.set_index('Datum'))

# Footer
st.sidebar.markdown("---")
st.sidebar.subheader("Über uns")
st.sidebar.info("Diese App wurde von Julia und Max entwickelt.")

st.sidebar.subheader("Kontakt")
st.sidebar.text("Bei Fragen oder Anregungen kontaktieren Sie uns unter:")
st.sidebar.text("fitmind@example.com")

