from extractor import extract_claims


article = """
Kenya's inflation rate fell to 4.5 percent in July 2026.
The government announced a new education funding program.
The president said the economy is doing very well.
"""


result = extract_claims(article)

print("Extracted Claims:")
print(result)