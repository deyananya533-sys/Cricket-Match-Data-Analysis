# Cricket Match Data Analysis

**Student:** Ananya Dey  
**Programme:** MCA  
**Student ID:** BWU/MCA/25/050

## Project files
- `data/Batting.csv` — supplied batting dataset (745 records).
- `data/Bowling_Tab_Screenshot.jpg` — screenshot supplied for the Bowling worksheet. It is included as source material; it is not a complete machine-readable bowling export.
- `src/analysis.py` — Python source code for the batting and match-result analysis.
- `outputs/Cricket_Match_Data_Analysis_Final.pptx` — final presentation.

## Questions covered
The script calculates Q1–Q6 and Q8–Q9 from the supplied batting CSV. The presentation includes a limited bowling analysis for Q7 based on readable rows from the screenshot. Q10 explains a proposed all-rounder impact formula, but does not claim a complete ranking because full bowling and TeamBat data were not supplied.

## Custom Player Performance Score
`0.4 × Runs + 0.2 × Strike Rate + 2 × Fours + 3 × Sixes + 0.1 × Balls Faced`

This is a custom project metric, not an official cricket rating.

## Run the code
Install Python 3, then run:

```bash
pip install -r requirements.txt
python src/analysis.py
```

Question-wise result CSV files will be generated in `outputs/`.

## Data limitation
The Bowling screenshot is only a visible partial table. For a complete Q7 and a reliable top-10 all-rounder ranking for Q10, export the full Bowling and TeamBat worksheets from the original Excel workbook.
