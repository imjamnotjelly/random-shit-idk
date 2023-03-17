with open("day1.txt", "r") as f:
    elfs = f.read().replace("\n", " ").split("  ")
    elf_sums = [sum([int(v) for v in e.split()]) for e in elfs]
    print(max(elf_sums))