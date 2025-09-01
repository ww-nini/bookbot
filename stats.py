def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_num_chars(text: str) -> dict[str, int]:
    map = {}
    for char in text:
        c = char.lower()
        map[c] = map.get(c, 0) + 1
    return map


def transform_num_chars_dict(map: dict[str, int]) -> list[dict]:
    l = []
    for k, v in map.items():
        l.append({"char": k, "num": v})
    l.sort(reverse=True, key=lambda x: x["num"])
    return l
