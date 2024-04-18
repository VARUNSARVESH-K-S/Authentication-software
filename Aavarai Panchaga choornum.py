#authentication code for Aavarai Panchaga choornam
import pandas as pd
observations = {
  "Parameters": ["Loss of drying at 110℃ ","Total ash (%) ", "Acid insoluble ash (%) ", "Water soluble ash (%)",
                   "Water soluble extractive", "pH value"],
    "Obtained Observation": [1.50, 11.3, 1.50, 9.80, 9.80, 7.50]
}
df = pd.DataFrame(observations)

specifications = {
   "Parameters": ["Loss of drying at 110℃ ","Total ash (%) ", "Acid insoluble ash (%) ", "Water soluble ash (%)",
                   "Water soluble extractive", "pH value"],
    "Minimum": [3, 4, 0, 1, 20, 2.5],
    "Maximum": [10, 15, 5, 10, 30, 8.00]
}
spec_df = pd.DataFrame(specifications)

try:
  merged_df = pd.merge(df, spec_df, on="Parameters")
  merged_df["Within Range"] = (merged_df["Obtained Observation"] >= merged_df["Minimum"]) & (merged_df["Obtained Observation"] <= merged_df["Maximum"])

  if all(merged_df["Within Range"]):
      print("Aavarai Panchaga choornam is within the acceptable specifications.")
  else:
      print("WARNING: Aavarai Panchaga choornam is OUTSIDE specifications for some parameters. See details in the DataFrame.")
  print(merged_df)
except Exception as e:
  print(f"Error: An error occurred during processing. {e}")
