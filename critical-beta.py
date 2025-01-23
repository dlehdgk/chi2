import matplotlib.pyplot as plt
import glob
import os
import pandas as pd
import numpy as np

log_num = np.array([0.05, 0.001])

data_rows = []
for i in log_num:
    file_list = sorted(glob.glob(f"./beta/*-at{i}log.1.txt"))

    for fpath in file_list:
        filename = os.path.basename(fpath)
        b_str = filename.replace(f"-at{i}log.1.txt", "")
        b_val = float(b_str)

        with open(fpath, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            header_line = lines[0].lstrip("#").split()
            values_line = lines[1].split()

        row_dict = dict(zip(header_line, values_line))
        row_dict["beta"] = b_val
        row_dict["beta_log"] = i

        data_rows.append(row_dict)

df = pd.DataFrame(data_rows)
df = df.apply(pd.to_numeric, errors="ignore")

df_0 = df[(df["beta_log"] == 0.05) & (df["beta"] < 0.1)]
df_1 = df[(df["beta_log"] == 0.001) & (df["beta"] < 0.1)]

fig, ax = plt.subplots()
ax.scatter(
    df_0["beta"],
    df_0["chi2"],
    color="red",
    marker=",",
    alpha=0.5,
    label="$\\beta_{crit} = 0.05$",
)
ax.scatter(
    df_1["beta"],
    df_1["chi2"],
    color="blue",
    marker="x",
    alpha=0.5,
    label="$\\beta_{crit} = 0.001$",
)
ax.set_xlabel("$\\beta$")
ax.set_ylabel("$\\chi^2$")
ax.legend()
ax.grid()
plt.savefig("beta/output/comparison.png", dpi=300)
