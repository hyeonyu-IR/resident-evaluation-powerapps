# Start Here

This page is for institutions that want to evaluate or implement this Power Apps resident-evaluation app.

## What You Need

- A Microsoft 365 environment with Power Apps access
- SharePoint Online
- Permission to create SharePoint lists and import a canvas app
- Someone who can reconnect data sources in Power Apps Studio

## Fastest Evaluation Path

If you want to assess whether this app is suitable for your program:
1. Review the latest `.msapp` in [`app/releases`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/app/releases).
2. Review the required SharePoint lists in [`docs/CONNECTION_MAP.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/CONNECTION_MAP.md).
3. Import the dummy CSV files from [`sharepoint-templates/dummy`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates/dummy).
4. Import the app and reconnect data sources.
5. Run the smoke tests in [`docs/IMPLEMENTATION_CHECKLIST.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/IMPLEMENTATION_CHECKLIST.md).

## Expected SharePoint Lists

Create these lists with these exact names:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

If your local SharePoint list names differ, expect to reconnect data sources and possibly update formulas.

## Which CSV Files Should You Use?

- Use [`sharepoint-templates/dummy`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates/dummy) if you want a realistic non-sensitive starter dataset.
- Use [`sharepoint-templates/template`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates/template) if you want only a minimal example row.
- Use [`sharepoint-templates/blank`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates/blank) only if you want to build the list contents from scratch.

## Recommended Reading Order

1. [`SETUP_GUIDE.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/SETUP_GUIDE.md)
2. [`CONNECTION_MAP.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/CONNECTION_MAP.md)
3. [`COMPREHENSIVE_MANUAL.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/COMPREHENSIVE_MANUAL.md)
4. [`IMPLEMENTATION_CHECKLIST.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/IMPLEMENTATION_CHECKLIST.md)
5. [`TROUBLESHOOTING.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/TROUBLESHOOTING.md)
6. [`USER_GUIDE.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/USER_GUIDE.md)

## Critical Adoption Notes

- The app uses `AttendingEmail` for record ownership and "My Feedback" filtering.
- PD/admin access is driven by `AttendingRole`.
- Procedure filtering depends on preserving the original main/subcategory structure.
- CSV filenames are not the same thing as SharePoint list names.

## Visual Walkthrough

If you want to see the user-facing workflow before implementation:
- [`USER_GUIDE.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/USER_GUIDE.md)
- [`Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/assets/Power_Apps_VIR_Resident_Evaluation_User_Guide.pdf)

## Comprehensive Manual

If you want a single downloadable step-by-step implementation document:
- [`COMPREHENSIVE_MANUAL.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/COMPREHENSIVE_MANUAL.md)
- [`Resident_Evaluation_Implementation_Manual.pdf`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/assets/Resident_Evaluation_Implementation_Manual.pdf)

## When You Should Customize

You should expect local customization if:
- your institution uses different list names
- your role names differ from `program director`, `pd`, `admin`, or similar values
- you want a Person column instead of text `AttendingEmail`
- you need branding, policy, or workflow changes
