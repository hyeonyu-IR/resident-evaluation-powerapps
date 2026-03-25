# Comprehensive Manual

This manual is intended to be a detailed step-by-step reference for institutions that want to evaluate, implement, and maintain this Power Apps resident-evaluation app.

For a shorter starting point, see:
- [`START_HERE.md`](START_HERE.md)

For the manual SharePoint schema lesson, see:
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

For a slide-based visual walkthrough, see:
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## 1. What This Repository Provides

This repository includes:
- an importable Power Apps canvas app package in `../app/releases`
- SharePoint CSV starter/reference files in `../sharepoint-templates`
- setup and reconnection instructions
- a visual user guide with screenshots
- troubleshooting and implementation checklists

The recommended adoption model is now:
1. create the required SharePoint lists
2. manually create the schema for `VIR_RealTime_FeedBack`
3. manually create the schema for `AttendingList`
4. manually create or preserve `Procedure_Categories_01`
5. import dummy CSV only for the resident reference list
6. download and import the latest `.msapp`
7. reconnect the app in Power Apps Studio when Power Apps prompts for SharePoint and Outlook connections
8. run the smoke tests before production use

For the simplest starting path, use the files in [`../download-files`](../download-files).

## 2. Intended Audience

This manual is for:
- program directors
- division chiefs
- Power Apps administrators
- SharePoint site owners
- local maintainers supporting the app after import

## 3. Microsoft 365 Requirements

Required services:
- Power Apps
- SharePoint Online
- Office 365 Outlook connector

Required permissions:
- ability to import a canvas app
- ability to create or modify SharePoint lists
- ability to reconnect data sources in Power Apps Studio

## 4. Files You Should Use

Primary implementation file:
- [`../app/releases/UNC_VIR_Resident_Evaluation.msapp`](../app/releases/UNC_VIR_Resident_Evaluation.msapp)

Import this directly:
- [`../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv`](../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv)

Use these as reference/sample data only after manual list creation:
- [`../sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv`](../sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv)
- [`../sharepoint-templates/dummy/AttendingList.dummy.csv`](../sharepoint-templates/dummy/AttendingList.dummy.csv)
- [`../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv`](../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv)

## 5. Expected SharePoint List Names

Create these lists with these exact names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

Important:
- the CSV filename is not the same thing as the SharePoint list name
- the SharePoint list names used by the app should match these expected names
- the SharePoint column names should also match expected app field names
- the SharePoint internal field names matter too

If your institution uses different list names, the app may still be adoptable, but you should expect data-source remapping and possibly formula updates.

## 6. Why Manual Schema Creation Matters

This section reflects a hard-earned lesson from external testing.

Two major problems were observed when the main feedback and attending lists were created directly from CSV:

1. SharePoint created wrong internal field names.
   - Example: a visible `ResidentYear` column could internally become `field_4`.
   - Power Apps binds to the internal field names, not just visible titles.

2. SharePoint inferred wrong field types.
   - `AttendingEmail` or `EmailAddress` could become `Person or Group`.
   - This app expects both of those as `Single line of text`.

The result could be:
- blank or partially blank records
- broken ownership filtering
- confusing behavior where records are created but most values do not save

## 7. Step-by-Step Implementation

### Step 1. Review the expected schema

Before importing anything, read:
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

Pay special attention to:
- `AttendingEmail`
- `EmailAddress`
- `AttendingRole`
- `ResidentYear`
- `ResidentName`
- `ProcedureMain`
- `ProcedureSub`
- `EvalDate`

### Step 2. Create SharePoint lists

Create the four expected lists with the exact names listed above.

Then manually create the schema for:
- `VIR_RealTime_FeedBack`
- `AttendingList`

Use:
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

### Step 3. Import starter data

Recommended for initial evaluation:
- import the resident dummy CSV for:
  - `Resident_Year_Name_01`

Use the dummy attending, feedback, and procedure CSV files only as reference/sample data after the lists already exist with the correct schema.

### Step 4. Verify key SharePoint column types

Review these fields after list creation:
- `AttendingEmail` should be `Single line of text`
- `EmailAddress` should be `Single line of text`
- `EvalDate` should be `Date and Time`
- `Comment` should be `Multiple lines of text`
- `Eval_Serial_No` should be `Number`

### Step 5. Import the app

1. Open `make.powerapps.com`
2. Go to `Apps`
3. Choose `Import canvas app`
4. Select the latest `.msapp`
5. Open the imported app only after the four required SharePoint lists have already been created

Important:
- on first open, Power Apps will prompt you to connect SharePoint and Office 365 Outlook
- this works best after the required SharePoint lists already exist with the expected names and columns

### Step 6. Reconnect data sources

Reconnect:
- SharePoint lists
- Office 365 Outlook

Recommended reconnect workflow:
1. open the imported app in Power Apps Studio
2. expect Power Apps to prompt for SharePoint and Office 365 Outlook connections on first open
3. go to `Data`
4. remove broken or unresolved SharePoint connections if present
5. add the four expected SharePoint lists
6. confirm formulas resolve without data-source errors

### Step 7. Run smoke tests

Perform these checks:
1. create a new evaluation
2. confirm `AttendingEmail` is populated
3. confirm the main record saves with real values, not an empty row
4. confirm `My Feedback List` only shows the current user's records
5. confirm `My Feedback Report` only uses the current user's records
6. confirm PD/admin-only screens are restricted correctly
7. confirm procedure category filtering works
8. confirm resident year and resident name filtering works
9. confirm report generation and email flow work
10. confirm the stats chart labels are still correct after reconnect:
   - `ccAttendingFeedbackNo.Items.Labels = Attending`
   - `ccProcedurePct.Items.Labels = ProcedureMain`

## 8. Key Functional Design Assumptions

The app currently assumes:
- ownership logic uses `AttendingEmail`
- PD/admin access is controlled by `AttendingRole`
- procedure filtering uses the original main/subcategory structure
- the app currently uses `Procedure_Categories_01.Title` as the main procedure category field

If any of those assumptions change locally, formula updates may be needed.

## 9. Common Failure Modes

Typical causes of implementation problems:
- SharePoint list names do not match expected app data sources
- internal field names differ from expected app field names
- `AttendingEmail` is missing, blank, or the wrong type
- `EmailAddress` is the wrong type
- procedure category structure was changed
- local `AttendingRole` values do not match expected role names
- data sources were not reconnected after import

For detailed troubleshooting:
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

## 10. Recommended Go-Live Checklist

Before production use:
- replace dummy attending data with local attending data
- replace dummy resident data with local resident data
- re-run smoke tests using local accounts
- confirm who owns ongoing app maintenance
- document who will maintain the SharePoint lists and role mappings

## 11. Questions That May Still Require Local Review

If the repository is working as intended, most institutions should be able to self-serve using:
- the `.msapp`
- the schema guide
- the setup and troubleshooting docs
- the visual user guide

The most common institution-specific decisions still remaining are:
- local role naming
- local SharePoint governance constraints
- whether to keep text email fields or intentionally redesign the app around Person columns
- whether local programs want custom procedure categories or evaluation fields

## 12. Distribution Recommendation

Use the GitHub repository as the main distribution point.

That is preferable to emailing attachments because:
- the latest version lives in one place
- setup instructions and screenshots are alongside the files
- institutions can download exactly what they need
- version history is visible
- you avoid repeatedly redistributing stale exports

## 13. Related Documents

- [`START_HERE.md`](START_HERE.md)
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)
- [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
- [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md)
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- [`USER_GUIDE.md`](USER_GUIDE.md)
