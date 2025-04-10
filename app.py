import io
import streamlit as st
import pandas as pd

from dynamic_characterization.ipcc_ar6.radiative_forcing import (
    characterize_co2,
    characterize_ch4,
)
from dynamic_characterization import characterize

st.set_page_config(
    page_title="dynamic-lcia", layout="centered", initial_sidebar_state="collapsed"
)


st.title("Characterize your Dynamic Inventory")

# Dummy CSV data as default input
dummy_csv = """
date,amount,flow,activity
2025-01-01,1,CO2,1
2027-01-01,1,CH4,2
"""

# Create tabs for manual input and CSV upload
tab1, tab2 = st.tabs(["Manual Input", "CSV Upload"])

with tab1:
    df = st.data_editor(
        pd.read_csv(io.StringIO(dummy_csv.strip())),
        num_rows="dynamic",
        use_container_width=True,
    )

with tab2:
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data preview:", df.head())

df["date"] = pd.to_datetime(df["date"].str.strip(), format="%Y-%m-%d")

metric_selection = st.segmented_control(
        "Select Metric", options=["Radiative Forcing", "Global Warming Potential"], default="Radiative Forcing"
    )

if metric_selection:
    metric_mapping = {"Radiative Forcing": "radiative_forcing", "Global Warming Potential": "GWP"}
    metric = metric_mapping[metric_selection]
    
    col_th_rf, col_th_rf_f = st.columns([3, 1])
    with col_th_rf:
        time_horizon_rf = st.slider(
            "Time Horizon",
            min_value=2,
            max_value=200,
            value=100,
            step=1,
        )
    with col_th_rf_f:
        fixed_th_rf = st.checkbox("Fixed Time Horizon", value=False, key="fixed_checkbox_rf")

    characterized_df = characterize(
        df,
        metric=metric,
        characterization_functions={
            "CO2": characterize_co2,
            "CH4": characterize_ch4,
        },
        time_horizon=time_horizon_rf,
        fixed_time_horizon=fixed_th_rf,
    )

    plot_data = characterized_df.pivot(
                    index="date", columns="flow", values="amount"
                )
    st.scatter_chart(plot_data)
