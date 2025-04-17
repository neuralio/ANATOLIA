# ANATOLIA PV Yield Anomaly Detection & Forecasting

This repository contains a complete end-to-end workflow for:

  1. Training data generation from PV plant SCADA, satellite (SARAH) and reanalysis (ERA5-Land) datasets.

  2. Model training of an LSTM-based autoencoder for anomaly detection in plant energy yield.

  3. Real-time inference: daily forecasting (with GFS) and online anomaly detection on live plant data.
