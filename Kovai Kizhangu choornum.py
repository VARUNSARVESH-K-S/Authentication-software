#authentication code for Kovia Kizhangu choornum
import pandas as pd
observations = {
    "Parameters": ["Loss of drying at 105℃ (%) ","Ash value at 550℃ (%) ", "Water soluble, (%) ", "Alkalinity as CaCO3 in water soluble ash, (%)",
                   "Acid insoluble ash, (%)", "pH value "],
    "Obtained Observation": [0.15, 15.39, 8.82, 3.55, 0.25, 6.58]
}
df = pd.DataFrame(observations)
specifications = {
    "Parameters": ["Loss of drying at 105℃ (%) ","Ash value at 550℃ (%) ", "Water soluble, (%) ", "Alkalinity as CaCO3 in water soluble ash, (%)",
                   "Acid insoluble ash, (%)", "pH at value "],
    "Minimum": [3, 4, 1, 1, 0, 2.5],
    "Maximum": [10, 15, 10, 10, 5, 8]
}
spec_df = pd.DataFrame(specifications)

try:
  merged_df = pd.merge(df, spec_df, on="Parameters")
  merged_df["Within Range"] = (merged_df["Obtained Observation"] >= merged_df["Minimum"]) & (merged_df["Obtained Observation"] <= merged_df["Maximum"])
  if all(merged_df["Within Range"]):
      print("Kovia Kizhangu choornum is within the acceptable specifications.")
  else:
      print("WARNING: Kovia Kizhangu choornum is OUTSIDE specifications for some parameters. See details in the DataFrame.")
  print(merged_df)
except Exception as e:
  print(f"Error: An error occurred during processing. {e}")


