from collections import Counter
import os
import re
from pathlib import Path
import pandas as pd
levels = Counter()
#======yahan se path badla hai==============
Desktop_path  = Path(r"\\nas.vcl\redirect$\yoginder.chauhan\Desktop")
LOG_FILE = Desktop_path / "logtest.txt"
OUT_FILE = Desktop_path / "log_report.csv"
rows= []
with open(LOG_FILE,"r",encoding = "utf-8",errors = "ignore" ) as f:
    for line in f:
        m = re.match(r"(\S+ \S+) (\w+)\s+(.*)",line)
        if m:
            time,level,message = m.groups()
            rows.append({"time": time, "level": level, "message": message})
df = pd.DataFrame(rows)
df["time"] = pd.to_datetime(df["time"])
problems  = df[df["level"].isin(["ERROR", "FAIL","WAR"])]
problems.to_csv(OUT_FILE, index=False)
counts  = df["level"].value_counts()
print(f"Most frequent level : {counts.idxmax()}({counts.max()} times )")
# Ye line terminal mein file ka EXACT address print karegi
print(f" File exactly yahan save hui: {OUT_FILE.resolve()}")