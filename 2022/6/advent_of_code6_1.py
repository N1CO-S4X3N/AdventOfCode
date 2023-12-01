with open(r'I:\Documents\PythonPrograms\AdventOfCode\6\items.txt', 'r', encoding='utf-8') as file:
    signal = file.read()
for i, char in enumerate(signal):
    marker = signal[i:i+4]
    if len(set(marker)) == 4:
        print("correct: ", marker)
        print("after char: ", i+4)
        break
