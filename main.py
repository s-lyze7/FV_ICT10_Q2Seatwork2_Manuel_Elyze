from pyscript import document

subject_fields = [
    ("gensci", "GenSci"),
    ("genmath", "GenMath"),
    ("effcom", "EFFCOM"),
    ("pklp", "PKLP"),
    ("arts", "Arts1"),
    ("filid", "FILID"),
    ("ff1", "FF1"),
    ("lcs", "LCS"),
]

def general_weighted_average(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    output = document.getElementById("output")
    student_info = document.getElementById("student_info")
    summary_el = document.getElementById("summary")

    student_info.innerText = ""
    summary_el.innerText = ""
    output.innerText = ""

    if not first_name or not last_name:
        output.innerText = "Fill in all the blanks."
        return

    grades = {}
    try:
        for field_id, _ in subject_fields:
            grades[field_id] = float(document.getElementById(field_id).value)
    except ValueError:
        output.innerText = "Fill in all the blanks with valid numbers."
        return

    summary_lines = [f"{label}: {grades[field_id]}" for field_id, label in subject_fields]
    summary_el.innerText = "\n".join(summary_lines)

    weighted_sum = sum(grade * 4 for grade in grades.values())
    total_units = 4 * len(grades)
    gwa = weighted_sum / total_units

    student_info.innerText = f"Name: {first_name} {last_name}"
    output.innerText = f"Your general weighted average is {gwa:.2f}"
