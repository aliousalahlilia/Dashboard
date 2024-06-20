# Step 1: Clean the data
df_cleaned = clean_data(df)
df_cleaned.show(5)

# Step 2: Create features
df_features = create_features(df_cleaned)
df_joined = df_cleaned.join(df_features, on=["ID", "NUM_ENR", "NO_DOSSIER_NAT"], how="inner")
df_joined.show(5)

# Step 3: Convert Spark DataFrame to Pandas DataFrame
df_pandas = df_joined.toPandas()
print(df_pandas.columns)


# Step 4: Perform PCA and Isolation Forest (create_labels functionality)
# def create_labels(df_pandas, n_estimators=200, contamination=0.01):
#     # Define feature columns
#     feature_columns = [
#         "TotalPrescriptionsPerMonth", "TotalCostPerMonth", 
#         "DaysBetweenLastPrescriptionforSameMedic", "DaysBetweenPrescriptions", 
#         "TotalMedicationsPerMonth", "CostAnomaly",
#         "PrescriptionCost_QuantityInteraction", "WeightedAvgQuantity",
#         "WeightedQuantityDeviation", "WeightedTotalQuantityMedicationPerMonth"
#     ]
    
#     # Perform PCA on selected features
#     pca = PCA(n_components=10)
#     pca_features = pca.fit_transform(df_pandas[feature_columns])
    
#     # Apply Isolation Forest for anomaly detection
#     iso_forest_best = IsolationForest(n_estimators=n_estimators, contamination=contamination, random_state=42)
#     iso_forest_best.fit(pca_features)
    
#     # Add anomaly scores and labels to DataFrame
#     df_pandas['anomaly_score'] = iso_forest_best.decision_function(pca_features)
#     df_pandas['anomaly'] = iso_forest_best.predict(pca_features)
#     df_pandas['anomaly'] = (df_pandas['anomaly'] == -1).astype(int)
    
#     # Add fraud_label based on anomaly score and other criteria
#     high_anomaly_threshold = -0.1  
#     moderate_anomaly_threshold = 0.0  
#     low_anomaly_threshold = 0.1 
#     verylow_anomaly_threshold = 0.2  
    
#     # df_pandas['rejected'] = df_pandas['motif_rejet'].apply(lambda x: 0 if x == "Not-rejected" else 1)
 
    
#     def label_fraud(row):
#         if (row['rejected'] == 1 and row['anomaly_score'] <= moderate_anomaly_threshold) or \
#            (row['rejected'] == 0 and row['anomaly_score'] <= moderate_anomaly_threshold) or \
#            (row['anomaly_score'] <= high_anomaly_threshold):
#             return "Fraud"
#         elif (row['rejected'] == 1 and moderate_anomaly_threshold < row['anomaly_score'] < verylow_anomaly_threshold) or \
#              (row['rejected'] == 0 and moderate_anomaly_threshold < row['anomaly_score'] < low_anomaly_threshold):
#             return "Suspicious"
#         elif row['anomaly_score'] >= verylow_anomaly_threshold or \
#              (row['rejected'] == 0 and row['anomaly_score'] >= low_anomaly_threshold):
#             return "Not Fraud"
#         else:
#             return "Suspicious"

#     df_pandas['fraud_label'] = df_pandas.apply(label_fraud, axis=1)
#     #transform fraud_label to binary to 0,1,2
#     df_pandas['fraud_label'] = df_pandas['fraud_label'].apply(lambda x: 0 if x == "Not Fraud" else 1 if x == "Suspicious" else 2)
    
#     return df_pandas

# Apply create_labels function
df_pandas = create_labels(df_pandas, n_estimators=200, contamination=0.01)


# Step 6: Select specific columns
selected_columns = [
    'ID', 'NO_DOSSIER_NAT', 'NUM_ENR', 'WeightedQuantityDeviation',
    'PrescriptionCost_QuantityInteraction', 'CostAnomaly', 'QUANTITE_MED',
    'TotalMedicationsPerMonth', 'DaysBetweenPrescriptions',
    'DaysBetweenLastPrescriptionforSameMedic', 'TotalCostPerMonth',
    'TotalPrescriptionsPerMonth', 'WeightedAvgQuantity', 'CENTRE',
    'PRIX_PPA', 'TARIF', 'TRANCHE_AGE_BENEF', 'rejected', 'Month',
    'trimester', 'fraud_label', 'TARIF_QUANTITE', 'PRIX_CENTRE', 
    'TARIF_SQUARE', 'QUANTITE_SQUARE', 'tarif_median_by_centre',
    'tarif_min_by_centre', 'tarif_max_by_centre'
]

df_selected = df_pandas[selected_columns]

# Step 7: Separate features and labels
X = df_selected.drop(columns=['ID', 'NO_DOSSIER_NAT', 'NUM_ENR', 'fraud_label'])
y = df_selected['fraud_label']

# Step 8: Apply RobustScaler
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

# Step 9: Best parameters for XGBoost
best_params = {
    'subsample': 1.0, 'reg_lambda': 0, 'reg_alpha': 0, 
    'n_estimators': 300, 'max_depth': 7, 
    'learning_rate': 0.2, 'gamma': 0, 
    'colsample_bytree': 0.8
}

# Step 10: Train XGBoost model
xgb_model = xgb.XGBClassifier(**best_params)
xgb_model.fit(X_scaled, y)
print("Model training completed.")

# Step 11: Predict with XGBoost model
df_pandas['predictions'] = xgb_model.predict(X_scaled)
df_pandas['predictions'] = df_pandas['predictions'].apply(lambda x: "Not Fraud" if x == 0 else "Suspicious" if x == 1 else "Fraud")
#save df_pandas to csv
df_pandas.to_csv(r'C:\Users\akila\BIG DATA M1\PFE\Model\data\predictions.csv', index=False)
# Step 12: Save the model
joblib.dump(scaler, 'robustScaler.pkl')
joblib.dump(xgb_model, 'xgboost_model.pkl')
print("Model saved as xgboost_model.pkl.")

# Show final DataFrame
print(df_pandas.head())

spark.stop()