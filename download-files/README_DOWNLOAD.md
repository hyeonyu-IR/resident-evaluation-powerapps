# Download Package

This folder is the easiest starting point for institutions that want to evaluate or implement the app.

Included files:
- `UNC_VIR_Resident_Evaluation.msapp`
- `Resident_Year_Name_01.dummy.csv`
- `Procedure_Categories_01.dummy.csv`

## Recommended use order

1. Create the required SharePoint lists with the exact expected names:
   - `VIR_RealTime_FeedBack`
   - `Procedure_Categories_01`
   - `Resident_Year_Name_01`
   - `AttendingList`
2. Read [`../docs/MANUAL_SHAREPOINT_SCHEMA.md`](../docs/MANUAL_SHAREPOINT_SCHEMA.md).
3. Manually create:
   - `VIR_RealTime_FeedBack`
   - `AttendingList`
4. Create `Procedure_Categories_01` from the preserved original procedure-category CSV.
5. Import only:
   - `Resident_Year_Name_01.dummy.csv`
6. Use `Procedure_Categories_01.dummy.csv` to generate the procedure category list.
7. Only after those lists exist, import `UNC_VIR_Resident_Evaluation.msapp` into Power Apps.
8. Open the app in Power Apps Studio and connect SharePoint and Outlook when prompted.
9. Run the smoke tests in `../docs/IMPLEMENTATION_CHECKLIST.md`.

## Important

- CSV filenames are import helpers only.
- SharePoint list names and column names should match what the app expects.
- SharePoint internal field names matter, not just visible display titles.
- list reads may appear to work when display names and field types look correct
- form submission can still fail unless the underlying SharePoint field identities also match the app's expected bindings
- The included CSV files are the two supported adoption CSVs, not production data.
- `AttendingEmail` must be `Single line of text`.
- `EmailAddress` must be `Single line of text`.
- The stats chart x-axis labels are not hard-coded. On first connect or reconnect, they can revert to the chart defaults `Count` and `Metric`. Verify:
  - `ccAttendingFeedbackNo.Items.Labels = Attending`
  - `ccProcedurePct.Items.Labels = ProcedureMain`
- Power Apps will prompt for SharePoint and Office 365 Outlook connections when the imported app is opened.
- That connection step is much easier if the SharePoint lists have already been created first.

## Why this changed

During external testing, simple CSV-driven SharePoint list creation caused:
- wrong internal field names such as `field_4`
- wrong email field types such as `Person or Group`
- blank or partially blank records even when the app appeared connected

Manual creation of `VIR_RealTime_FeedBack` and `AttendingList` fixed that issue.

For full instructions, use:
- [`../docs/START_HERE.md`](../docs/START_HERE.md)
- [`../docs/MANUAL_SHAREPOINT_SCHEMA.md`](../docs/MANUAL_SHAREPOINT_SCHEMA.md)
- [`../docs/COMPREHENSIVE_MANUAL.md`](../docs/COMPREHENSIVE_MANUAL.md)
