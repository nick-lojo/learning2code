# You're building a print queue tool for a document management system.
#
# A list of documents is waiting to be printed.
# Process each document from the queue and move it to a completed list.
# When the queue is empty, display all completed documents.

def print_documents(queue, completed):
    """Processes documents from a queue to be printed, and moves them to a
    completed list."""
    while queue:
        processed = queue.pop()
        print(f"Processing {processed}...")
        completed.append(processed)

def completion_check(completed):
    print("\nPrinted Documents:")
    for document in completed:
        print(f"\t{document}")

document_queue = ['doc_0', 'doc_1', 'doc_2', 'doc_3']
completed_docs = []

print_documents(document_queue, completed_docs)
completion_check(completed_docs)