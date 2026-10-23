"""CamelCase / PascalCase splitting into lowercase word tokens."""


import re


_BOUNDARY_RE = re.compile(
    r"(?<=[a-z0-9])(?=[A-Z])"        # aLower -> Upper
    r"|(?<=[0-9])(?=[A-Za-z])"       # digit -> letter
    r"|(?<=[A-Za-z])(?=[0-9])"      # letter -> digit
    r"|(?<=[A-Z])(?=[A-Z][a-z])"    # ALLCaps -> UpperLower
)


def split(identifier):
    """Split a camelCase / PascalCase identifier into lowercase word tokens.

    Decisions baked in (one interpretation, chosen deliberately):
      * Acronyms are handled greedily: a run of uppercase letters is kept
        together until the last one, which starts the next word if it is
        followed by a lowercase letter. "HTTPServer" -> ["http", "server"];
        "XMLHttpRequest" -> ["xml", "http", "request"].
      * Digits form their own token when adjacent to letters, so "file2Name"
        becomes ["file", "2", "name"] rather than ["file2", "name"].
      * Non-alphanumeric characters (spaces, underscores, dots) are treated
        as separators themselves and also split adjacent letters/digits, so
        "foo_bar" yields ["foo", "bar"].
      * An empty or all-separator input returns an empty list.
      * Results are lowercased.
    """
    if not isinstance(identifier, str):
        raise TypeError("identifier must be a str")
    if not identifier:
        return []
    parts = _BOUNDARY_RE.split(identifier)
    tokens = []
    for part in parts:
        if not part:
            continue
        sub = re.split(r"[^0-9A-Za-z]+", part)
        for piece in sub:
            if piece:
                tokens.append(piece.lower())
    return tokens


def split_camel_case(identifier):
    """Alias of :func:`split` for callers that prefer an explicit name."""
    return split(identifier)
