# You're building a pet registration tool for a vet clinic.
#
# Write a tool that accepts a pet's species and name, then prints a
# registration confirmation.
# Register a dog named Rex and a cat named Luna.

def pet_registration(species, name):
    """Pet registrationt tool for a vet that intakes a pet's species and name."""
    print("\nRegistering Pet...")
    print(f"\tPet Name: {name.title()}")
    print(f"\tSpecies: {species}")

pet_registration('dog', 'rex')
pet_registration('cat', 'luna')