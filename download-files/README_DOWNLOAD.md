# Download Package

This folder is the easiest starting point for institutions that want to evaluate or implement the app.

Included files:
- `UNC_VIR_Resident_Evaluation.msapp`
- `AttendingList.dummy.csv`
- `Resident_Year_Name_01.dummy.csv`
- `Procedure_Categories_01.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv`

Recommended use order:
1. Create the required SharePoint lists with the exact expected names:
   - `VIR_RealTime_FeedBack`
   - `Procedure_Categories_01`
   - `Resident_Year_Name_01`
   - `AttendingList`
2. Import the matching CSV files into those lists.
3. Import `UNC_VIR_Resident_Evaluation.msapp` into Power Apps.
4. Reconnect the app to the local SharePoint lists and Outlook connector.
5. Run the smoke tests in `docs/IMPLEMENTATION_CHECKLIST.md`.

Important:
- CSV filenames are import helpers only.
- SharePoint list names and column names should match what the app expects.
- The included CSV files are dummy data for setup and testing, not production data.

For full instructions, use:
- [`docs/START_HERE.md`](../docs/START_HERE.md)
- [`docs/COMPREHENSIVE_MANUAL.md`](../docs/COMPREHENSIVE_MANUAL.md)
