from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA / "Batting.csv")
for col in ["R", "B", "4s", "6s", "Chase", "Win"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

players = df.groupby("Player").agg(
    Runs=("R", "sum"), Balls=("B", "sum"),
    Fours=("4s", "sum"), Sixes=("6s", "sum"),
    Innings=("R", "size")
)
players["StrikeRate"] = players["Runs"].div(players["Balls"].replace(0, pd.NA)) * 100
players["BoundaryRuns"] = players["Fours"] * 4 + players["Sixes"] * 6
players["PerformanceScore"] = (
    0.4 * players["Runs"] + 0.2 * players["StrikeRate"].fillna(0)
    + 2 * players["Fours"] + 3 * players["Sixes"] + 0.1 * players["Balls"]
)

players.sort_values("Runs", ascending=False).head(10).to_csv(OUT / "Q1_Top_10_Batsmen.csv")
players[players["Balls"] >= 50].sort_values("StrikeRate", ascending=False).head(10).to_csv(OUT / "Q2_Top_Strike_Rates.csv")
players.sort_values("Fours", ascending=False).head(1).to_csv(OUT / "Q3_Most_Fours.csv")
players.sort_values("Sixes", ascending=False).head(1).to_csv(OUT / "Q3_Most_Sixes.csv")

matches = df[["Date", "Team", "Vs", "Win"]].drop_duplicates()
matches.groupby("Team")["Win"].sum().sort_values(ascending=False).to_csv(OUT / "Q4_Team_Wins.csv")

df["Fixture"] = df.apply(
    lambda r: (str(r["Date"]),) + tuple(sorted([str(r["Team"]), str(r["Vs"])])), axis=1
)
idx = df.groupby("Fixture")["R"].idxmax()
df.loc[idx, ["Date", "Player", "Team", "Vs", "R"]].to_csv(OUT / "Q5_Match_Highest_Scorers.csv", index=False)

innings = df.groupby(["Date", "Team", "Vs"], as_index=False).agg(
    InningsRuns=("R", "sum"), Chase=("Chase", "first"),
    Win=("Win", "first")
)
innings.groupby("Chase").agg(
    Innings=("Team", "size"), AverageRuns=("InningsRuns", "mean"),
    Wins=("Win", "sum"), WinRate=("Win", "mean")
).to_csv(OUT / "Q6_Batting_First_vs_Chasing.csv")

players.sort_values("BoundaryRuns", ascending=False).head(10).to_csv(OUT / "Q8_Boundary_Run_Leaders.csv")
players.sort_values("PerformanceScore", ascending=False).head(20).to_csv(OUT / "Q9_Top_20_Performance_Score.csv")

print("Analysis complete. Question-wise CSV outputs are in the outputs folder.")
print("Q7 uses only the visible Bowling screenshot sample in the presentation.")
print("Q10 cannot be fully ranked without complete bowling and TeamBat datasets.")
