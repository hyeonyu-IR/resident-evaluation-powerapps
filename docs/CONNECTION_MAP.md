# Connection Map

## SharePoint data sources

- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

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

## Dummy import compatibility

The dummy CSV files in `sharepoint-templates/` are intentionally compatible with the app:
- `VIR_RealTime_FeedBack.dummy.csv` uses attending names/emails from `AttendingList.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv` uses resident year/name pairs from `Resident_Year_Name_01.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv` uses procedure main/subcategory pairs from `Procedure_Categories_01.dummy.csv`
