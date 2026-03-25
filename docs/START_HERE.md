# Start Here

This page is for institutions that want to evaluate or implement this Power Apps resident-evaluation app.

## What You Need

- A Microsoft 365 environment with Power Apps access
- SharePoint Online
- Permission to create SharePoint lists and import a canvas app
- Someone who can reconnect data sources in Power Apps Studio

## Most Important Lesson First

Do not use simple CSV import to create the schema for:
- `VIR_RealTime_FeedBack`
- `AttendingList`

Use manual SharePoint list creation for those two lists instead.

Why:
- SharePoint can create the wrong internal field names
- Power Apps binds to internal field names, not just visible display titles
- SharePoint can infer email columns as `Person or Group` instead of `Single line of text`

Read this before you build anything:
- [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)

## Fastest Reliable Evaluation Path

If you want to assess whether this app is suitable for your program:
1. Open [`../download-files`](../download-files).
2. Review the expected SharePoint list names in [`CONNECTION_MAP.md`](CONNECTION_MAP.md).
3. Read [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md).
4. Manually create `VIR_RealTime_FeedBack`.
5. Manually create `AttendingList`.
6. Manually create or preserve `Procedure_Categories_01`.
7. Import `Resident_Year_Name_01.dummy.csv` if you want starter resident data.
8. Only after the SharePoint lists exist, import the included `.msapp`.
9. When Power Apps prompts for connections, reconnect SharePoint and Outlook.
10. Run the smoke tests in [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md).

## Simplest Download Path

For most institutions, the easiest path is:
- [`../download-files`](../download-files)

That folder intentionally contains the minimum recommended files for initial setup.

## Expected SharePoint Lists

Create these lists with these exact names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

If your local SharePoint list names differ, expect to reconnect data sources and possibly update formulas.

Important:
- create these SharePoint lists before opening the imported `.msapp` in Power Apps Studio
- on first open, Power Apps will ask you to connect SharePoint and Office 365 Outlook
- that connection step works best when the lists already exist with the expected names and correct schema

## Which CSV Files Should You Use?

Import this directly if you want starter resident data:
- [`../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv`](../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv)

Use these as reference/sample data only after manual list creation:
- [`../sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv`](../sharepoint-templates/dummy/Procedure_Categories_01.dummy.csv)
- [`../sharepoint-templates/dummy/AttendingList.dummy.csv`](../sharepoint-templates/dummy/AttendingList.dummy.csv)
- [`../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv`](../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv)

## Recommended Reading Order

1. [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)
2. [`SETUP_GUIDE.md`](SETUP_GUIDE.md)
3. [`CONNECTION_MAP.md`](CONNECTION_MAP.md)
4. [`FAQ.md`](FAQ.md)
5. [`IMPLEMENTATION_CHECKLIST.md`](IMPLEMENTATION_CHECKLIST.md)
6. [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)
7. [`USER_GUIDE.md`](USER_GUIDE.md)

## Critical Adoption Notes

- The app uses `AttendingEmail` for record ownership and "My Feedback" filtering.
- `AttendingEmail` must be `Single line of text`.
- `EmailAddress` in `AttendingList` must also be `Single line of text`.
- PD/admin access is driven by `AttendingRole`.
- Procedure filtering depends on preserving the original main/subcategory structure.
- After reconnecting data sources, the stats chart label bindings may drift:
  - `ccAttendingFeedbackNo.Items.Labels` should be `Attending`
  - `ccProcedurePct.Items.Labels` should be `ProcedureMain`
- CSV filenames are not the same thing as SharePoint list names.

## Visual Walkthrough

If you want to see the user-facing workflow before implementation:
- [`USER_GUIDE.md`](USER_GUIDE.md)
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## Comprehensive Manual

If you want the implementation manual:
- [`Resident_Evaluation_Implementation_Manual.docx`](assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable master version
- [`Resident_Evaluation_Implementation_Guide_Published.pdf`](assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published PDF version
- [`COMPREHENSIVE_MANUAL.md`](COMPREHENSIVE_MANUAL.md)
  - supporting Markdown reference

## When You Should Customize

You should expect local customization if:
- your institution uses different list names
- your role names differ from `program director`, `pd`, `admin`, or similar values
- you intentionally redesign the app to use Person columns instead of text email fields
- you need branding, policy, or workflow changes
