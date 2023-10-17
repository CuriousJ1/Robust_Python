class Person:
    name: str = ""
    years_experience: int = 0
    address: str = ""

pat = Person()
pat.name = "Pat"

print(f"Hello {pat.name}")
print(f"Years of Experience {pat.years_experience}")
print(f"Address {pat.address}")