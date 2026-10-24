# mini-camel-case-splitter

Splits PascalCase and camelCase identifiers into lowercase word tokens for readability or indexing.

```python
from mini_camel_case_splitter import split

split("camelCaseWords")    # ["camel", "case", "words"]
split("HTTPServer")        # ["http", "server"]
split("XMLHttpRequest")    # ["xml", "http", "request"]
split("file2Name")         # ["file", "2", "name"]
```

`split_camel_case` is an alias of `split` if you prefer the explicit name.

## Why

Tokenising identifiers is a common need for full-text indexes, diffing, and human-friendly
labels. The trade-off here is simplicity over configurability: there is exactly one
splitting strategy, no options, no dependency surface. If your identifiers use a
different convention you will want a different library rather than flags here.

## Edge cases

Acronyms are handled greedily: `HTTPServer` -> `["http", "server"]`, not `["h", "t",
"t", "p", "server"]`. Digits are treated as their own token when adjacent to letters
(`file2Name` -> `["file", "2", "name"]`). Non-alphanumeric characters (underscores,
dots, spaces) act as separators and are discarded. An empty string returns an empty list.
