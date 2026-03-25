# Setup Guide

See also:
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

## 1. Create SharePoint lists

Create these lists in the target tenant:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

These SharePoint list names should match exactly.

Important:
- the SharePoint list name does need to match the expected app data source name
- the SharePoint column names also need to match the expected field names in the app
- the internal SharePoint field names matter, not just the visible display titles
- create column names exactly as documented, including capitalization, spelling, and underscores
- for setup purposes, treat the documented column names as case-sensitive

## 2. Use manual schema for the two critical lists

Manually create these two lists first:
- `VIR_RealTime_FeedBack`
- `AttendingList`

Do not let CSV import define those schemas.

Why:
- SharePoint can create wrong internal names such as `field_4`
- Power Apps binds to internal field names
- SharePoint can infer email columns as `Person or Group`

Practical caution:
- list reads may appear to work when display names and field types look correct
- form submission can still fail unless the underlying SharePoint field identities also match the app's expected bindings

Critical email-field rules:
- `AttendingEmail` in `VIR_RealTime_FeedBack` must be `Single line of text`
- `EmailAddress` in `AttendingList` must be `Single line of text`

Use:
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

## 3. Seed the reference lists from CSV

Only this list is still recommended for direct dummy CSV import:
- `Resident_Year_Name_01`

Recommended file:
- [`../download-files/Resident_Year_Name_01.dummy.csv`](../download-files/Resident_Year_Name_01.dummy.csv)

Use this file to generate `Procedure_Categories_01` with the preserved original taxonomy:
- [`../download-files/Procedure_Categories_01.dummy.csv`](../download-files/Procedure_Categories_01.dummy.csv)

## 4. Import the app

1. Open `make.powerapps.com`
2. Go to `Apps`
3. Choose `Import canvas app`
4. Select the latest `.msapp` from [`../app/releases`](../app/releases)
5. Open the imported app only after the four SharePoint lists above have already been created

## 5. Reconnect data sources

Reconnect:
- SharePoint lists
- Office 365 Outlook

Recommended reconnect process:
1. Open the imported app in Power Apps Studio
2. Expect Power Apps to prompt for SharePoint and Office 365 Outlook connections on first open
3. Go to `Data`
4. Remove broken or unresolved SharePoint connections if present
5. Add the four SharePoint lists with the exact names listed above
6. Confirm formulas resolve without data-source errors

If the target institution used different SharePoint list names, they should expect to:
- remove the old data source references
- add the replacement list
- update formulas if Power Apps does not automatically rebind them cleanly

## 6. Smoke tests

1. Create a new evaluation
2. Confirm `AttendingEmail` is populated
3. Confirm the main feedback record is saved with actual field values, not an empty row
4. Confirm `My Feedback List` only shows the current user's records
5. Confirm PD/admin screens are restricted correctly
6. Confirm report emails send successfully
7. Confirm procedure main-category and subcategory dropdown filtering works correctly
8. Confirm resident year and resident name filtering works correctly
9. Confirm the app can open existing records without schema errors
10. Confirm the stats chart labels are correct after first connect or reconnect. These labels are not hard-coded and can fall back to the default chart fields `Count` and `Metric`:
   - `ccAttendingFeedbackNo.Items.Labels = Attending`
   - `ccProcedurePct.Items.Labels = ProcedureMain`

## 7. Hard-earned lesson

The main external setup failure mode was not the app package itself. It was SharePoint schema creation.

Simple CSV-driven list creation can look correct at first glance and still fail because:
- internal field names do not match the app
- email columns are inferred as the wrong type
- Power Apps forms then create blank or partially blank records

Manual list creation for `VIR_RealTime_FeedBack` and `AttendingList` was the fix that made external testing stable.
