# profile.py

class FakePatientRam:
    def __init__(self):
        self.name = "Ram"
        self.dob = "1999-01-10"
        self.height_cm = 172
        self.weight_kg = 68
        self.allergies = ["Penicillin"]
        self.conditions = ["Borderline Hypertension"]
        self.meds = [
            {"time": "08:00 AM", "name": "Metformin", "dose": "500mg", "with_food": True},
            {"time": "08:30 PM", "name": "Vitamin D3", "dose": "1000 IU", "with_food": False},
        ]
        self.appointments = [
            {"date": "2025-09-10", "time": "10:30 AM", "doctor": "Dr. Meera N", "purpose": "BP & Labs", "location": "CloudCare Clinic, Indiranagar"}
        ]

    def get_schedule(self):
        lines = [f"{m['time']} → {m['name']} {m['dose']}" for m in self.meds]
        lines += [f"{a['date']} {a['time']} → {a['doctor']} ({a['purpose']}) at {a['location']}" for a in self.appointments]
        return "\n".join(lines)
