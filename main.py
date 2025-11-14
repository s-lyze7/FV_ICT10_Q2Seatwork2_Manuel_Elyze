from pyscript import document, display

subjects = ["science", "math", "english", "filipino", "ict", "pe"]

def general_weighted_average(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    try:
        science = float(document.getElementById('science').value)
        math = float(document.getElementById('math').value)
        english = float(document.getElementById('english').value)
        filipino = float(document.getElementById('filipino').value)
        ict = float(document.getElementById('ict').value)
        pe = float(document.getElementById('pe').value)
    except ValueError:
        document.getElementById("gwa").innerText = "Fill in all the blanks"
        return

    if not first_name or not last_name:
        document.getElementById("gwa").innerText = "Fill in all the blanks"
        return
    
    weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
    total_units = 5 + 5 + 5 + 3 + 2 + 1
    gwa = weighted_sum / total_units

    summary = f""" {subjects[0]}: {science}
{subjects[1]}: {math}
{subjects[2]}: {english}
{subjects[3]}: {filipino}
{subjects[4]}: {ict}
{subjects[5]}: {pe}
"""

    display(f'Name: {first_name} {last_name}', target='student_info')
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
