# FAQ

This FAQ is intended to answer the most common implementation and setup questions before an institution reaches out for help.

## Do I need the full exported Power Apps `.zip` package to implement the app?

No. For normal adoption, the main file needed for import is:
- [`UNC_VIR_Resident_Evaluation.msapp`](../app/releases/UNC_VIR_Resident_Evaluation.msapp)

The raw exported folder structure and internal JSON files are not normally required for another institution to import and use the app.

## Which files should I download first?

The simplest starting point is:
- [`../download-files`](../download-files)

That folder contains:
- the latest `.msapp`
- the 4 recommended dummy CSV files
- a short README focused on downloading and initial setup

## Should I create the SharePoint lists before importing the `.msapp`?

Yes. That is the recommended order.

Best practice:
1. create the four required SharePoint lists first
2. import the CSV starter files into those lists
3. import the `.msapp`
4. open it in Power Apps Studio and connect SharePoint and Outlook when prompted

Why:
- on first open, Power Apps will prompt for SharePoint and Office 365 Outlook connections
- that connection step is smoother when the required lists already exist with the expected names and columns

## Which CSV files should I use?

For most institutions, use the `dummy` CSV files first.

Why:
- they are non-sensitive
- they are internally compatible with the app
- they make it easier to test the workflow quickly

Use:
- `AttendingList.dummy.csv`
- `Resident_Year_Name_01.dummy.csv`
- `Procedure_Categories_01.dummy.csv`
- `VIR_RealTime_FeedBack.dummy.csv`

Use `template` or `blank` files only if the local team prefers to build the lists more manually.

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

These are the most important ones to review manually after CSV import:
- `EvalDate` should be Date/Time
- score-related fields should be numeric
- comment fields should allow enough text
- `AttendingEmail` should remain Single line of text unless the app is intentionally redesigned to use a Person column

## Why does the app not find my SharePoint data after import?

Common causes:
- SharePoint list names do not match expected names
- data sources were not reconnected
- the imported app still points to the original tenant's connections

Use:
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

## Why does "My Feedback" show the wrong records?

Common causes:
- `AttendingEmail` is missing or blank
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

## What is the difference between the implementation manual `.docx` and `.pdf`?

- [`Resident_Evaluation_Implementation_Manual.docx`](assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable master document
- [`Resident_Evaluation_Implementation_Guide_Published.pdf`](assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published reader-facing PDF copy

The repository treats the `.docx` as the source of truth for future edits.

## Where should I start if I am evaluating the app for my institution?

Recommended order:
1. [`START_HERE.md`](START_HERE.md)
2. [`../download-files`](../download-files)
3. [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
4. [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
5. [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md)
6. [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)

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
- [`START_HERE.md`](START_HERE.md)
- [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
- [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
- [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md)
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
- [`USER_GUIDE.md`](USER_GUIDE.md)
