# The file is invisible to oj-resolve, the extension is not `.py`..
import argparse

from competitive_verifier.models import VerificationInput

parser = argparse.ArgumentParser()
parser.add_argument("file1")
parser.add_argument("file2")
parser.add_argument("--not-equal", action="store_true")
args = parser.parse_args()
obj1 = VerificationInput.parse_file(args.file1)
obj2 = VerificationInput.parse_file(args.file2)

print("file1")
print(obj1.json(indent=2))
print("\n")
print("file2")
print(obj2.json(indent=2))
if args.not_equal:
    assert obj1 != obj2
else:
    assert obj1 == obj2
