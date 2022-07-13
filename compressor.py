import os

replacements = {
    "\\": "\\\\",
    "\n": "\\n",
    "\t": "\\t",
    "  ": "\\t",
    "\"": "\\\""
}

for file in os.listdir():
    # Ignore all non-text files
    if not file.endswith(".txt"):
        print(f"Skipped {file}")
        continue

    print(f"Starting compression of {file}...")

    fileReader = open(file, "r")
    fileContents = fileReader.read()

    for key in replacements:
        fileContents = fileContents.replace(key, replacements[key])

    fileReader.close()

    fileWriter = open(f"{file[:-4]}_compressed.txt", "x")
    fileWriter.write(fileContents)
    fileWriter.close()
    print(f"Finished compression of {file}...")
