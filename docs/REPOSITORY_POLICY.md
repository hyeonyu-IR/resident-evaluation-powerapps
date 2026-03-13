# Repository Policy

This repository should keep the smallest durable set of artifacts needed for:
- version control
- deployment handoff
- source review

## Keep in Git

- `README.md`
- `CHANGELOG.md`
- `docs/`
- `sharepoint-templates/`
- `app/releases/`
- `_unpacked/`

Recommended focus inside `_unpacked/`:
- `Src/`
- `References/`
- `AppCheckerResult.sarif`
- `Header.json`
- `Properties.json`

Usually exclude from Git inside `_unpacked/`:
- `Assets/`
- `Controls/`
- `Resources/`

## Usually do not keep in Git

- `deployment-package.zip`
- `deployment-package/`
- `Microsoft.PowerApps/`
- one-off exported package metadata copies
- local scratch files

## Rationale

- `app/releases/` gives a ready-to-import `.msapp`
- `_unpacked/` gives reviewable source for diffs and pull requests
- `deployment-package/` is generated handoff material and can be rebuilt from repo contents
- `Microsoft.PowerApps/` is the raw package container from export and is redundant once the `.msapp` is stored in `app/releases/`

## Recommended release routine

1. Export the newest `.msapp` from Power Apps Studio
2. Replace the file in `app/releases/`
3. Refresh `_unpacked/` from that same export if you want source-level diff history
4. Update docs/templates if schema or setup changed
5. Commit and tag the release

## Privacy rule

Do not commit real institutional resident, attending, or evaluation data.
Only commit schema templates, sample rows, and documentation unless disclosure is intentional and approved.
