# Comprehensive Manual

This manual is intended to be a detailed step-by-step reference for institutions that want to evaluate, implement, and maintain this Power Apps resident-evaluation app.

For a shorter starting point, see:
- [`START_HERE.md`](START_HERE.md)

For a slide-based visual walkthrough, see:
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## 1. What This Repository Provides

This repository includes:
- an importable Power Apps canvas app package in `app/releases`
- SharePoint CSV starter files in `sharepoint-templates`
- setup and reconnection instructions
- a visual user guide with screenshots
- troubleshooting and implementation checklists

The recommended adoption model is:
1. download the latest `.msapp`
2. create the required SharePoint lists
3. import the recommended CSV starter files
4. reconnect the app in Power Apps Studio
5. run the smoke tests before production use

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

Primary implementation files:
- [`UNC_VIR_Resident_Evaluation.msapp`](../app/releases/UNC_VIR_Resident_Evaluation.msapp)

Recommended SharePoint CSV starter files:
- [`AttendingList.dummy.csv`](../sharepoint-templates/dummy/AttendingList.dummy.csv)
- [`Resident_Year_Name_01.dummy.csv`](../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv)
- [`Procedure_Categories_01.dummy.csv`](../sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv)
- [`VIR_RealTime_FeedBack.dummy.csv`](../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv)

These files reflect the reference implementation used for this app.

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

If your institution uses different list names, the app may still be adoptable, but you should expect data-source remapping and possibly formula updates.

## 6. Step-by-Step Implementation

### Step 1. Review the expected schema

Before importing anything, read:
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)

Pay special attention to:
- `AttendingEmail`
- `AttendingRole`
- `ResidentYear`
- `ResidentName`
- `ProcedureMain`
- `ProcedureSub`
- `EvalDate`

### Step 2. Create SharePoint lists

Create the four expected lists with the exact names listed above.

Recommended pattern:
1. create the list with the exact target name
2. import the corresponding CSV content
3. confirm the resulting column names
4. confirm key column types manually

### Step 3. Import starter data

Recommended for initial evaluation:
- import the `dummy` CSV files

Use `template` files if you want a minimal example row.

Use `blank` files only if you prefer to build all list content yourself.

### Step 4. Verify key SharePoint column types

Review these fields after import:
- `EvalDate` should be date/time
- score fields should be numeric if you want numeric sorting and calculations
- comment fields should allow sufficient text
- `AttendingEmail` should remain a single-line text field unless you intentionally refactor the app to use a Person column

### Step 5. Import the app

1. Open `make.powerapps.com`
2. Go to `Apps`
3. Choose `Import canvas app`
4. Select the latest `.msapp`

### Step 6. Reconnect data sources

Reconnect:
- SharePoint lists
- Office 365 Outlook

Recommended reconnect workflow:
1. open the imported app in Power Apps Studio
2. go to `Data`
3. remove broken or unresolved SharePoint connections if present
4. add the four expected SharePoint lists
5. confirm formulas resolve without data-source errors

### Step 7. Run smoke tests

Perform these checks:
1. create a new evaluation
2. confirm `AttendingEmail` is populated
3. confirm `My Feedback List` only shows the current user's records
4. confirm `My Feedback Report` only uses the current user's records
5. confirm PD/admin-only screens are restricted correctly
6. confirm procedure category filtering works
7. confirm resident year and resident name filtering works
8. confirm report generation and email flow work

## 7. Key Functional Design Assumptions

The app currently assumes:
- ownership logic uses `AttendingEmail`
- PD/admin access is controlled by `AttendingRole`
- procedure filtering uses the original main/subcategory structure
- the app currently uses `Procedure_Categories_01.Title` as the main procedure category field

If any of those assumptions change locally, formula updates may be needed.

## 8. User Workflow Overview

Main user workflows:
- create feedback
- review personal feedback history
- inspect and edit feedback details
- generate personal summary reports
- review stats
- use PD/admin all-attending reports

For screenshots and workflow visuals, see:
- [`USER_GUIDE.md`](USER_GUIDE.md)

## 9. Common Failure Modes

Typical causes of implementation problems:
- SharePoint list names do not match expected app data sources
- imported column names differ from expected field names
- `AttendingEmail` is missing or blank
- procedure category structure was changed
- local `AttendingRole` values do not match expected role names
- data sources were not reconnected after import

For detailed troubleshooting:
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

## 10. Recommended Go-Live Checklist

Before production use:
- replace dummy attending data with local attending data
- replace dummy resident data with local resident data
- remove dummy evaluation rows if they were used only for testing
- re-run smoke tests using local accounts
- confirm who owns ongoing app maintenance
- document who will maintain the SharePoint lists and role mappings

## 11. Questions That May Still Require Local Review

If the repository is working as intended, most institutions should be able to self-serve using:
- the `.msapp`
- the CSV templates
- the setup and troubleshooting docs
- the visual user guide

The most common institution-specific decisions still remaining are:
- local role naming
- local SharePoint governance constraints
- whether to keep `AttendingEmail` as text or convert it to a Person column
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
- [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
- [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md)
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- [`USER_GUIDE.md`](USER_GUIDE.md)
