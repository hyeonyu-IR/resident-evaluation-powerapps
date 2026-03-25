# UNC VIR Resident Evaluation

Canvas app for resident evaluation built in Microsoft Power Apps with SharePoint-backed data sources.

This repository is intended to be usable by outside institutions without direct one-on-one walkthroughs. It contains:
- an importable Power Apps canvas app package
- SharePoint starter data and schema templates
- setup and reconnection instructions
- implementation and validation checklists
- a visual user guide with screenshots from the app

## Most Important Setup Update

The safest external setup path is now:
- manually create `VIR_RealTime_FeedBack`
- manually create `AttendingList`
- manually create or preserve `Procedure_Categories_01`
- use dummy CSV only for:
  - `Resident_Year_Name_01`

Do not rely on simple CSV import to create the schema for `VIR_RealTime_FeedBack` or `AttendingList`.

Why:
- SharePoint can assign incorrect internal field names such as `field_4` even when the visible column title looks correct
- Power Apps binds to SharePoint internal field names, not just display titles
- SharePoint can infer email columns as `Person or Group`, which breaks this app's text-based ownership logic

Start here:
- [`docs/MANUAL_SHAREPOINT_SCHEMA.md`](docs/MANUAL_SHAREPOINT_SCHEMA.md)

## Who This Repository Is For

This repository is likely a good fit for adopters who are:
- clinically interested
- reasonably comfortable with Microsoft 365
- able to work with SharePoint and Power Apps Studio
- willing to follow documentation carefully

For that audience, the repository is likely sufficient to:
- understand what the app does
- create the SharePoint lists correctly
- import the app
- reconnect the data sources
- test the workflow
- decide whether it fits the local institution

## Important Limitation

This repository is designed as a serious self-service implementation package, but it should not be assumed to be fully standalone for every possible user.

Successful implementation still depends on some working familiarity with:
- Power Apps
- SharePoint list setup
- Microsoft 365 permissions and connectors
- troubleshooting schema mismatches

## Important Setup Order

Create the SharePoint lists before importing the `.msapp`.

When the app is imported and opened in Power Apps Studio, Power Apps will immediately prompt for SharePoint and Office 365 Outlook connections. That setup is much smoother if the required SharePoint lists already exist with the expected names, internal field names, and column types.

## Start Here

If you are evaluating or adopting this app for another institution, read these in order:
1. [`docs/START_HERE.md`](docs/START_HERE.md)
2. [`download-files`](download-files)
3. [`docs/MANUAL_SHAREPOINT_SCHEMA.md`](docs/MANUAL_SHAREPOINT_SCHEMA.md)
4. [`docs/SETUP_GUIDE.md`](docs/SETUP_GUIDE.md)
5. [`docs/CONNECTION_MAP.md`](docs/CONNECTION_MAP.md)
6. [`docs/FAQ.md`](docs/FAQ.md)
7. [`docs/IMPLEMENTATION_CHECKLIST.md`](docs/IMPLEMENTATION_CHECKLIST.md)
8. [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md)
9. [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md)
10. [`docs/assets/Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
11. [`docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf)

## What This Repository Contains

- [`app/releases`](app/releases)
  - the single latest importable `.msapp` file
- [`sharepoint-templates/dummy`](sharepoint-templates/dummy)
  - starter/reference CSV files
- [`sharepoint-templates/template`](sharepoint-templates/template)
  - minimal example CSV files
- [`sharepoint-templates/blank`](sharepoint-templates/blank)
  - header-only CSV files
- [`docs`](docs)
  - adoption, setup, troubleshooting, and maintenance documentation
- [`download-files`](download-files)
  - single-place starter download bundle for adopters
- [`docs/screenshots`](docs/screenshots)
  - selected app screenshots for onboarding and user documentation
- [`docs/assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](docs/assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)
  - full slide-based visual guide
- [`docs/assets/Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable master implementation manual
- [`docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published PDF copy of the implementation manual
- [`_unpacked`](_unpacked)
  - unpacked app source for review and diffing

## Quick Adoption Summary

To implement this app at another institution:
1. Create four SharePoint lists with the exact expected names.
2. Manually create `VIR_RealTime_FeedBack` with the expected schema.
3. Manually create `AttendingList` with the expected schema.
4. Manually create or preserve `Procedure_Categories_01` with the expected constant taxonomy.
5. Use dummy CSV only for `Resident_Year_Name_01`.
6. Use the dummy feedback, attending, and procedure CSV files only as reference/sample files if needed.
7. Import the latest `.msapp` into Power Apps after the SharePoint lists already exist.
8. When prompted, reconnect the app to the local SharePoint lists and Outlook connector.
9. Run the smoke-test checklist before production use.

Required SharePoint list names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

Critical schema rules:
- `AttendingEmail` in `VIR_RealTime_FeedBack` must be `Single line of text`
- `EmailAddress` in `AttendingList` must be `Single line of text`
- do not let SharePoint convert either one to `Person or Group`

## Download These Files

If you want the simplest starting point, go to:
- [`download-files`](download-files)

That folder contains:
- the latest `.msapp`
- the four reference CSV files
- a short download-specific README

## Recommended Files for New Institutions

Import this directly if you want starter resident data:
- [`Resident_Year_Name_01.dummy.csv`](sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv)

Use these as reference/sample files only after the lists already exist with the correct manual schema:
- [`Procedure_Categories_01.dummy.csv`](sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv)
- [`AttendingList.dummy.csv`](sharepoint-templates/dummy/AttendingList.dummy.csv)
- [`VIR_RealTime_FeedBack.dummy.csv`](sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv)

## Visual User Documentation

For end-user workflow screenshots and a slide-based walkthrough:
- [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md)
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](docs/assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## Implementation Manual

For the implementation manual:
- [`Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable source-of-truth document
- [`Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published PDF for distribution
- [`COMPREHENSIVE_MANUAL.md`](docs/COMPREHENSIVE_MANUAL.md)
  - supporting Markdown reference

## FAQ

For common implementation and connection questions:
- [`docs/FAQ.md`](docs/FAQ.md)

## Required Microsoft 365 Dependencies

- SharePoint Online
- Office 365 Outlook connector

## Critical Implementation Rules

- SharePoint list names should match the expected app data source names exactly.
- SharePoint column names should also match exactly unless you plan to modify app formulas.
- SharePoint internal field names matter, not just display titles.
- The app relies on `AttendingEmail` for stable ownership filtering.
- `AttendingEmail` must be `Single line of text`.
- `EmailAddress` in `AttendingList` must also be `Single line of text`.
- `AttendingRole` in `AttendingList` controls PD/admin access.
- Procedure filtering assumes `Procedure_Categories_01.Title` is the main category field.
- After reconnecting data sources, the stats chart label bindings may drift and need to be reset manually:
  - `ccAttendingFeedbackNo.Items.Labels = Attending`
  - `ccProcedurePct.Items.Labels = ProcedureMain`

## For Maintainers

If you are updating the source repository itself:
- [`docs/RELEASE_WORKFLOW.md`](docs/RELEASE_WORKFLOW.md)
- [`docs/REPOSITORY_POLICY.md`](docs/REPOSITORY_POLICY.md)
- [`CHANGELOG.md`](CHANGELOG.md)

Manual workflow:
- edit [`docs/assets/Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
- export/update [`docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf) from Word
- treat the DOCX as the editable master and the PDF as the published copy

## Privacy

Do not commit or share real resident, attending, or evaluation data unless disclosure is intentional and approved.
