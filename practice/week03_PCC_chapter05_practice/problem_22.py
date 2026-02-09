available_tables = [1, 2, 3, 5, 7, 8, 10, 12]
reservation_requests = [2, 4, 7, 9, 10]

for table in reservation_requests:
    if table in available_tables:
        print(f'Table {table} is available. Reservation confirmed.')
    else:
        print(f'Sorry, table {table} is not available.')