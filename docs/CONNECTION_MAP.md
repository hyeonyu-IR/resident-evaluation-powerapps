# Connection Map

## SharePoint data sources

- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

These are the expected SharePoint list names in Power Apps. They should be created with these exact names whenever possible.

Important distinction:
- CSV filenames are only import helpers
- SharePoint list names are the actual app connection targets
- if list names differ, reconnecting may not be enough and some formulas may require manual updates

## Outlook connector

- `Office365`

## Critical fields

### `VIR_RealTime_FeedBack`
- `Attending`
- `AttendingEmail`
- `ResidentYear`
- `ResidentName`
- `ProcedureMain`
- `ProcedureSub`
- `EvalDate`
- `AverageScore`
- `Comment`
- `Non_Preoperative`
- `Intraoperative`
- `Postoperative`

### `AttendingList`
- `AttendingName`
- `EmailAddress`
- `AttendingRole`

Field names should also match exactly where possible. The current app formulas assume these names directly.

Leadership roles recognized by formulas:
- `program director`
- `pd`
- `program dir`
- `chair`
- `division chief`
- `admin`
- `administrator`

## Schema caveat

The procedure category formulas currently use `Procedure_Categories_01.Title` as the main category field. If a target institution uses another field name such as `MainCategory`, update the formulas after import.

Similarly, the ownership and report logic assumes:
- `VIR_RealTime_FeedBack.AttendingEmail`
- `VIR_RealTime_FeedBack.ResidentYear`
- `VIR_RealTime_FeedBack.ResidentName`
- `VIR_RealTime_FeedBack.ProcedureMain`
- `VIR_RealTime_FeedBack.ProcedureSub`

Changing those field names without updating the app will break filtering and report behavior.

## Dummy import compatibility

The dummy CSV files in `sharepoint-templates/dummy/` are intentionally compatible with the app:
- `VIR_RealTime_FeedBack.dummy.csv` uses attending names/emails from `AttendingList.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv` uses resident year/name pairs from `Resident_Year_Name_01.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv` uses procedure main/subcategory pairs from `Procedure_Categories_01.dummy.csv`
