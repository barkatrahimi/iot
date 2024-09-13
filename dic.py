data = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

mest_tid = 0  # project start
projekt_med_mest_tid = ""  

for projekt in data:
    if "Erik" in data[projekt]:
        timmar = data[projekt]["Erik"]
        if timmar > mest_tid:
            mest_tid = timmar
            projekt_med_mest_tid = projekt

# Skriv ut resultatet
print("Erik har jobbat mest på:", projekt_med_mest_tid, "med", mest_tid, "timmar.")


