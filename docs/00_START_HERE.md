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

Practical caution:
- list reads may appear to work when display names and field types look correct
- form submission can still fail unless the underlying SharePoint field identities also match the app's expected bindings

Read this before you build anything:
- [`02_MANUAL_SHAREPOINT_SCHEMA.md`](02_MANUAL_SHAREPOINT_SCHEMA.md)

If you want the shortest practical setup path first:
- [`01_FIRST_15_MINUTES_SETUP.md`](01_FIRST_15_MINUTES_SETUP.md)

## Fastest Reliable Evaluation Path

If you want to assess whether this app is suitable for your program:
1. Open [`../download-files`](../download-files).
2. If you want the shortest path, follow [`01_FIRST_15_MINUTES_SETUP.md`](01_FIRST_15_MINUTES_SETUP.md).
3. Review the expected SharePoint list names in [`04_CONNECTION_MAP.md`](04_CONNECTION_MAP.md).
4. Read [`02_MANUAL_SHAREPOINT_SCHEMA.md`](02_MANUAL_SHAREPOINT_SCHEMA.md).
5. Manually create `VIR_RealTime_FeedBack`.
6. Manually create `AttendingList`.
7. Create `Procedure_Categories_01` from the preserved original procedure-category CSV.
8. Import `Resident_Year_Name_01.dummy.csv` if you want starter resident data.
9. Only after the SharePoint lists exist, import the included `.msapp`.
10. When Power Apps prompts for connections, reconnect SharePoint and Outlook.
11. Run the smoke tests in [`05_IMPLEMENTATION_CHECKLIST.md`](05_IMPLEMENTATION_CHECKLIST.md).
12. After the app works and a test submission succeeds, use [`06_POST_SETUP_ROLLOUT_GUIDE.md`](06_POST_SETUP_ROLLOUT_GUIDE.md).

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
- [`../download-files/Resident_Year_Name_01.dummy.csv`](../download-files/Resident_Year_Name_01.dummy.csv)

Use this to generate the procedure category list:
- [`../download-files/Procedure_Categories_01.dummy.csv`](../download-files/Procedure_Categories_01.dummy.csv)

## Recommended Reading Order

1. [`01_FIRST_15_MINUTES_SETUP.md`](01_FIRST_15_MINUTES_SETUP.md)
2. [`02_MANUAL_SHAREPOINT_SCHEMA.md`](02_MANUAL_SHAREPOINT_SCHEMA.md)
3. [`03_SETUP_GUIDE.md`](03_SETUP_GUIDE.md)
4. [`04_CONNECTION_MAP.md`](04_CONNECTION_MAP.md)
5. [`08_FAQ.md`](08_FAQ.md)
6. [`05_IMPLEMENTATION_CHECKLIST.md`](05_IMPLEMENTATION_CHECKLIST.md)
7. [`06_POST_SETUP_ROLLOUT_GUIDE.md`](06_POST_SETUP_ROLLOUT_GUIDE.md)
8. [`07_TROUBLESHOOTING.md`](07_TROUBLESHOOTING.md)
9. [`09_USER_GUIDE.md`](09_USER_GUIDE.md)

## Critical Adoption Notes

- The app uses `AttendingEmail` for record ownership and "My Feedback" filtering.
- `AttendingEmail` must be `Single line of text`.
- `EmailAddress` in `AttendingList` must also be `Single line of text`.
- PD/admin access is driven by `AttendingRole`.
- Procedure filtering depends on preserving the original main/subcategory structure.
- The stats chart x-axis labels are not hard-coded. On first connect or after reconnect, they can revert to the chart defaults `Count` and `Metric`:
  - `ccAttendingFeedbackNo.Items.Labels` should be `Attending`
  - `ccProcedurePct.Items.Labels` should be `ProcedureMain`
- CSV filenames are not the same thing as SharePoint list names.

## Visual Walkthrough

If you want to see the user-facing workflow before implementation:
- [`09_USER_GUIDE.md`](09_USER_GUIDE.md)
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## Comprehensive Manual

If you want the implementation manual:
- [`Resident_Evaluation_Implementation_Manual.docx`](assets/Resident_Evaluation_Implementation_Manual.docx)
  - editable master version
- [`Resident_Evaluation_Implementation_Guide_Published.pdf`](assets/Resident_Evaluation_Implementation_Guide_Published.pdf)
  - published PDF version
- [`10_COMPREHENSIVE_MANUAL.md`](10_COMPREHENSIVE_MANUAL.md)
  - supporting Markdown reference

## When You Should Customize

You should expect local customization if:
- your institution uses different list names
- your role names differ from `program director`, `pd`, `admin`, or similar values
- you intentionally redesign the app to use Person columns instead of text email fields
- you need branding, policy, or workflow changes

