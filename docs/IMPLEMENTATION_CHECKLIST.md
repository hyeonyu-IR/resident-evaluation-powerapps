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
- Import the preferred CSV starter files
- Verify key column names are correct after import
- Verify key column types are correct after import

## Power Apps Setup

- Import the latest `.msapp`
- Open the app in Power Apps Studio
- Reconnect all SharePoint data sources
- Reconnect the Outlook connector
- Resolve any broken data-source references

## Functional Validation

- Create a new feedback entry
- Confirm `AttendingEmail` is populated on save
- Confirm `My Feedback List` only shows the current user's records
- Confirm `My Feedback Report` only uses the current user's records
- Confirm procedure main/subcategory filtering works
- Confirm resident year and resident name filtering works
- Confirm report generation works
- Confirm PD/admin-only screens are protected

## Local Customization Review

- Review `AttendingRole` values for local leadership titles
- Review email sender and Outlook behavior
- Review whether score fields and comments match local evaluation policy
- Review whether local programs want additional resident metadata or procedure categories

## Go-Live Readiness

- Remove dummy feedback rows if they were used only for testing
- Replace dummy attending data with local attending data
- Replace dummy resident data with local resident data
- Re-run the smoke tests with real local accounts
- Document the local app owner and support contact
