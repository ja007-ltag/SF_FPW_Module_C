print("Hello world!")
# Интересный шрифт 🅰️🅻🅴🆇🅴🆈

text = "🅰️🅻🅴🆇🅴🆈"

for char in text:
    print(f"{char}: {ord(char)}")
print(text)

for num in range(127344, 127344+26):
    const = 65039
    # print(f"{num}: {chr(num)}")
    print(f"{num}+{const}: {chr(num)}{chr(const)}", f"{num}: {chr(num)}")
