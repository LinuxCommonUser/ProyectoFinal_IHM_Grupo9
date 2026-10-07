import streamlit as st
import datetime
import time

# Configuración de la página
st.set_page_config(page_title="EsSalud - Programación de Citas", page_icon="🏥", layout="centered")

# Estilos visuales básicos
st.markdown("""
    <style>
    .main-header { font-size: 28px; font-weight: bold; color: #0056b3; }
    .step-text { font-size: 18px; font-weight: bold; color: #333; margin-top: 20px; }
    .success-msg { padding: 15px; background-color: #d4edda; color: #155724; border-radius: 5px; border-left: 5px solid #28a745; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🏥 Portal de Citas - EsSalud</p>', unsafe_allow_html=True)

# Simulación de sesión y selección de perfil (Mejorado: Lenguaje más claro)
st.sidebar.markdown("### 👤 Mi Perfil")
st.sidebar.info("Seleccione para quién es la cita:")
perfil_seleccionado = st.sidebar.radio(
    "", 
    ["Mi cuenta (Titular)", "Familiar dependiente (Hijo/Esposo)"]
)

if perfil_seleccionado == "Familiar dependiente (Hijo/Esposo)":
    familiar = st.sidebar.selectbox("Seleccione el familiar registrado:", ["María Mendez (Madre)", "Juan Benito (Padre)"])
else:
    familiar = "Jose Benito (Titular)"

st.sidebar.divider()
st.sidebar.button("🚪 Cerrar Sesión")

# Menú principal de navegación
pestana1, pestana2 = st.tabs(["📅 Nueva Cita", "📋 Mis Citas Programadas"])

with pestana1:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"Agendando cita para: **{familiar if perfil_seleccionado != 'Mi cuenta (Titular)' else 'Titular'}**")
    with col2:
        # Control y libertad: Botón para limpiar formulario
        if st.button("🔄 Reiniciar selección"):
            st.rerun()

    st.progress(25)
    
    # Paso 1: Centro de Atención 
    st.markdown('<p class="step-text">Paso 1: Centro de Atención y Especialidad</p>', unsafe_allow_html=True)
    centro = st.selectbox("Seleccione su Centro de Atención (Red):", ["Seleccione", "Hospital Edgardo Rebagliati", "Hospital Guillermo Almenara", "Policlínico Chincha"])
    especialidad = st.selectbox("Seleccione la Especialidad:", ["Seleccione", "Medicina General", "Cardiología", "Geriatría", "Odontología"])
    
    if centro and especialidad:
        st.progress(60)
        
        # Paso 2: Selección de Médico y Horario
        st.markdown('<p class="step-text">Paso 2: Fechas y Horarios Disponibles</p>', unsafe_allow_html=True)
        
        # Prevención de errores: Bloquear fechas en el pasado
        hoy = datetime.date.today()
        fecha = st.date_input("Seleccione la fecha preferida:", min_value=hoy)
        
        # Validación extra