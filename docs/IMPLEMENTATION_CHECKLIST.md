# Implementation Checklist

Use this checklist when standing up the app in a new institution.

## Pre-Implementation

- Confirm Power Apps and SharePoint access in the target Microsoft 365 tenant.
- Confirm who will own the SharePoint lists.
- Confirm who will maintain the Power Apps canvas app after import.
- Confirm whether the target site will use the exact expected SharePoint list names.

## SharePoint Setup

- Create `VIR_RealTime_FeedBack`
- Create `Procedure_Categories_01`
- Create `Resident_Year_Name_01`
- Create `AttendingList`
- Read [`MANUAL_SHAREPOINT_SCHEMA.md`](MANUAL_SHAREPOINT_SCHEMA.md)
- Manually create the schema for `VIR_RealTime_FeedBack`
- Manually create the schema for `AttendingList`
- Import only the resident dummy CSV if starter resident data is needed
- Verify key column names are correct after setup
- Verify key column types are correct after setup
- Confirm `AttendingEmail` is `Single line of text`
- Confirm `EmailAddress` is `Single line of text`

## Power Apps Setup

- Import the latest `.msapp` only after the SharePoint lists already exist
- Open the app in Power Apps Studio
- Expect a first-open prompt to connect SharePoint and Office 365 Outlook
- Reconnect all SharePoint data sources
- Reconnect the Outlook connector
- Resolve any broken data-source references

## Functional Validation

- Create a new feedback entry
- Confirm `AttendingEmail` is populated on save
- Confirm the saved row contains actual values, not an empty or partially empty record
- Confirm `My Feedback List` only shows the current user's records
- Confirm `My Feedback Report` only uses the current user's records
- Confirm procedure main/subcategory filtering works
- Confirm resident year and resident name filtering works
- Confirm report generation works
- Confirm stats chart labels are correct after reconnect
- Confirm PD/admin-only screens are protected

## Local Customization Review

- Review `AttendingRole` values for local leadership titles
- Review email sender and Outlook behavior
- Review whether score fields and comments match local evaluation policy
- Review whether local programs want additional resident metadata or procedure categories

## Go-Live Readiness

- Remove any locally created test feedback rows before production use
- Replace dummy attending data with local attending data
- Replace dummy resident data with local resident data
- Re-run the smoke tests with real local accounts
- Document the local app owner and support contact
