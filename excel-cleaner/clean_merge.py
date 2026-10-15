"""Merges every Excel file in input/, standardises column names, names,
emails, amounts and dates, removes duplicates, and writes a summary report."""
import glob, re, pandas as pd

def load():
    frames = []
    for f in glob.glob("input/*.xlsx"):
        df = pd.read_excel(f)
        df.columns = [c.strip().lower() for c in df.columns]
        df["source"] = f.split("/")[-1]
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

def clean(df):
    df = df.dropna(subset=["customer name"]).copy()
    df["customer name"] = df["customer name"].str.strip().str.title()
    df["email"] = df["email"].str.strip().str.lower()
    df["amount"] = df["amount"].astype(str).map(lambda s: float(re.sub(r"[^\d.]", "", s)))
    def parse_date(s):
        s = str(s).strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}", s):  # ISO dates: year first
            return pd.to_datetime(s[:10]).date()
        return pd.to_datetime(s, dayfirst=True).date()  # Malaysian day/month style
    df["date"] = df["date"].map(parse_date)
    return df.drop_duplicates(subset=["email", "amount"])

if __name__ == "__main__":
    raw = load(); df = clean(raw)
    with pd.ExcelWriter("cleaned_report.xlsx") as w:
        df.to_excel(w, sheet_name="Clean Data", index=False)
        df.groupby("customer name")["amount"].sum().reset_index().to_excel(w, sheet_name="Totals", index=False)
    print(f"{len(raw)} rows in, {len(df)} clean rows out")
    print(df.to_string(index=False))
