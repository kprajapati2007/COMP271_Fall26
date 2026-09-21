from __future__ import annotations
from typing import Any
import math


# ============================================================
#                 ModularInteger Class
# ============================================================

class ModularInteger:
    """
    Represents integer value in modular arithmetic.
    Stores normalized value 0 <= value < modulus.
    Supports addition, multiplication, exponentiation,
    equality, string formatting, and RSA-related helpers.
    """

    CLOCK_MODULUS = 12

    def __init__(self, value: int, modulus: int):
        """
        Initialize ModularInteger with given value and modulus.
        Normalizes value into range [0, modulus).
        Raises ValueError if modulus <= 1.
        """
        if modulus <= 1:
            raise ValueError("Modulus must be greater than 1.")

        self.__modulus = modulus
        self.__value = value % modulus

    @property
    def value(self) -> int:
        """Return normalized value."""
        return self.__value

    @property
    def modulus(self) -> int:
        """Return modulus."""
        return self.__modulus

    def __str__(self) -> str:
        """Return string representation: 'value (mod modulus)'."""
        return f"{self.__value} (mod {self.__modulus})"

    def __eq__(self, other: Any) -> bool:
        """
        Two ModularInteger objects are equal only if:
        - same modulus
        - same normalized value
        If other isn't ModularInteger, return NotImplemented.
        """
        if not isinstance(other, ModularInteger):
            return NotImplemented
        return self.__value == other.__value and self.__modulus == other.__modulus

    def __add__(self, other: ModularInteger) -> ModularInteger:
        """
        Add two ModularInteger objects.
        Must have same modulus.
        Returns new ModularInteger.
        """
        if self.__modulus != other.__modulus:
            raise ValueError("Can't add values with different moduli.")
        return ModularInteger(self.__value + other.__value, self.__modulus)

    def __mul__(self, other: ModularInteger) -> ModularInteger:
        """
        Multiply two ModularInteger objects.
        Must have same modulus.
        Returns new ModularInteger.
        """
        if self.__modulus != other.__modulus:
            raise ValueError("Can't multiply values with different moduli.")
        return ModularInteger(self.__value * other.__value, self.__modulus)

    def __pow__(self, exponent: int) -> ModularInteger:
        """
        Raise ModularInteger to nonnegative integer exponent.
        Uses pow(value, exponent, modulus) for efficiency.
        Returns new ModularInteger.
        """
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Exponent must be nonnegative integer.")
        return ModularInteger(pow(self.__value, exponent, self.__modulus), self.__modulus)

    @classmethod
    def from_clock(cls, hour: int) -> ModularInteger:
        """
        Alternative constructor using CLOCK_MODULUS (12).
        Represents hour on a 12-hour clock.
        """
        return cls(hour, cls.CLOCK_MODULUS)

    @staticmethod
    def are_coprime(a: int, b: int) -> bool:
        """
        Return True if gcd(a, b) == 1, else False.
        """
        return math.gcd(a, b) == 1


# ============================================================
#                 RSAEncryptor Class
# ============================================================

class RSAEncryptor:
    """
    Educational RSA demonstration using fixed small primes.
    Not secure — for teaching only.
    """

    P = 61
    Q = 53
    E = 17
    D = 2753
    N = P * Q
    PHI = (P - 1) * (Q - 1)

    @classmethod
    def encrypt(cls, ch: str) -> ModularInteger:
        """
        Encrypt a single character using RSA:
        encrypted = message^E mod N
        Returns a ModularInteger.
        Raises ValueError if:
        - input is not exactly one character
        - ord(ch) >= N
        """
        if len(ch) != 1:
            raise ValueError("encrypt() requires exactly one character.")

        m = ord(ch)
        if m >= cls.N:
            raise ValueError("Character value too large for RSA modulus.")

        m_mod = ModularInteger(m, cls.N)
        encrypted = m_mod ** cls.E
        return encrypted

    @classmethod
    def decrypt(cls, encrypted: ModularInteger) -> str:
        """
        Decrypt an RSA-encrypted ModularInteger:
        decrypted = encrypted^D mod N
        Returns the recovered character.
        Raises ValueError if modulus != N.
        """
        if encrypted.modulus != cls.N:
            raise ValueError("Encrypted value must use modulus N.")

        decrypted_mod = encrypted ** cls.D
        return chr(decrypted_mod.value)


# ============================================================
#                 TESTING CODE
# ============================================================

print("=== Testing RSA Setup ===")
print("Are E and PHI coprime?", ModularInteger.are_coprime(RSAEncryptor.E, RSAEncryptor.PHI))
print("Check (E * D) mod PHI:", (RSAEncryptor.E * RSAEncryptor.D) % RSAEncryptor.PHI)
print()

# Test letters
test_letters = ["A", "B", "Z"]

print("=== RSA Encryption/Decryption Tests ===")
for letter in test_letters:
    print(f"\nTesting letter: {letter}")

    # Original value
    original_value = ord(letter)
    print("Original letter:", letter)
    print("Original value:", original_value)

    # Encrypt
    encrypted = RSAEncryptor.encrypt(letter)
    print("Encrypted value:", encrypted.value)
    # Decrypt
    recovered = RSAEncryptor.decrypt(encrypted)
    print("Recovered letter:", recovered)

  # Verify
  print("Match:", recovered == letter)
