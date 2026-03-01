# You're building a report generator for a logistics company.
#
# Starting from 1, print only odd-numbered shipment IDs up to 20.
# Even-numbered IDs should be skipped entirely.
# Each line should read: "Shipment #[number] dispatched."

shipment_id = 0

while shipment_id < 20:
    shipment_id = shipment_id + 1
    if shipment_id % 2 == 0:
        continue
    else:
        print(f"Shipment ID: {shipment_id}")