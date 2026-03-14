# Troubleshooting

## App Cannot Find SharePoint Data

Likely causes:
- SharePoint list names do not match the expected names
- data sources were not reconnected after import
- the app is still pointing to the original tenant's connections

Check:
1. confirm the SharePoint list names exactly match the expected names
2. open the app in Power Apps Studio
3. remove broken SharePoint data sources
4. reconnect the local SharePoint lists

## "My Feedback" Shows Wrong Records

Likely causes:
- `AttendingEmail` is missing or blank on old rows
- the local app was modified to use `Attending` instead of `AttendingEmail`

Check:
1. create a new row and confirm `AttendingEmail` saves correctly
2. inspect old rows and backfill `AttendingEmail` if needed
3. verify formulas still use email-based filtering

## Procedure Filtering Does Not Work

Likely causes:
- the procedure category list was renamed
- the main category field is not `Title`
- imported procedure pairs do not match the app's expected structure

Check:
1. confirm the list is named `Procedure_Categories_01`
2. confirm the main category field is `Title`
3. confirm the subcategory field structure matches the provided CSV files

## PD/Admin Screens Are Missing or Everyone Can See Them

Likely causes:
- `AttendingRole` values do not match the expected role names
- the local attending list has missing or inconsistent role data

Check:
1. inspect `AttendingList`
2. confirm PD/admin users have expected role values
3. review the formulas if your institution uses different leadership titles

## Imported Columns Have Wrong Data Types

Likely causes:
- SharePoint inferred types incorrectly from CSV import

Check these explicitly:
- `EvalDate`
- score-related fields
- comment fields
- email fields

Adjust SharePoint column types manually if needed, then retest the app.

## Existing Records Open but New Records Fail

Likely causes:
- a required column is missing
- a column name differs from what the app expects
- a connector was not reattached correctly

Check:
1. compare local list schema against [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
2. confirm all required columns exist
3. confirm Power Apps data-source warnings are resolved
