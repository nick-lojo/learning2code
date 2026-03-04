# You're building a cargo manifest tool for a shipping company.
#
# Write a tool that accepts a container ID and destination port,
# then prints a shipping confirmation.
# Ship one container to Rotterdam and one to Singapore.

def cargo_manifesto(container_id, destination_port):
    """Prints shipping confirmation for a container."""
    print(f"Container #{container_id} has been shipped to {destination_port.title()}.")

cargo_manifesto(123, 'rotterdam')
cargo_manifesto(456, 'singapore')