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


def bullet_list(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style)) for item in items],
        bulletType="bullet",
        leftIndent=18,
    )


def add_image(path, width_inches):
    img = Image(str(path))
    img._restrictSize(width_inches * inch, 6.5 * inch)
    return img


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ManualTitle",
        parent=styles["Title"],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0b3558"),
        spaceAfter=16,
    )
)
styles.add(
    ParagraphStyle(
        name="ManualHeading",
        parent=styles["Heading1"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#0b3558"),
        spaceBefore=10,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="ManualBody",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
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
    Paragraph(
        "Step-by-step guidance for institutions adopting the Power Apps resident-evaluation app.",
        styles["ManualBody"],
    )
)
story.append(Spacer(1, 0.15 * inch))
story.append(Paragraph("What This Manual Covers", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "What files to download from the repository",
            "How to create the required SharePoint lists",
            "How to import the app into Power Apps",
            "How to reconnect data sources and verify the deployment",
            "How to validate the core user workflows",
        ],
        styles["ManualBody"],
    )
)

story.append(Paragraph("Required SharePoint Lists", styles["ManualHeading"]))
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
    Paragraph(
        "These list names should match exactly. CSV filenames are import helpers, but Power Apps connects to SharePoint list names and field names.",
        styles["ManualBody"],
    )
)

story.append(Paragraph("Recommended Files", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "Latest .msapp from app/releases",
            "dummy/AttendingList.dummy.csv",
            "dummy/Resident_Year_Name_01.dummy.csv",
            "dummy/Procedure_Categories_01.dummy.csv",
            "dummy/VIR_RealTime_FeedBack.dummy.csv",
        ],
        styles["ManualBody"],
    )
)

story.append(Paragraph("Implementation Steps", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "Review the expected schema before importing data",
            "Create the four SharePoint lists with exact names",
            "Import the recommended CSV starter files",
            "Verify key SharePoint column types such as EvalDate and AttendingEmail",
            "Import the canvas app from the latest .msapp file",
            "Reconnect SharePoint and Outlook data sources in Power Apps Studio",
            "Run smoke tests before production use",
        ],
        styles["ManualBody"],
    )
)

story.append(PageBreak())
story.append(Paragraph("Visual Workflow Overview", styles["ManualHeading"]))
story.append(
    Paragraph(
        "The screenshots below summarize the most important user-facing parts of the app.",
        styles["ManualBody"],
    )
)

for title, filename in [
    ("Home Screen Overview", "home-screen-overview.png"),
    ("Entering New Feedback", "entering-feedback.png"),
    ("My Summary Report", "my-summary-report.png"),
    ("All-Attending Report", "all-attending-report.png"),
    ("Stats Screen", "stats-screen.png"),
]:
    story.append(Paragraph(title, styles["ManualHeading"]))
    story.append(add_image(SCREENSHOTS / filename, 7.0))
    story.append(Spacer(1, 0.15 * inch))

story.append(PageBreak())
story.append(Paragraph("Validation Checklist", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "Create a new evaluation and confirm AttendingEmail saves correctly",
            "Confirm My Feedback List only shows the current user's records",
            "Confirm My Feedback Report only uses the current user's records",
            "Confirm PD and admin-only views are protected",
            "Confirm procedure filtering and resident filtering work",
            "Confirm report generation and email delivery work in the local tenant",
        ],
        styles["ManualBody"],
    )
)

story.append(Paragraph("Common Failure Modes", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "List names differ from what the app expects",
            "Column names differ from what the formulas expect",
            "AttendingEmail is missing or blank",
            "Procedure category structure was changed",
            "AttendingRole values do not match local leadership mapping",
            "Data sources were not reconnected after import",
        ],
        styles["ManualBody"],
    )
)

story.append(Paragraph("Go-Live Guidance", styles["ManualHeading"]))
story.append(
    bullet_list(
        [
            "Replace dummy attending and resident data with local data",
            "Remove dummy feedback rows if they were used only for testing",
            "Re-run the smoke tests using local accounts",
            "Document the local app owner and SharePoint owner",
            "Keep GitHub as the primary distribution and documentation source",
        ],
        styles["ManualBody"],
    )
)

doc.build(story)
print(OUTPUT)
