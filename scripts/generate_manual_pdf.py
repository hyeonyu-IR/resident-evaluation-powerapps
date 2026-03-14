from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "Resident_Evaluation_Implementation_Manual.pdf"
SCREENSHOTS = ROOT / "docs" / "screenshots"


def bullet_list(items, style, left_indent=18):
    return ListFlowable(
        [ListItem(Paragraph(item, style)) for item in items],
        bulletType="bullet",
        leftIndent=left_indent,
    )


def add_image(path, width_inches):
    img = Image(str(path))
    img._restrictSize(width_inches * inch, 6.6 * inch)
    return img


def section_title(text):
    return Paragraph(text, styles["ManualHeading"])


def body(text):
    return Paragraph(text, styles["ManualBody"])


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ManualTitle",
        parent=styles["Title"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0b3558"),
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="ManualHeading",
        parent=styles["Heading1"],
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#0b3558"),
        spaceBefore=10,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="ManualSubheading",
        parent=styles["Heading2"],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#114a78"),
        spaceBefore=8,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="ManualBody",
        parent=styles["BodyText"],
        fontSize=9.5,
        leading=13,
        spaceAfter=5,
    )
)

doc = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=letter,
    rightMargin=0.65 * inch,
    leftMargin=0.65 * inch,
    topMargin=0.65 * inch,
    bottomMargin=0.65 * inch,
)

story = []

story.append(Paragraph("Resident Evaluation App Implementation Manual", styles["ManualTitle"]))
story.append(
    body(
        "Step-by-step guidance for institutions adopting the Power Apps resident-evaluation app. "
        "This version is intended to work as a stronger standalone implementation document, not just a brief overview."
    )
)
story.append(Spacer(1, 0.12 * inch))

