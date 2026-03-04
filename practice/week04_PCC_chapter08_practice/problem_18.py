# You're building a task logger for a project management tool.
#
# A list of pending tasks needs to be processed and moved to a completed list.
# Write two functions — one to process the tasks, one to display them.
# Call both from the main script.

def task_logger(pending, completed):
    """Processes a list of pending tasks and moves them to a completed list."""
    while pending:
        processing = pending.pop()
        print(f"Processing {processing}...")
        completed.append(processing)

def show_completed(completed):
    print(f"\nCompleted Tasks:")
    for task in completed:
        print(f"\t{task}")

pending_tasks = ['complete rfp', 'negotiate budget', 'define success',
                 'sign agreement']
completed_tasks = []

task_logger(pending_tasks, completed_tasks)
show_completed(completed_tasks)