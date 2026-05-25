
import streamlit as st

st.set_page_config(page_title="Robo-Advisor", layout="centered")

st.title("🤖 Robo-Advisor Inteligente")
st.subheader("Cuestionario de Perfilado del Inversor")

st.write("Responda las siguientes preguntas para determinar su perfil de inversión.")

# -----------------------------
# PREGUNTA 1
# -----------------------------

p1 = st.selectbox(
    "1. ¿En qué rango de edad se encuentra?",
    [
        "Más de 60 años",
        "Entre 45 y 60 años",
        "Entre 30 y 45 años",
        "Menos de 30 años"
    ]
)

# -----------------------------
# PREGUNTA 2
# -----------------------------

p2 = st.selectbox(
    "2. ¿Cuánto tiempo planea mantener la inversión?",
    [
        "Menos de 1 año",
        "Entre 1 y 3 años",
        "Entre 3 y 7 años",
        "Más de 7 años"
    ]
)

# -----------------------------
# PREGUNTA 3
# -----------------------------

p3 = st.selectbox(
    "3. ¿Cuál es su principal objetivo al invertir?",
    [
        "Preservar capital",
        "Obtener ingresos estables",
        "Crecimiento moderado",
        "Maximizar rentabilidad"
    ]
)

# -----------------------------
# PREGUNTA 4
# -----------------------------

p4 = st.selectbox(
    "4. Si su cartera pierde un 15% en un mes, ¿qué haría?",
    [
        "Vendería toda la inversión",
        "Vendería una parte",
        "Mantendría la inversión",
        "Invertiría más aprovechando la caída"
    ]
)

# -----------------------------
# PREGUNTA 5
# -----------------------------

p5 = st.selectbox(
    "5. ¿Cuál es su experiencia invirtiendo?",
    [
        "Ninguna",
        "Básica",
        "Intermedia",
        "Avanzada"
    ]
)

# -----------------------------
# PREGUNTA 6
# -----------------------------

p6 = st.selectbox(
    "6. ¿Qué porcentaje de sus ingresos mensuales puede ahorrar?",
    [
        "Menos del 5%",
        "Entre 5% y 15%",
        "Entre 15% y 30%",
        "Más del 30%"
    ]
)

# -----------------------------
# PREGUNTA 7
# -----------------------------

p7 = st.selectbox(
    "7. ¿Qué prefiere?",
    [
        "Baja rentabilidad con mínimo riesgo",
        "Rentabilidad moderada con algo de riesgo",
        "Buena rentabilidad aceptando volatilidad",
        "Máxima rentabilidad aunque haya grandes pérdidas"
    ]
)

# -----------------------------
# PREGUNTA 8
# -----------------------------

p8 = st.selectbox(
    "8. ¿Cómo describiría la estabilidad de sus ingresos?",
    [
        "Muy inestables",
        "Algo inestables",
        "Bastante estables",
        "Totalmente estables"
    ]
)

# -----------------------------
# PREGUNTA 9
# -----------------------------

p9 = st.selectbox(
    "9. ¿Qué importancia tiene este dinero para sus necesidades actuales?",
    [
        "Es fundamental para mis gastos diarios",
        "Es importante, pero no imprescindible",
        "Apenas afecta a mi situación financiera",
        "No necesito este dinero a corto plazo"
    ]
)

# -----------------------------
# PREGUNTA 10
# -----------------------------

p10 = st.selectbox(
    "10. ¿Cómo valoraría sus conocimientos financieros?",
    [
        "Muy bajos",
        "Básicos",
        "Intermedios",
        "Avanzados"
    ]
)

# -----------------------------
# DICCIONARIO DE PUNTOS
# -----------------------------

puntos = {
    "Más de 60 años": 5,
    "Entre 45 y 60 años": 10,
    "Entre 30 y 45 años": 15,
    "Menos de 30 años": 20,

    "Menos de 1 año": 5,
    "Entre 1 y 3 años": 10,
    "Entre 3 y 7 años": 15,
    "Más de 7 años": 20,

    "Preservar capital": 5,
    "Obtener ingresos estables": 10,
    "Crecimiento moderado": 15,
    "Maximizar rentabilidad": 20,

    "Vendería toda la inversión": 5,
    "Vendería una parte": 10,
    "Mantendría la inversión": 15,
    "Invertiría más aprovechando la caída": 20,

    "Ninguna": 5,
    "Básica": 10,
    "Intermedia": 15,
    "Avanzada": 20,

    "Menos del 5%": 5,
    "Entre 5% y 15%": 10,
    "Entre 15% y 30%": 15,
    "Más del 30%": 20,

    "Baja rentabilidad con mínimo riesgo": 5,
    "Rentabilidad moderada con algo de riesgo": 10,
    "Buena rentabilidad aceptando volatilidad": 15,
    "Máxima rentabilidad aunque haya grandes pérdidas": 20,

    "Muy inestables": 5,
    "Algo inestables": 10,
    "Bastante estables": 15,
    "Totalmente estables": 20,

    "Es fundamental para mis gastos diarios": 5,
    "Es importante, pero no imprescindible": 10,
    "Apenas afecta a mi situación financiera": 15,
    "No necesito este dinero a corto plazo": 20,

    "Muy bajos": 5,
    "Básicos": 10,
    "Intermedios": 15,
    "Avanzados": 20
}

# -----------------------------
# BOTÓN
# -----------------------------

if st.button("Calcular Perfil"):

    score = (
        puntos[p1] +
        puntos[p2] +
        puntos[p3] +
        puntos[p4] +
        puntos[p5] +
        puntos[p6] +
        puntos[p7] +
        puntos[p8] +
        puntos[p9] +
        puntos[p10]
    )

    st.subheader(f"Puntuación total: {score}")

    # PERFIL

    if score <= 95:
        perfil = "Conservador"
    elif score <= 145:
        perfil = "Moderado"
    else:
        perfil = "Agresivo"

    st.success(f"Perfil detectado: {perfil}")
