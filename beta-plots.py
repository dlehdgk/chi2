import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Get the list of all files matching the pattern
file_list = sorted(glob.glob("./beta/*-beta.1.txt"))

# Prepare a list to hold each file's data as a dict
data_rows = []

for fpath in file_list:
    # 2. Extract the <b> value from the filename, e.g. "0.05" from "0.05-beta.1.txt"
    filename = os.path.basename(fpath)
    # Remove the suffix '-beta.1.txt'
    b_str = filename.replace("-beta.1.txt", "")
    # Convert to float, if desired
    b_val = float(b_str)

    # 3. Read the file lines
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]  # strip out empty lines
        # The first line (header) may begin with a '#'
        header_line = lines[0].lstrip("#").split()
        # The second line has the numeric values
        values_line = lines[1].split()

    # Zip header + values into a dictionary
    row_dict = dict(zip(header_line, values_line))
    # Add the beta value as a separate column
    row_dict["beta"] = b_val

    # Add this row to the list
    data_rows.append(row_dict)

# 4. Create a Pandas DataFrame
df = pd.DataFrame(data_rows)

# Optionally, attempt to convert all columns to numeric when possible
df = df.apply(pd.to_numeric, errors="ignore")

# chi2_df = df[["chi2", "beta"]]
chi2_df = df[(df["beta"] < 0.0015) & (df["beta"] > 0.0005)]

print(chi2_df)

sns.lmplot(x="beta", y="chi2", data=chi2_df, fit_reg=True)
plt.savefig("beta/output/chi2.png", dpi=300)
