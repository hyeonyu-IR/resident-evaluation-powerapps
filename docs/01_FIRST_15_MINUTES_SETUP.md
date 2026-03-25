# First 15 Minutes Setup

This guide is the quickest reliable path for a new institution to test whether the app can be connected and used locally.

The goal is simple:
- create the required SharePoint lists
- import the app
- reconnect the data sources
- submit one test feedback record

If that works, you can move on to the more detailed setup and rollout guides.

## What You Need Before Starting

- Power Apps access in Microsoft 365
- SharePoint Online access
- permission to create SharePoint lists
- permission to import a canvas app
- the files in [download-files](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/download-files)

If you want the full background first, start here:
- [00_START_HERE.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/00_START_HERE.md)

## Step 1: Create Four SharePoint Lists

Create these lists with these exact names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

Important:
- create the names exactly, including capitalization and underscores
- do this before importing the `.msapp`

Reference:
- [04_CONNECTION_MAP.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/04_CONNECTION_MAP.md)

## Step 2: Manually Create the Two Critical Lists

Do **not** use simple CSV-based SharePoint list creation for:
- `VIR_RealTime_FeedBack`
- `AttendingList`

Create those two lists manually.

Why:
- SharePoint can create the wrong hidden/internal field names
- email fields can become the wrong type
- the app may look connected but fail when writing data

Use these detailed schema tables:
- [02_MANUAL_SHAREPOINT_SCHEMA.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/02_MANUAL_SHAREPOINT_SCHEMA.md)

Most important fields:
- `AttendingEmail` in `VIR_RealTime_FeedBack` must be `Single line of text`
- `EmailAddress` in `AttendingList` must be `Single line of text`

## Step 3: Load the Two Supported CSV-Based Lists

Use these files from [download-files](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/download-files):

- [Resident_Year_Name_01.dummy.csv](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/download-files/Resident_Year_Name_01.dummy.csv)
- [Procedure_Categories_01.dummy.csv](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/download-files/Procedure_Categories_01.dummy.csv)

Use:
- the resident CSV for starter resident data
- the procedure CSV to generate the procedure-category list

More detail:
- [03_SETUP_GUIDE.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/03_SETUP_GUIDE.md)

## Step 4: Import the App

Import:
- [UNC_VIR_Resident_Evaluation.msapp](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/download-files/UNC_VIR_Resident_Evaluation.msapp)

Then open it in Power Apps Studio.

## Step 5: Reconnect the Data Sources

When Power Apps prompts you, connect:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`
- Office 365 Outlook

If you need the full reconnect workflow:
- [03_SETUP_GUIDE.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/03_SETUP_GUIDE.md)
- [07_TROUBLESHOOTING.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/07_TROUBLESHOOTING.md)

## Step 6: Submit One Test Feedback Record

Confirm that you can:
- open the app
- select a resident
- select a procedure
- enter scores
- submit one test feedback record

Then confirm that:
- the record appears in `VIR_RealTime_FeedBack`
- the detail screen loads correctly
- the My Feedback history screen shows the record

Use:
- [05_IMPLEMENTATION_CHECKLIST.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/05_IMPLEMENTATION_CHECKLIST.md)

## Step 7: If the Test Works, Move to the Next Guides

Once one test record is submitted successfully, continue with:

- [03_SETUP_GUIDE.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/03_SETUP_GUIDE.md)
  - for the full setup and reconnection process
- [06_POST_SETUP_ROLLOUT_GUIDE.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/06_POST_SETUP_ROLLOUT_GUIDE.md)
  - for sharing the app and lists with faculty users
- [07_TROUBLESHOOTING.md](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/07_TROUBLESHOOTING.md)
  - if anything behaves unexpectedly

## One Important Reminder

The stats chart labels are not hard-coded.

After first connect or reconnect, they can revert to the default chart fields:
- `Count`
- `Metric`

If that happens, reset:
- `ccAttendingFeedbackNo.Items.Labels = Attending`
- `ccProcedurePct.Items.Labels = ProcedureMain`

That issue does not usually block initial testing, but it is worth checking before broader rollout.

Visual reference:
- [07_TROUBLESHOOTING.md](07_TROUBLESHOOTING.md)

