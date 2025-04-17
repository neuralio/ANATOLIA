# ANATOLIA PV Yield Anomaly Detection & Forecasting

This repository contains a complete end-to-end workflow for:

  1. Training data generation from PV plant SCADA, satellite (SARAH) and reanalysis (ERA5-Land) datasets.

  2. Model training of an LSTM-based autoencoder for anomaly detection in plant energy yield.

  3. Real-time inference: daily forecasting (with GFS) and online anomaly detection on live plant data.

# 📂 Repository Structure

```
STEP1_Plant_Data/        # Download and preprocess plant SCADA data
├── IA_AGRO/             # Python notebooks for IA_AGRO plant series
│   ├── isolar_S901.ipynb
│   ├── isolar_S902.ipynb
│   ├── isolar_S903.ipynb
│   └── isolar_S905.ipynb
├── SOLAR_KAPITAL/       # Scripts for Solar Kapital plants
│   ├── SK_LAGOS.py
│   ├── SK_Larissa.py
│   ├── SK_Arnissa.py
│   ├── SK_PALAIOK.py
│   ├── SK_Sitia.py
│   ├── SK_ag10.py
│   ├── "SK datalogger and portal access.xlsx"
│   └── README             # notes on credentials & portal API

STEP2_Satellite_Data/     # Download and convert SARAH solar radiation data
└── process_SARAH_to_csv.sh

STEP3_ERA5_Land_Data/     # Download and convert ERA5-Land meteorological data
├── Download_ERA5_LAND.py
├── master_run_ERA5.sh
└── process_ERA5_to_csv.sh

STEP4_Merge_Datasets/     # Merge plant, SARAH & ERA5 datasets
└── merge_weather_sarah_plant.ipynb

STEP5_Training/           # Model training & anomaly detection
├── visualise_data.ipynb  # Exploratory plots & statistics
├── LSTM_autoencoder.h5   # Trained autoencoder weights
└── Predict_detect.ipynb  # Inference, reconstruction error & anomaly plots
```

# 🔄 Workflow
1. STEP 1 – Download Plant Data (```STEP1_Plant_Data/```)

    - Fetch SCADA readings (energy yield, meteorological sensors) for each plant.

    - Scripts/notebooks per plant series handle portal authentication and CSV export.

2. STEP 2 – Satellite Solar Data (```STEP2_Satellite_Data/```)

    - Download hourly surface solar radiation from the SARAH dataset via the Climate Data Store.

    - Convert NetCDF to CSV at plant locations.

3. STEP 3 – ERA5-Land Data (```STEP3_ERA5_Land_Data/```)

    - Download hourly temperature, humidity, pressure etc. from ERA5-Land.

    - Process and save features to CSV.

4. STEP 4 – Merge Datasets (```STEP4_Merge_Datasets/merge_weather_sarah_plant.ipynb```)

    - Join SCADA, SARAH & ERA5 features by timestamp and geolocation.

    - Clean, impute missing data, and split into training/test sets.

5. STEP 5 – Model Training & Anomaly Detection (```STEP5_Training/```)

    - Visualise data distributions and correlations (visualise_data.ipynb).

    - Train LSTM autoencoder on normal operation to learn typical temporal patterns.

    ![Loss](https://github.com/neuralio/ANATOLIA/blob/main/Plots/Loss.png)

    - Compute reconstruction error & set anomaly threshold (e.g. mean + 3σ).

    - Detect and visualise anomalies
      
    ![Reconstruction Error & Detected Anomalies](https://github.com/neuralio/ANATOLIA/blob/main/Plots/Error_and_anomalies.png)

6. Forecasting & Live Monitoring

    - Download GFS forecasts

    - Predict next-day yield and trend using the trained LSTM model.

![True vs Predicted Yield](https://github.com/neuralio/ANATOLIA/blob/main/Plots/True_VS_Predicted_Yield.png)

![Modeled vs Actual Trend](https://github.com/neuralio/ANATOLIA/blob/main/Plots/Model_VS_True_trend.png)

# ⚙️ Requirements

- Python: 3.8+
- Key packages (install via pip or conda):
```numpy, pandas, xarray, netCDF4, requests, cdsapi, tensorflow (or keras), matplotlib, scikit-learn, jupyterlab```
- Shell utilities for batch downloads (bash)







