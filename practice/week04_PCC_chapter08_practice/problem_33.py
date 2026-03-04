# You're building a work order tool for a facilities management company.
#
# Write a tool that accepts a technician's name and the job type,
# then returns a formatted work order.
# Keep accepting new work orders until the dispatcher is done.

def format_work_order(name, job_type):
    """Intakes a tech's name and job type, formats the work order."""
    work_order = f"\nTechnician Name: {name.title()}"
    work_order += f"\nJob Type: {job_type}"
    return work_order

while True:
    print(f"\nPlease enter your name and the job type you are completing.")
    print(f"Enter 'q' at any time to stop collecting input.")

    tech_name = input("\nPlease enter your name: ")
    if tech_name == 'q':
        break
    job = input("Please enter the job type assigned to you: ")
    if job == 'q':
        break

    order = format_work_order(tech_name, job)
    print(order)