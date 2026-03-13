# Setup Guide

See also:
- [`CONNECTION_MAP.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/CONNECTION_MAP.md)

## 1. Create SharePoint lists

Create these lists in the target tenant:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

Use the CSV files in [`sharepoint-templates`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates) as schema starters.

## 2. Seed reference data

Minimum data required:
- Attendings with email and role
- Resident year/name rows
- Procedure categories and subcategories

## 3. Import the app

1. Open `make.powerapps.com`
2. Go to `Apps`
3. Choose `Import canvas app`
4. Select the latest `.msapp` from [`app/releases`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/app/releases)

## 4. Reconnect data sources

Reconnect:
- SharePoint lists
- Office 365 Outlook

## 5. Smoke tests

1. Create a new evaluation
2. Confirm `AttendingEmail` is populated
3. Confirm “My Feedback List” only shows the current user’s records
4. Confirm PD/admin screens are restricted correctly
5. Confirm report emails send successfully
