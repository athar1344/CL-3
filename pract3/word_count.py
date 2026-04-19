from collections import Counter

with open("input.txt", "r") as f:
    text = f.read().lower()

# Mapper phase
print("MAPPER OUTPUT")
print("=" * 30)
mapped = []
for word in text.split():
    print(f"{word}\t1")
    mapped.append(word)

# Reducer phase
print("\nREDUCER OUTPUT (Final Count)")
print("=" * 30)
word_count = Counter(mapped)
for word, count in sorted(word_count.items()):
    print(f"{word}\t{count}")