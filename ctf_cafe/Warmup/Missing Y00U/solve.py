from urllib.parse import unquote

string_input = "%u52%u55%u53%u48%u7B%u57%u48%u41%u54%u49%u53%u43%u4F%u44%u45%u42%u41%u42%u59%u44%u4F%u4E%u54%u48%u55%u52%u54%u4D%u45%u44%u4F%u4E%u54%u48%u55%u52%u54%u4D%u45%u4E%u4F%u4D%u4F%u52%u45%u7D%u0A%u0A"
string_filter = string_input.replace("%u", " ")
string_decoded = unquote(string_filter)
string_bytes = bytes.fromhex(string_decoded.replace(" ", ""))
string_text = string_bytes.decode("utf-8")

print(string_text)
## flag is RUSH{WHATISCODEBABYDONTHURTMEDONTHURTMENOMORE}
