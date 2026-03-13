# Release Workflow

## When you update the live app in Power Apps Studio

1. Save and publish the app in Power Apps Studio.
2. Export the newest version as `.msapp`.
3. Copy it into [`app/releases`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/app/releases) with a date-stamped name.
4. Optionally update `UNC_VIR_Resident_Evaluation.msapp` to the same latest export.
5. If you want source-level diffs, unpack the new `.msapp` and refresh [`_unpacked`](/c:/Users/hyeon/Documents/miniconda_medimg_env/ms-powerapps-projects/unc-vir-resident-evaluation/_unpacked).
6. Update docs if list schema, formulas, or setup steps changed.
7. Commit and tag the release in git.

## Suggested release naming

- `UNC_VIR_Resident_Evaluation_vYYYY-MM-DD.msapp`

## Suggested git tags

- `v1.0-initial-shareable`
- `v1.1-attending-email-filtering`
- `v1.2-pd-access-hardening`
