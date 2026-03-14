# Setup Guide

See also:
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)

## 1. Create SharePoint lists

Create these lists in the target tenant:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

These SharePoint list names should match exactly. Power Apps connects to list names, not to CSV filenames.

Important:
- the CSV filename does not need to match the target list name exactly
- the SharePoint list name does need to match the expected app data source name
- the SharePoint column names also need to match the expected field names in the app
- if a target institution creates differently named lists, they must reconnect those data sources in Power Apps and may still need formula updates

Use the CSV files in [`sharepoint-templates`](../sharepoint-templates).

Recommended import choice:
- use files in [`sharepoint-templates/dummy`](../sharepoint-templates/dummy) for a realistic, non-sensitive starter dataset
- use files in [`sharepoint-templates/template`](../sharepoint-templates/template) for a minimal example row
- use files in [`sharepoint-templates/blank`](../sharepoint-templates/blank) only if the target team prefers to build the content from scratch after list creation

The files in [`sharepoint-templates/dummy`](../sharepoint-templates/dummy) are aligned with each other:
- feedback rows match the dummy attending list
- feedback rows match the dummy resident/year list
- feedback rows use procedure pairs that match the preserved original procedure category list

Recommended list creation pattern:
1. Create the SharePoint list with the exact target name first
2. Import the matching CSV content into that list
3. Confirm the imported column names are correct
4. Reconnect the app to that list inside Power Apps

Example:
- file: `dummy/AttendingList.dummy.csv`
- target SharePoint list name: `AttendingList`

Do not leave the SharePoint list named something like `AttendingList_dummy` unless you are prepared to remap the app manually.

## 2. Seed reference data

Minimum data required:
- Attendings with email and role
- Resident year/name rows
- Procedure categories and subcategories

If the target institution wants the fastest working setup, import:
- `dummy/AttendingList.dummy.csv`
- `dummy/Resident_Year_Name_01.dummy.csv`
- `dummy/Procedure_Categories_01.dummy.csv`
- `dummy/VIR_RealTime_FeedBack.dummy.csv`

After import, review SharePoint column types manually. CSV-based SharePoint creation can infer incorrect types for some fields.

Fields worth checking explicitly:
- `EvalDate` should be date/time
- score fields should be numeric if the local implementation expects numeric sorting or calculations
- long free-text comment fields should allow enough text length
- `AttendingEmail` should remain a single-line text field unless the app is intentionally changed to use a Person column

## 3. Import the app

1. Open `make.powerapps.com`
2. Go to `Apps`
3. Choose `Import canvas app`
4. Select the latest `.msapp` from [`app/releases`](../app/releases)

## 4. Reconnect data sources

Reconnect:
- SharePoint lists
- Office 365 Outlook

Recommended reconnect process:
1. Open the imported app in Power Apps Studio
2. Go to `Data`
3. Remove broken or unresolved SharePoint connections if present
4. Add the four SharePoint lists with the exact names listed above
5. Confirm formulas resolve without data-source errors

If the target institution used different SharePoint list names, they should expect to:
- remove the old data source references
- add the replacement list
- update formulas if Power Apps does not automatically rebind them cleanly

## 5. Smoke tests

1. Create a new evaluation
2. Confirm `AttendingEmail` is populated
3. Confirm `My Feedback List` only shows the current user's records
4. Confirm PD/admin screens are restricted correctly
5. Confirm report emails send successfully
6. Confirm procedure main-category and subcategory dropdown filtering works correctly
7. Confirm resident year and resident name filtering works correctly
8. Confirm the app can open existing imported dummy feedback rows without schema errors
