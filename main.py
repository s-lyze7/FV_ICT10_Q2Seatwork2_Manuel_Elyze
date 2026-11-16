from pyscript import document, display

subjects = ["gensci", "genmath", "effcom", "pklp", "ff1", "arts", "filid", "lcs"]

def general_weighted_average(e):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    try:
        gensci = float(document.getElementById('gensci').value)
        genmath = float(document.getElementById('genmath').value)
        effcom = float(document.getElementById('effcom').value)
        pklp = float(document.getElementById('pklp').value)
        ff1 = float(document.getElementById('ff1').value)
        arts = float(document.getElementById('arts').value)
        filid = float(document.getElementById('filid').value)
        lcs = float(document.getElementById('lcs').value)

    except ValueError:
        document.getElementById("gwa").innerText = "Fill in all the blanks"
        return

    if not first_name or not last_name:
        document.getElementById("gwa").innerText = "Fill in all the blanks"
        return
    
    weighted_sum = (gensci * 4 + genmath * 4 + effcom * 4 + pklp * 4 + ff1 * 4 + arts * 4 + filid * 4 + lcs * 4)
    total_units = 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4
    gwa = weighted_sum / total_units

    summary = f""" {subjects[0]}: {science}
{subjects[1]}: {gensci}
{subjects[2]}: {genmath}
{subjects[3]}: {effcom}
{subjects[4]}: {pklp}
{subjects[5]}: {arts}
{subjects[6]}: {filid}
{subjects[7]}: {ff1}
{subjects[8]}: {lcs}
"""

    display(f'Name: {first_name} {last_name}', target='student_info')
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')
