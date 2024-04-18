#authentication code for Mehari choornum
import pandas as pd

observations = {
  "Parameters": ["Total Ash (%) ","Acid-insoluble Ash (%) ", "Water soluble, (%) ", "Loss on drying",
                   "Bulk Density (%)", "pH value"],
    "Obtained Observation": [5.14, 3.12, 2.11, 6.33, 0.48, 6.00]
}
df = pd.DataFrame(observations)

specifications = {
   "Parameters": ["Total Ash (%) ","Acid-insoluble Ash (%) ", "Water soluble, (%) ", "Loss on drying",
                   "Bulk Density (%)", "pH value"],
    "Minimum": [4, 0, 1, 3, 0.4, 2.5],
    "Maximum": [15, 5, 10, 10, 0.8, 8.00]
}
spec_df = pd.DataFrame(specifications)

try:
  merged_df = pd.merge(df, spec_df, on="Parameters")
  merged_df["Within Range"] = (merged_df["Obtained Observation"] >= merged_df["Minimum"]) & (merged_df["Obtained Observation"] <= merged_df["Maximum"])

  if all(merged_df["Within Range"]):
      print("Mehari choornum is within the acceptable specifications.")
  else:
      print("WARNING: Mehari choornum is OUTSIDE specifications for some parameters. See details in the DataFrame.")
  print(merged_df)
except Exception as e:
  print(f"Error: An error occurred during processing. {e}")
