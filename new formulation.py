#authentication code for The New Formulation
import pandas as pd

observations = {
  "Parameters": ["Total Ash (%)", "Water Soluble Ash (WSA) (%)", "Acid Insoluble Ash (AIA) (%)",
                  "pH (%)", "Bulk Density (g/ml)", "Granulometry (%)",
                  "Moisture Loss on Drying (LOD) (%)", "Water Soluble Extract (WSE) (%)",
                  "Alcohol Soluble Extract (ASE) (%)"],
  "Obtained Observation": [7.11, 1.58, 0.39, 5.67, 0.68, 91.21, 3.4, 23.148, 16.67]
}
df = pd.DataFrame(observations)

specifications = {
  "Parameters": ["Total Ash (%)", "Water Soluble Ash (WSA) (%)", "Acid Insoluble Ash (AIA) (%)",
                  "pH (%)", "Bulk Density (g/ml)", "Granulometry (%)",
                  "Moisture Loss on Drying (LOD) (%)", "Water Soluble Extract (WSE) (%)",
                  "Alcohol Soluble Extract (ASE) (%)"],
  "Minimum": [4, 1, 0, 2.5, 0.4, 80, 3, 20, 15],
  "Maximum": [15, 10, 5, 8, 0.8, 100, 10, 30, 30]
}
spec_df = pd.DataFrame(specifications)

try:
  merged_df = pd.merge(df, spec_df, on="Parameters")
  merged_df["Within Range"] = (merged_df["Obtained Observation"] >= merged_df["Minimum"]) & (merged_df["Obtained Observation"] <= merged_df["Maximum"])
  if all(merged_df["Within Range"]):
      print("The New formulation is within the acceptable specifications.")
  else:
      print("WARNING: The New formulation is OUTSIDE specifications for some parameters. See details in the DataFrame.")
  print(merged_df)
except Exception as e:
  print(f"Error: An error occurred during processing. {e}")


