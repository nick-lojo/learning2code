def appointment_booker(first_name, last_name, appointment_time):
    """Patients can use this to schedule their appointments at a hospital."""
    full_name = f"{first_name} {last_name}"
    print(f"Hello {full_name.title()}, your appointment has successfully been scheduled for {appointment_time}.")