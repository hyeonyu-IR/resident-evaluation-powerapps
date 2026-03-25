# Manual SharePoint Schema Guide

This guide documents an important implementation lesson from external testing.

Short version:
- Do **not** rely on simple CSV import to create the schema for `VIR_RealTime_FeedBack`.
- Do **not** rely on simple CSV import to create the schema for `AttendingList`.
- Manually create those two SharePoint lists first.
- Use dummy CSV import only for the resident reference list:
  - `Resident_Year_Name_01`

This approach is more reliable and is now the recommended setup path for outside institutions.

## Why Simple CSV-Based List Creation Can Fail

We found two recurring problems when SharePoint lists were created directly from CSV files.

### 1. SharePoint can assign the wrong internal field names

A column may look correct in SharePoint because the display title appears as expected, but the internal field name can still be different.

Example:
- expected field name in the app: `ResidentYear`
- newly created SharePoint internal field name after CSV-driven creation: `field_4`

Power Apps form cards bind to SharePoint internal field names, not just visible display titles. That means a form can appear connected and still create mostly empty records if the internal field names do not match what the app expects.

### 2. SharePoint can infer the wrong field type

Email-like columns were especially vulnerable during testing.

Examples:
- `AttendingEmail` in `VIR_RealTime_FeedBack`
- `EmailAddress` in `AttendingList`

These sometimes became:
- `Person or Group`

But this app expects them to be:
- `Single line of text`

If those columns are created as `Person or Group`, ownership filtering and related app logic can fail.

## Recommended Setup Order

1. Manually create `VIR_RealTime_FeedBack` with the exact columns and types below.
2. Manually create `AttendingList` with the exact columns and types below.
3. Manually create or preserve `Procedure_Categories_01` with the expected taxonomy.
4. Import dummy CSV data only for:
   - `Resident_Year_Name_01`
5. If desired, use the dummy feedback, attending, and procedure CSV files as reference data only after the lists already exist with the correct schema.
6. Import `UNC_VIR_Resident_Evaluation.msapp`.
7. Reconnect SharePoint and Outlook in Power Apps Studio.
8. Run smoke tests before production use.

## Manual Schema: `VIR_RealTime_FeedBack`

Create this SharePoint list manually:
- `VIR_RealTime_FeedBack`

Create these columns manually.

| Column Name | SharePoint Type |
| --- | --- |
| `EvalDate` | Date and Time |
| `Attending` | Single line of text |
| `ResidentYear` | Single line of text |
| `ResidentName` | Single line of text |
| `ProcedureMain` | Single line of text |
| `Comment` | Multiple lines of text |
| `ProcedureSub` | Single line of text |
| `AverageScore` | Single line of text |
| `Non_Preoperative` | Single line of text |
| `Intraoperative` | Single line of text |
| `Postoperative` | Single line of text |
| `AttendingEmail` | Single line of text |
| `Eval_Serial_No` | Number |

Do not manually create these SharePoint-managed columns:
- `Title`
- `Modified`
- `Created`
- `Created By`
- `Modified By`

Important:
- `AttendingEmail` must remain `Single line of text`.
- Do not let SharePoint convert it to `Person or Group`.
- The app expects these names exactly.

## Manual Schema: `AttendingList`

Create this SharePoint list manually:
- `AttendingList`

Create these columns manually.

| Column Name | SharePoint Type |
| --- | --- |
| `AttendingName` | Single line of text |
| `EmailAddress` | Single line of text |
| `AttendingRole` | Single line of text |

Do not manually create these SharePoint-managed columns:
- `Title`
- `Modified`
- `Created`
- `Created By`
- `Modified By`

Important:
- `EmailAddress` must remain `Single line of text`.
- Do not let SharePoint convert it to `Person or Group`.
- PD/admin access depends on `AttendingRole`.

## Dummy CSV Still Worth Using

The one dummy CSV that remains clearly useful for external setup is:
- [`../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv`](../sharepoint-templates/dummy/Resident_Year_Name_01.dummy.csv)

`Procedure_Categories_01` is typically a constant list and does not require a dummy import for routine setup if the list is created correctly.

## How To Use The Dummy Feedback And Attending CSV Files

The following files are still useful, but they should no longer be treated as the primary schema-creation path for outside institutions:
- [`../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv`](../sharepoint-templates/dummy/VIR_RealTime_FeedBack.dummy.csv)
- [`../sharepoint-templates/dummy/AttendingList.dummy.csv`](../sharepoint-templates/dummy/AttendingList.dummy.csv)

Recommended use:
- use them as examples of expected columns and sample content
- use them only after the SharePoint lists already exist with the correct manual schema
- do not use them as the first step to generate the SharePoint schema automatically

## Reconnect Caveat: Stats Chart Labels

During testing, we found that disconnecting and reconnecting data sources could cause the stats chart label bindings to drift.

After reconnect, verify:
- `ccAttendingFeedbackNo.Items.Labels = Attending`
- `ccProcedurePct.Items.Labels = ProcedureMain`

If those properties drift to `Count` or `Metric`, the chart may render with incorrect x-axis labels even though the underlying data is correct.

## Practical Lesson

This was a hard-earned but valuable lesson. The app itself was portable, but SharePoint schema creation was more fragile than it first appeared.

The most reliable external implementation path is now:
- manually create the main feedback list
- manually create the attending list
- confirm email columns are plain text
- preserve exact field names
- import only the lighter reference lists from CSV

That workflow makes external deployment much more stable and predictable.
