# FAQ

This FAQ is intended to answer the most common implementation and setup questions before an institution reaches out for help.

## Do I need the full exported Power Apps `.zip` package to implement the app?

No. For normal adoption, the main file needed for import is:
- [`../app/releases/UNC_VIR_Resident_Evaluation.msapp`](../app/releases/UNC_VIR_Resident_Evaluation.msapp)

The raw exported folder structure and internal JSON files are not normally required for another institution to import and use the app.

## Which files should I download first?

The simplest starting point is:
- [`../download-files`](../download-files)

That folder contains:
- the latest `.msapp`
- the two supported CSV files
- a short README focused on downloading and initial setup

## Should I create the SharePoint lists before importing the `.msapp`?

Yes.

Best practice:
1. create the four required SharePoint lists first
2. manually create the schema for `VIR_RealTime_FeedBack`
3. manually create the schema for `AttendingList`
4. create `Procedure_Categories_01` from the preserved original procedure-category CSV
5. import CSV directly only for `Resident_Year_Name_01`
6. import the `.msapp`
7. open it in Power Apps Studio and connect SharePoint and Outlook when prompted

## Why should I not create `VIR_RealTime_FeedBack` from CSV?

Because SharePoint can create the wrong internal field names even when the display titles look correct.

Example:
- visible title: `ResidentYear`
- actual internal field name: `field_4`

Power Apps binds to internal field names. That can lead to blank or partially blank records even though the app appears connected.

More careful interpretation:
- list reads may appear to work when display names and field types look correct
- form submission can still fail unless the underlying SharePoint field identities also match the app's expected bindings

## Why should I not create `AttendingList` from CSV?

Because SharePoint may infer:
- `EmailAddress`

as:
- `Person or Group`

This app expects:
- `EmailAddress` to be `Single line of text`

The same risk exists for:
- `AttendingEmail` in `VIR_RealTime_FeedBack`

## Which CSV files should I use directly?

Import this directly:
- `Resident_Year_Name_01.dummy.csv`

Use this to generate the procedure category list:
- `Procedure_Categories_01.dummy.csv`

## Do the SharePoint list names need to match exactly?

Yes, that is strongly recommended.

Expected SharePoint list names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

If different list names are used, the app may still be adoptable, but the team should expect:
- data-source remapping
- possible formula updates

## Do the SharePoint column names need to match exactly?

Yes, for most fields.

For setup purposes, treat them as case-sensitive and match them exactly, including:
- capitalization
- spelling
- underscores

Important fields include:
- `AttendingEmail`
- `AttendingRole`
- `ResidentYear`
- `ResidentName`
- `ProcedureMain`
- `ProcedureSub`
- `EvalDate`

If those field names differ, filtering, reports, or dropdown behavior can fail.

## Which SharePoint field types matter most?

These are the most important ones:
- `AttendingEmail` should be `Single line of text`
- `EmailAddress` should be `Single line of text`
- `EvalDate` should be `Date and Time`
- `Comment` should be `Multiple lines of text`
- `Eval_Serial_No` should be `Number`

## Why does the app not find my SharePoint data after import?

Common causes:
- SharePoint list names do not match expected names
- data sources were not reconnected
- the imported app still points to the original tenant's connections
- the target SharePoint schema was created incorrectly

Use:
- [`07_TROUBLESHOOTING.md`](07_TROUBLESHOOTING.md)

## Why does "My Feedback" show the wrong records?

Common causes:
- `AttendingEmail` is missing or blank
- `AttendingEmail` is not a text field
- old data was not backfilled properly
- formulas were changed away from email-based ownership logic

The current app expects ownership filtering to rely on `AttendingEmail`.

## Why are PD/admin-only screens not behaving correctly?

Those screens depend on:
- `AttendingRole` values in `AttendingList`

If local leadership role names differ, the role mapping may need adjustment.

## Why does procedure filtering break?

Procedure filtering is sensitive to the structure of:
- `Procedure_Categories_01`

The app expects:
- the main category field in `Procedure_Categories_01.Title`
- a consistent main/subcategory relationship

If the taxonomy is changed casually, dependent dropdown behavior can break.

## Why do the stats chart x-axis labels turn into count or metric after reconnect?

This is a known chart-default issue during first connect and reconnect.

The two stats chart x-axis labels are not hard-coded. When the lists are connected for the first time, or reconnected later, the chart control can revert to its default label fields:
- `Count`
- `Metric`

Check these properties manually:
- `ccAttendingFeedbackNo.Items.Labels` should be `Attending`
- `ccProcedurePct.Items.Labels` should be `ProcedureMain`

If those values drift to `Count` or `Metric`, the chart will still render but the x-axis labels will be wrong.

## Can the app be implemented without personal help from the original maintainer?

Often yes, but not always for every possible adopter.

This repository is likely sufficient for someone who is:
- clinically interested
- reasonably comfortable with Microsoft 365
- able to work with SharePoint and Power Apps Studio
- willing to follow documentation carefully

It should not be assumed to be fully standalone for every possible user with no Power Apps or SharePoint familiarity.

## What level of technical comfort is expected?

Successful implementation usually requires some familiarity with:
- Power Apps
- SharePoint list setup
- Microsoft 365 permissions and connectors
- troubleshooting schema mismatches

## Where should I start if I am evaluating the app for my institution?

Recommended order:
1. [`00_START_HERE.md`](00_START_HERE.md)
2. [`02_MANUAL_SHAREPOINT_SCHEMA.md`](02_MANUAL_SHAREPOINT_SCHEMA.md)
3. [`../download-files`](../download-files)
4. [`03_SETUP_GUIDE.md`](03_SETUP_GUIDE.md)
5. [`04_CONNECTION_MAP.md`](04_CONNECTION_MAP.md)
6. [`05_IMPLEMENTATION_CHECKLIST.md`](05_IMPLEMENTATION_CHECKLIST.md)
7. [`07_TROUBLESHOOTING.md`](07_TROUBLESHOOTING.md)

## Can the app be customized for local workflows?

Yes, but local customization may require Power Apps changes.

Typical customization areas:
- local role naming
- procedure taxonomy
- evaluation fields
- branding
- local reporting expectations

## Where should institutions look before asking for help?

Start with:
- [`00_START_HERE.md`](00_START_HERE.md)
- [`02_MANUAL_SHAREPOINT_SCHEMA.md`](02_MANUAL_SHAREPOINT_SCHEMA.md)
- [`03_SETUP_GUIDE.md`](03_SETUP_GUIDE.md)
- [`04_CONNECTION_MAP.md`](04_CONNECTION_MAP.md)
- [`05_IMPLEMENTATION_CHECKLIST.md`](05_IMPLEMENTATION_CHECKLIST.md)
- [`07_TROUBLESHOOTING.md`](07_TROUBLESHOOTING.md)
- [`09_USER_GUIDE.md`](09_USER_GUIDE.md)

