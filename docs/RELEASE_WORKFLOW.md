# Release Workflow

## When you update the live app in Power Apps Studio

1. Save and publish the app in Power Apps Studio.
2. Export the newest version as `.msapp`.
3. Replace [`UNC_VIR_Resident_Evaluation.msapp`](../app/releases/UNC_VIR_Resident_Evaluation.msapp) in [`app/releases`](../app/releases) with the newest export.
4. If you want source-level diffs, unpack the new `.msapp` and refresh [`_unpacked`](../_unpacked).
5. Update docs if list schema, formulas, or setup steps changed.
6. Commit and tag the release in git.

## Manual workflow

1. Edit [`Resident_Evaluation_Implementation_Manual.docx`](assets/Resident_Evaluation_Implementation_Manual.docx) as the master manual.
2. Export/update [`Resident_Evaluation_Implementation_Guide_Published.pdf`](assets/Resident_Evaluation_Implementation_Guide_Published.pdf) from Word.
3. Update [`10_COMPREHENSIVE_MANUAL.md`](10_COMPREHENSIVE_MANUAL.md) only if you want the Markdown reference to stay aligned.
4. Commit the `.docx` and `.pdf` together so they remain in sync.

## Suggested git tags

- `v1.0-initial-shareable`
- `v1.1-attending-email-filtering`
- `v1.2-pd-access-hardening`

