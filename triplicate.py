first = input()
second = input()
third = input()
if first == second == third:
    print("OK")
elif first != second and first != third:
    print("BOTH MISMATCH")
elif first == third and second != first:
    print("ENTRY 2 MISMATCH")
elif first == second and first != third:
    print("ENTRY 3 MISMATCH")
