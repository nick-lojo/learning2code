# You're building a records tool for a law firm.
#
# A list of case files needs to be archived, but the original list
# must remain intact after processing.
# Process each file into an archived list.
# After processing, confirm both lists still have their contents.

def process_files(queue, archived):
    """Processes files from a queue and moves them to an archive."""
    while queue:
        processed = queue.pop()
        print(f"Archiving copy of {processed}...")
        archived.append(processed)

def archive_files(archived):
    """Prints the files from the queue that are now in the archived list."""
    print("\nThe following file copies have now been archived:")
    for file in archived:
        print(f"\t{file}")

case_files = ['file_0', 'file_1', 'file_2', 'file_3']
archived_files = []

process_files(case_files[:], archived_files)
archive_files(archived_files)

print(case_files)