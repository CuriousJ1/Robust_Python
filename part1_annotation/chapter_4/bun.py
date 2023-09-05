def dispense_bun() -> Bun:
    return Bun('Wheat')


def dispense_bun() -> Bun:
    if not are_buns_available():
        return None
    return Bun('Wheat')

