import streamlit as st

# Configuración de la página
st.set_page_config(page_title="EsSalud - Programación de Citas", page_icon="🏥", layout="centered")

# Estilos visuales básicos
st.markdown("""
    <style>
    .main-header { font-size: 28px; font-weight: bold; color: #0056b3; }
    .step-text { font-size: 18px; font-weight: bold; color: #333; }
    .success-msg { padding: 15px; background-color: #d4edda; color: #155724; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🏥 Portal de Citas - EsSalud</p>', unsafe_allow_html=True)

st.sidebar.header("👤 Mi Perfil")
perfil_seleccionado = st.sidebar.radio("¿Para quién es la cita?", ["Mi cuenta (Titular)", "Familiar (Derechohabiente)"])

if perfil_seleccionado == "Familiar (Derechohabiente)":
    st.sidebar.selectbox("Seleccione el familiar:", ["María Ancalla (Madre)", "Juan Sotil (Padre)"])

st.sidebar.divider()
st.sidebar.button("🚪 Cerrar Sesión")

# Menú principal de navegación
pestana1, pestana2 = st.tabs(["📅 Nueva Cita", "📋 Mis Citas Programadas"])

with pestana1:
    st.write(f"Agendando cita para: **{perfil_seleccionado}**")
    st.progress(25)
    
    st.markdown('<p class="step-text">Paso 1: Centro de Atención y Especialidad</p>', unsafe_allow_html=True)
    centro = st.selectbox("Seleccione su Centro de Atención (Red):", ["Seleccione", "Hospital Edgardo Rebagliati", "Hospital Guillermo Almenara", "Policlínico Chincha"])
    especialidad = st.selectbox("Seleccione la Especialidad:", ["Seleccione", "Medicina General", "Cardiología", "Geriatría", "Odontología"])
    
    if centro and especialidad:
        st.progress(60)
        st.markdown('<p class="step-text">Paso 2: Fechas y Horarios Disponibles</p>', unsafe_allow_html=True)
        fecha = st.date_input("Seleccione la fecha preferida:")
        medico = st.selectbox("Seleccione el médico:", ["Dr. Carlos Mendoza", "Dra. Ana Rojas (Disponible hoy)"])
        
        horario = st.radio("Seleccione el horario:", ["08:00 AM - 08:30 AM", "09:30 AM - 10:00 AM", "11:00 AM - 11:30 AM (Último cupo)"])
        
        if horario:
            st.progress(90)
            st.markdown('<p class="step-text">Paso 3: Confirmación</p>', unsafe_allow_html=True)
            st.warning("⚠️ Recuerde que tiene 2 minutos para confirmar este horario antes de que sea liberado.")
            
            # Confirmación explícita (Prevención de errores)
            if st.button("✅ Confirmar Cita Médica", type="primary"):
                st.progress(100)
                st.markdown(f"""
                <div class="success-msg">
                    <b>¡Cita Confirmada Exitosamente!</b><br>
                    <b>Paciente:</b> {perfil_seleccionado}<br>
                    <b>Especialidad:</b> {especialidad} en {centro}<br>
                    <b>Fecha y Hora:</b> {fecha} a las {horario[:8]}<br>
                    <b>Código de Reserva:</b> ESS-2026-X98V
                </div>
                """, unsafe_allow_html=True)

with pestana2:
    st.markdown('<p class="step-text">Citas Próximas</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("**Medicina General**\n\nHospital Rebagliati - 15/10/2026 09:00 AM")
    with col2:
        if st.button("❌ Cancelar Cita"):
            st.error("¿Está seguro que desea cancelar esta cita? Esta acción no se puede deshacer.")
            st.button("Sí, cancelar definitivamente")