story.append(section_title("What This Manual Covers"))
story.append(
    bullet_list(
        [
            "What files to download from the repository",
            "How to create the required SharePoint lists",
            "Which list names, field names, and field types matter most",
            "How to import the app into Power Apps",
            "How to reconnect data sources and verify the deployment",
            "How ownership, PD/admin roles, and procedure filtering work",
            "How to validate the core user workflows before production use",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Required SharePoint Lists"))
story.append(
    bullet_list(
        [
            "VIR_RealTime_FeedBack",
            "Procedure_Categories_01",
            "Resident_Year_Name_01",
            "AttendingList",
        ],
        styles["ManualBody"],
    )
)
story.append(
    body(
        "These SharePoint list names should match exactly. CSV filenames are only import helpers. "
        "Power Apps connects to SharePoint list names and field names, so renaming lists or fields can break formulas and data binding."
    )
)

story.append(section_title("Recommended Files"))
story.append(
    bullet_list(
        [
            "Latest .msapp from app/releases or download-files",
            "dummy/AttendingList.dummy.csv",
            "dummy/Resident_Year_Name_01.dummy.csv",
            "dummy/Procedure_Categories_01.dummy.csv",
            "dummy/VIR_RealTime_FeedBack.dummy.csv",
        ],
        styles["ManualBody"],
    )
)
story.append(
    body(
        "The dummy CSV files are the recommended starter set because they are non-sensitive, internally compatible with the app, "
        "and useful for standing up a test deployment quickly. They should later be replaced with local institutional data."
    )
)
story.append(
    body(
        "For the simplest starting path, institutions should begin with the files in the repository's download-files folder."
    )
)

story.append(section_title("Critical Field Names"))
story.append(
    bullet_list(
        [
            "VIR_RealTime_FeedBack.AttendingEmail",
            "VIR_RealTime_FeedBack.ResidentYear",
            "VIR_RealTime_FeedBack.ResidentName",
            "VIR_RealTime_FeedBack.ProcedureMain",
            "VIR_RealTime_FeedBack.ProcedureSub",
            "VIR_RealTime_FeedBack.EvalDate",
            "AttendingList.AttendingName",
            "AttendingList.EmailAddress",
            "AttendingList.AttendingRole",
        ],
        styles["ManualBody"],
    )
)
story.append(
    body(
        "These names are important because the app formulas refer to them directly. "
        "If another institution changes them without updating the app, filtering, reports, dropdowns, or access logic can fail."
    )
)

story.append(section_title("Critical Field Types"))
story.append(
    bullet_list(
        [
            "EvalDate should be Date/Time",
            "AttendingEmail should remain Single line of text unless the app is intentionally changed to use a Person column",
            "Score-related fields should remain numeric if local teams want numeric calculations and sorting",
            "Comment fields should allow enough text for narrative feedback",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Implementation Steps"))
story.append(
    bullet_list(
        [
            "Review the expected schema before importing data",
            "Create the four SharePoint lists with exact names",
            "Import the recommended CSV starter files",
            "Verify key SharePoint column names and types",
            "Import the canvas app from the latest .msapp file",
            "Reconnect SharePoint and Outlook data sources in Power Apps Studio",
            "Run smoke tests before production use",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Reconnect Workflow"))
story.append(
    bullet_list(
        [
            "Open the imported app in Power Apps Studio",
            "Go to Data",
            "Remove broken or unresolved SharePoint connections if present",
            "Add the four local SharePoint lists with the expected names",
            "Reconnect the Office 365 Outlook connector",
            "Confirm that formulas resolve without data-source errors",
        ],
        styles["ManualBody"],
    )
)
story.append(
    body(
        "If the target institution created differently named SharePoint lists, reconnecting alone may not be enough. "
        "Formula updates may still be required."
    )
)

story.append(PageBreak())
story.append(section_title("Role and Ownership Behavior"))
story.append(
    bullet_list(
        [
            "Ownership-based views depend on AttendingEmail",
            "My Feedback List and My Feedback Report are expected to use the current user's email-based ownership",
            "PD/admin-only screens depend on AttendingRole values in AttendingList",
            "If local leadership titles differ, role mapping should be reviewed before go-live",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Procedure Filtering Dependency"))
story.append(
    body(
        "Procedure filtering is one of the more sensitive parts of the app. "
        "The main/subcategory dropdown behavior depends on preserving the original structure in Procedure_Categories_01."
    )
)
story.append(
    bullet_list(
        [
            "The app expects a main category field in Procedure_Categories_01.Title",
            "Subcategory relationships should remain consistent with the provided CSV files",
            "If the target institution changes the procedure taxonomy casually, dependent dropdown behavior can break",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Visual Workflow Overview"))
story.append(
    body(
        "The screenshots below summarize the most important user-facing parts of the app. "
        "These are helpful for validating whether the imported app is behaving as expected."
    )
)

for title, filename in [
    ("Home Screen Overview", "home-screen-overview.png"),
    ("Entering New Feedback", "entering-feedback.png"),
    ("My Summary Report", "my-summary-report.png"),
    ("All-Attending Report", "all-attending-report.png"),
    ("Stats Screen", "stats-screen.png"),
]:
    story.append(Paragraph(title, styles["ManualSubheading"]))
    story.append(add_image(SCREENSHOTS / filename, 7.0))
    story.append(Spacer(1, 0.1 * inch))

story.append(PageBreak())
story.append(section_title("Validation Checklist"))
story.append(
    bullet_list(
        [
            "Create a new evaluation and confirm AttendingEmail saves correctly",
            "Confirm My Feedback List only shows the current user's records",
            "Confirm My Feedback Report only uses the current user's records",
            "Confirm PD/admin-only views are protected",
            "Confirm procedure main-category and subcategory filtering work",
            "Confirm resident year and resident name filtering work",
            "Confirm report generation works",
            "Confirm report email delivery works in the local tenant",
            "Confirm existing imported dummy rows open without schema or binding errors",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Common Failure Modes"))
story.append(
    bullet_list(
        [
            "List names differ from what the app expects",
            "Field names differ from what the formulas expect",
            "AttendingEmail is missing or blank on imported data",
            "Procedure category structure was changed or renamed",
            "AttendingRole values do not match local leadership mapping",
            "Data sources were not reconnected after import",
            "SharePoint inferred incorrect field types from CSV import",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("Go-Live Guidance"))
story.append(
    bullet_list(
        [
            "Replace dummy attending and resident data with local data",
            "Replace dummy feedback rows if they were used only for testing",
            "Re-run the smoke tests using real local accounts",
            "Document the local app owner and SharePoint owner",
            "Document who will maintain AttendingRole mappings",
            "Keep GitHub as the primary distribution and documentation source",
        ],
        styles["ManualBody"],
    )
)

story.append(section_title("What This Manual Does Not Replace"))
story.append(
    body(
        "This PDF is intended to stand on its own reasonably well, but the repository still contains deeper reference material. "
        "If a local team encounters schema drift, role-mapping differences, or custom workflow needs, they should also consult the "
        "connection map, troubleshooting notes, and user guide in the repository."
    )
)

story.append(section_title("Questions That May Still Require Local Review"))
story.append(
    bullet_list(
        [
            "Local role naming and leadership-title mapping",
            "SharePoint governance constraints in the target tenant",
            "Whether to keep AttendingEmail as text or convert it to a Person column",
            "Whether local programs want custom procedure categories or evaluation fields",
        ],
        styles["ManualBody"],
    )
)

doc.build(story)
print(OUTPUT)
