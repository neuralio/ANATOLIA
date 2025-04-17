# ANATOLIA PV Yield Anomaly Detection & Forecasting

This repository contains a complete end-to-end workflow for:

  1. Training data generation from PV plant SCADA, satellite (SARAH) and reanalysis (ERA5-Land) datasets.

  2. Model training of an LSTM-based autoencoder for anomaly detection in plant energy yield.

  3. Real-time inference: daily forecasting (with GFS) and online anomaly detection on live plant data.

📂 Repository Structure

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


