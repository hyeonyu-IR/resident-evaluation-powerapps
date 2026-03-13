# UNC VIR Resident Evaluation

Canvas app for resident evaluation built in Microsoft Power Apps with SharePoint-backed data sources.

## Repository layout

- [`app/releases`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/app/releases)
  - distributable `.msapp` exports for import into Power Apps
- [`_unpacked`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/_unpacked)
  - unpacked app source for review and diffing
- [`sharepoint-templates`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/sharepoint-templates)
  - CSV templates for required SharePoint lists
- [`docs`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs)
  - setup, deployment, and maintenance documentation
- [`deployment-package`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/deployment-package)
  - ready-to-share handoff bundle

## Required Microsoft 365 dependencies

- SharePoint Online
- Office 365 Outlook connector

Required SharePoint lists:
- `VIR_RealTime_FeedBack`
- `Procedure_Categories_01`
- `Resident_Year_Name_01`
- `AttendingList`

## Recommended workflow

1. Make app changes in Power Apps Studio.
2. Save and publish.
3. Export the latest `.msapp`.
4. Add a date-stamped release artifact in `app/releases`.
5. Optionally update the canonical `UNC_VIR_Resident_Evaluation.msapp` file to the same latest export.
6. If needed, unpack the latest `.msapp` and refresh `_unpacked`.
7. Update docs or templates when schema or deployment steps change.
8. Commit to git and push to GitHub.

Repository asset rules:
- track the latest importable app in [`app/releases`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/app/releases)
- track unpacked source in [`_unpacked`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/_unpacked)
- do not rely on [`Microsoft.PowerApps`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/Microsoft.PowerApps) as the long-term Git artifact
- treat [`deployment-package`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/deployment-package) as generated handoff material

## Sharing with another institution

Use the deployment package and setup docs:
- [`docs/SETUP_GUIDE.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/SETUP_GUIDE.md)
- [`docs/CONNECTION_MAP.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/CONNECTION_MAP.md)
- [`docs/REPOSITORY_POLICY.md`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/docs/REPOSITORY_POLICY.md)

Do not share production data unless you explicitly intend to disclose it.

## Notes

- The app relies on `AttendingEmail` for stable ownership filtering.
- `AttendingRole` in `AttendingList` controls PD/admin access.
- The current formulas use `Procedure_Categories_01.Title` as the main category field.
