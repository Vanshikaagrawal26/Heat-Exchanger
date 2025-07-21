# 🌡️ Heat Exchanger Performance Visualizer

This project is a Python-based Streamlit application designed to compare the performance of **Parallel Flow** and **Counter Flow** heat exchangers. It offers an interactive visualization of temperature profiles and quantifies the heat transfer and efficiency of both configurations.

---

## 🔍 What is a Heat Exchanger?

A **heat exchanger** is a device used to transfer thermal energy between two fluids at different temperatures without mixing them. It is widely used in chemical industries, power plants, refrigeration systems, and automobile radiators.

Heat exchangers enhance energy efficiency by recovering heat from exhaust streams or cooling hot fluids without using additional energy sources.

---

## 🔁 Configurations Compared

### 🔸 Parallel Flow Heat Exchanger
- **Both fluids flow in the same direction**, entering and exiting the exchanger from the same ends.
- High temperature difference at the start, but it quickly reduces, leading to lower efficiency.
- Less effective in transferring heat.

### 🔹 Counter Flow Heat Exchanger
- **Fluids flow in opposite directions**, entering the exchanger from opposite ends.
- Maintains a more uniform temperature gradient.
- Higher outlet temperature of cold fluid and better thermal performance.

---

## 🧮 Formulas Used

### 1. **Heat Transfer Rate (Q):**
\[
Q = m \cdot C_p \cdot (T_{\text{in}} - T_{\text{out}})
\]
- \( m \): mass flow rate (kg/s)  
- \( C_p \): specific heat (J/kg·K)  
- \( T_{\text{in}}, T_{\text{out}} \): inlet and outlet temperatures

---

### 2. **Maximum Possible Heat Transfer (Q_max):**
\[
Q_{\text{max}} = C_{\min} \cdot (T_{h,in} - T_{c,in})
\]
- \( C_{\min} = \min(m \cdot C_p) \) between hot and cold fluids

---

### 3. **Effectiveness (ε):**
\[
\varepsilon = \frac{Q_{\text{actual}}}{Q_{\text{max}}}
\]

---







