import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Heat Exchanger Visualizer")

st.title("🌡️ Heat Exchanger Performance Visualizer")
st.markdown(
    """
    Compare the performance of **Parallel Flow** and **Counter Flow** heat exchangers 
    based on input temperatures, flow rates, and design specifications.
    """
)

# --- Sidebar Inputs ---
st.sidebar.header("🔧 Input Parameters")

# Hot Fluid Inputs
st.sidebar.subheader("Hot Fluid")
m_hot = st.sidebar.number_input("Mass Flow Rate (kg/s)", value=1.5, min_value=0.01)
Cp_hot = st.sidebar.number_input("Specific Heat Cp (kJ/kg·K)", value=4.2, min_value=0.1)
T_hot_in = st.sidebar.number_input("Inlet Temperature (°C)", value=140.0)
T_hot_out = st.sidebar.number_input("Outlet Temperature (°C)", value=90.0)

# Cold Fluid Inputs
st.sidebar.subheader("Cold Fluid")
m_cold = st.sidebar.number_input("Mass Flow Rate (kg/s)", value=2.0, min_value=0.01)
Cp_cold = st.sidebar.number_input("Specific Heat Cp (kJ/kg·K)", value=4.18, min_value=0.1)
T_cold_in = st.sidebar.number_input("Inlet Temperature (°C)", value=30.0)
T_cold_out = st.sidebar.number_input("Outlet Temperature (°C)", value=70.0)

# Heat Exchanger Design
st.sidebar.subheader("Heat Exchanger Design")
U = st.sidebar.number_input("Overall Heat Transfer Coefficient U (W/m²·K)", value=600.0)
A = st.sidebar.number_input("Heat Transfer Area A (m²)", value=25.0)

# Flow Type
flow_type = st.selectbox("Flow Configuration", ["Parallel Flow", "Counter Flow"])

# --- Calculations ---
Q_hot = m_hot * Cp_hot * (T_hot_in - T_hot_out) * 1000  # W
Q_cold = m_cold * Cp_cold * (T_cold_out - T_cold_in) * 1000  # W
Q_actual = min(Q_hot, Q_cold)  # Actual heat transfer rate (W)

# Log Mean Temperature Difference (LMTD)
if flow_type == "Parallel Flow":
    delta_T1 = T_hot_in - T_cold_in
    delta_T2 = T_hot_out - T_cold_out
else:  # Counter Flow
    delta_T1 = T_hot_in - T_cold_out
    delta_T2 = T_hot_out - T_cold_in

if delta_T1 != delta_T2:
    LMTD = (delta_T1 - delta_T2) / np.log(delta_T1 / delta_T2)
else:
    LMTD = delta_T1  # Avoid division by zero

Q_LMTD = U * A * LMTD  # Estimated heat transfer using LMTD (W)

# Effectiveness Calculation
C_min = min(m_hot * Cp_hot, m_cold * Cp_cold)
Q_max = C_min * (T_hot_in - T_cold_in) * 1000  # Maximum possible heat transfer (W)
effectiveness = Q_actual / Q_max

# --- Output Results ---
st.subheader("📊 Results Summary")
col1, col2 = st.columns(2)
col1.metric("Heat Duty (Q)", f"{Q_actual / 1000:.2f} kW")
col2.metric("Effectiveness (ε)", f"{effectiveness:.2f}")

st.write(f"**LMTD**: `{LMTD:.2f} °C`")
st.write(f"**Estimated Q (via LMTD)**: `{Q_LMTD / 1000:.2f} kW`")

# --- Temperature Profile Plot ---
st.subheader("📈 Temperature Distribution")

x = np.linspace(0, 1, 50)


# Profiles for both flow types
T_hot_profile = T_hot_in - (T_hot_in - T_hot_out) * x
if flow_type == "Parallel Flow":
    T_cold_profile = T_cold_in + (T_cold_out - T_cold_in) * x
else:
    T_cold_profile = T_cold_out - (T_cold_out - T_cold_in) * x[::-1]

    plt.figure(figsize=(7, 4))
plt.plot(x, T_hot_profile, label="Hot Fluid", color="crimson", linewidth=2)
plt.plot(x, T_cold_profile, label="Cold Fluid", color="royalblue", linewidth=2)
plt.xlabel("Normalized Exchanger Length")
plt.ylabel("Temperature (°C)")
plt.title(f"Temperature Profile - {flow_type}")
plt.grid(True)
plt.legend()
plt.tight_layout()
st.pyplot(plt.gcf())
