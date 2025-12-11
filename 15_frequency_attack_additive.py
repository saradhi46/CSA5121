# Program 15: Frequency Attack on Additive Cipher
def frequency_attack_additive():
    print("=== Frequency Attack on Additive Cipher ===")
    ciphertext = input("Enter ciphertext: ").upper()
    
    results = []
    for shift in range(26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted += char
        results.append((shift, decrypted))
    
    num_results = int(input("How many top results? (default 10): ") or "10")
    
    print(f"\nTop {num_results} possible plaintexts:")
    for i in range(min(num_results, 26)):
        print(f"\n{i+1}. Shift {results[i][0]}:")
        print(results[i][1][:80])

if __name__ == "__main__":
    frequency_attack_additive()

OUTPUT:Enter ciphertext: HELLO
How many top results? (default 10): 10

Top 10 possible plaintexts:

1. Shift 0:
HELLO

2. Shift 1:
GDKKN

3. Shift 2:
FCJJM

4. Shift 3:
EBIIL

5. Shift 4:
DAHHK

6. Shift 5:
CZGGJ

7. Shift 6:
BYFFI

8. Shift 7:
AXEEH

9. Shift 8:
ZWDDG

10. Shift 9:
YVCCF
