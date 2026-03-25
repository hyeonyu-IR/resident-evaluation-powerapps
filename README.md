# UNC VIR Resident Evaluation

Canvas app for resident evaluation built in Microsoft Power Apps with SharePoint-backed data sources.

This repository is intended to be usable by outside institutions without direct one-on-one walkthroughs. It contains:
- an importable Power Apps canvas app package
- the two CSV files still needed for outside adoption
- setup and reconnection instructions
- post-setup rollout guidance for local owners
- implementation and validation checklists
- a visual user guide with screenshots from the app

## Most Important Setup Update

The safest external setup path is now:
- manually create `VIR_RealTime_FeedBack`
- manually create `AttendingList`
- generate `Procedure_Categories_01` from the preserved original procedure-category CSV
- use dummy CSV only for:
  - `Resident_Year_Name_01`

Do not rely on simple CSV import to create the schema for `VIR_RealTime_FeedBack` or `AttendingList`.

Why:
- SharePoint can assign incorrect internal field names such as `field_4` even when the visible column title looks correct
- Power Apps binds to SharePoint internal field names, not just display titles
- SharePoint can infer email columns as `Person or Group`, which breaks this app's text-based ownership logic

Practical caution:
- list reads may appear to work when display names and field types look correct
- form submission can still fail unless the underlying SharePoint field identities also match the app's expected bindings

Start here:
- [`docs/02_MANUAL_SHAREPOINT_SCHEMA.md`](docs/02_MANUAL_SHAREPOINT_SCHEMA.md)

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
1. [`docs/00_START_HERE.md`](docs/00_START_HERE.md)
2. [`docs/01_FIRST_15_MINUTES_SETUP.md`](docs/01_FIRST_15_MINUTES_SETUP.md)
3. [`download-files`](download-files)
4. [`docs/02_MANUAL_SHAREPOINT_SCHEMA.md`](docs/02_MANUAL_SHAREPOINT_SCHEMA.md)
5. [`docs/03_SETUP_GUIDE.md`](docs/03_SETUP_GUIDE.md)
6. [`docs/04_CONNECTION_MAP.md`](docs/04_CONNECTION_MAP.md)
7. [`docs/08_FAQ.md`](docs/08_FAQ.md)
8. [`docs/05_IMPLEMENTATION_CHECKLIST.md`](docs/05_IMPLEMENTATION_CHECKLIST.md)
9. [`docs/06_POST_SETUP_ROLLOUT_GUIDE.md`](docs/06_POST_SETUP_ROLLOUT_GUIDE.md)
10. [`docs/07_TROUBLESHOOTING.md`](docs/07_TROUBLESHOOTING.md)
11. [`docs/09_USER_GUIDE.md`](docs/09_USER_GUIDE.md)
12. [`docs/assets/Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
13. [`docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf)

## What This Repository Contains

- [`app/releases`](app/releases)
  - the single latest importable `.msapp` file
- [`download-files`](download-files)
  - the two supported CSV files plus the importable `.msapp`
- [`docs`](docs)
  - adoption, setup, troubleshooting, and maintenance documentation
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
4. Create `Procedure_Categories_01` from the preserved original procedure-category CSV.
5. Use dummy CSV only for `Resident_Year_Name_01`.
6. Use only the two supported CSV files for setup:
   - `Resident_Year_Name_01.dummy.csv`
   - `Procedure_Categories_01.dummy.csv`
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
- the two supported CSV files
- a short download-specific README

If you want the shortest practical setup path first, use:
- [`docs/01_FIRST_15_MINUTES_SETUP.md`](docs/01_FIRST_15_MINUTES_SETUP.md)

After setup and testing are complete, use:
- [`docs/06_POST_SETUP_ROLLOUT_GUIDE.md`](docs/06_POST_SETUP_ROLLOUT_GUIDE.md)

## Visual User Documentation

For end-user workflow screenshots and a slide-based walkthrough:
- [`docs/09_USER_GUIDE.md`](docs/09_USER_GUIDE.md)
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](docs/assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## Implementation Manual

For the implementation manual:
- [`Resident_Evaluation_Implementation_Manual.docx`](docs/assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable source-of-truth document
- [`Resident_Evaluation_Implementation_Guide_Published.pdf`](docs/assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published PDF for distribution
- [`10_COMPREHENSIVE_MANUAL.md`](docs/10_COMPREHENSIVE_MANUAL.md)
  - supporting Markdown reference

## Post-Setup Rollout

After the app is connected and one test feedback submission works, the next step is local rollout to faculty users. That includes:
- sharing the app itself
- sharing the four SharePoint lists
- confirming faculty submission access
- confirming program leadership reporting access

Use:
- [`docs/06_POST_SETUP_ROLLOUT_GUIDE.md`](docs/06_POST_SETUP_ROLLOUT_GUIDE.md)

For common implementation and connection questions:
- [`docs/08_FAQ.md`](docs/08_FAQ.md)

## Required Microsoft 365 Dependencies

- SharePoint Online
- Office 365 Outlook connector

## Questions / Contact

If your institution is adopting this app and needs reasonable setup guidance, you may contact:

- `Hyeon Yu, MD, FSIR`
- `hyeon_yu@med.unc.edu`

## Critical Implementation Rules

- SharePoint list names should match the expected app data source names exactly.
- SharePoint column names should also match exactly unless you plan to modify app formulas.
- SharePoint internal field names matter, not just display titles.
- The app relies on `AttendingEmail` for stable ownership filtering.
- `AttendingEmail` must be `Single line of text`.
- `EmailAddress` in `AttendingList` must also be `Single line of text`.
- `AttendingRole` in `AttendingList` controls PD/admin access.
- Procedure filtering assumes `Procedure_Categories_01.Title` is the main category field.
- The stats chart x-axis labels are not hard-coded. On first connect or after reconnect, they can revert to the chart defaults `Count` and `Metric`, so they may need to be reset manually:
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

