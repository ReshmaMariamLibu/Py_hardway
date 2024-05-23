tabby_cat = "\tI'm tabbed in." # tab escape sequence (\t), which adds a tab space before the text
persian_cat = "I'm split\non a line." # string contains a newline escape sequence (\n), which breaks the line after "split."
backslash_cat = "I'm \\ a \\ cat." #  string contains a backslash escape sequence (\\),  allows to include a single backslash in the string.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

