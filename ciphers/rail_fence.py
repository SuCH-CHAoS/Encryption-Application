def _normalize_rails(rails):
    rails = int(rails)
    if rails < 1:
        raise ValueError("Rails must be at least 1.")
    return rails


def _rail_pattern(length, rails):
    if rails == 1:
        return [0] * length

    pattern = []
    rail = 0
    direction = 1

    for _ in range(length):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    return pattern


def encrypt(text, rails):
    rails = _normalize_rails(rails)
    if rails == 1 or rails >= len(text):
        return text

    rows = [[] for _ in range(rails)]
    for char, rail in zip(text, _rail_pattern(len(text), rails)):
        rows[rail].append(char)

    return "".join("".join(row) for row in rows)


def decrypt(text, rails):
    rails = _normalize_rails(rails)
    if rails == 1 or rails >= len(text):
        return text

    pattern = _rail_pattern(len(text), rails)
    counts = [pattern.count(rail) for rail in range(rails)]

    rows = []
    start = 0
    for count in counts:
        rows.append(list(text[start:start + count]))
        start += count

    positions = [0] * rails
    result = []

    for rail in pattern:
        result.append(rows[rail][positions[rail]])
        positions[rail] += 1

    return "".join(result)
