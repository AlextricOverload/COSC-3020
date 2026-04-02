# solution.py
# COSC 3020
# Lab Practice 3
# Author: Alexander Warren
# Last Modified: 16 February 2026

def main():
    p = 61
    q = 53
    e = 17

    # Generate our keys
    public_key, private_key, n, phi = rsa_keygen(p, q, e)

    # Print required values
    print(f"n: {n}")
    print(f"phi: {phi}")
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")

    # Test each grade
    test_grades = [92, 7, 100]

    for grade in test_grades:
        # Encrypt
        ciphertext = rsa_encrypt(grade, public_key)
        # Decrypt
        recovered_grade = rsa_decrypt(ciphertext, private_key)

        # Print results
        print(f"Original grade: {grade}")
        print(f"Ciphertext: {ciphertext}")
        print(f"Recovered grade: {recovered_grade}")

        # Verify
        if recovered_grade == grade:
            print("OK")
        else:
            raise ValueError(f"Error: {recovered_grade} does not match {grade}")



def gcd(a: int, b: int) -> int:
    """
    Takes in two values and returns the greatest common divisor using Euclidean algorithm

    :param a: the first integer, eventually reaches greatest common divisor
    :type a: int
    :param b: the second integer
    :type b: int
    :return: the greatest common divisor
    :rtype: int
    """
    #Unless b == 0, we have not yet reached the gcd
    while b != 0:
        a, b = b, a % b

    return a  # 'a' is now our GCD


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Takes in two values and returns the GCD and coefficients using Extended Euclidean Algorithm

    :param a: the first integer, eventually reaches greatest common divisor
    :type a: int
    :param b: the second integer
    :type b: int
    :return: the greatest common divisor and x, y such that x*a + y*b = g
    :rtype: tuple[int, int, int]
    """
    old_a, old_b = a, b
    x0, x1, y0, y1 = 1, 0, 0, 1  # Identity matrix

    # Iterate until a = gcd
    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1

    return a, x0, y0


def mod_inverse(e: int, phi: int) -> int:
    """
    Calculates the modular inverse of an integer

    :param e: The public exponent
    :type e: int
    :param phi: The value of Euler's totient function (p-1)(q-1)
    :type phi: int
    :return: The modular inverse
    :rtype: int
    """
    g, d, y = extended_gcd(e, phi)  # g = GCD, d = x coefficient, y = y coefficient

    if g != 1:  # Our GCD must be 1 for a mod inverse to exist
        raise Exception('Modular inverse does not exist')

    return d % phi


def rsa_keygen(p: int, q: int, e: int) -> tuple[tuple[int, int], tuple[int, int], int, int]:
    """
    Generates a public key and private key for rsa encryption and decryption
    :param p: A distinct prime number
    :type p: int
    :param q: A distinct prime number
    :type q: int
    :param e: The public exponent
    :type e: int
    :return: A tuple of the public key (e,n) and the private key (d, n) as well as n and phi
    :rtype: tuple[tuple[int, int], tuple[int, int], int, int]
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    public_key = (e,n)
    private_key = (d,n)

    return public_key, private_key, n, phi  # n and phi are returned for printing in main()


def rsa_encrypt(m, public_key) -> int:
    """
    Encrypts a message using the RSA public key
    :param m: The unencrypted message (as an integer)
    :type m: int
    :param public_key: The public key (e,n)
    :type public_key: tuple[int, int]
    :return: The encrypted message (as an integer)
    :rtype: int
    """
    e, n = public_key
    return pow(m, e, n)

def rsa_decrypt(c, private_key) -> int:
    """
    Decrypts a message using the RSA private key
    :param c: The encrypted message (as an integer)
    :type c: int
    :param private_key: The private key (d, n)
    :type private_key: tuple[int, int]
    :return: The deciphered message (as an integer)
    :rtype: int
    """
    d, n = private_key
    return pow(c, d, n)

# Driver code
if __name__ == "__main__" :
    main()
