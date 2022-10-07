import re
from pathlib import Path

filename = input("Enter the filename: ")
filepath = Path(filename)

if (not filepath.is_file()):
    print("File does not exist")
    exit(1)

with open(filepath, 'r') as file:
    data = file.read()

imagematches = re.findall(r'!\[.*\]\((.*)\)', data)
folder = filepath.parent

print(imagematches)

i = 1
for imagename in imagematches:
    if filepath.stem in imagename:
        continue

    imagefile = Path(folder, imagename)
    if (not imagefile.is_file()):
        print(f"Image file {imagefile} does not exist")
        continue
    
    newimagefile = None
    while (newimagefile is None or newimagefile.is_file()):
        newimagefile = Path("Images", f"{filepath.stem}-{i:02d}.png")
        i += 1

    imagefile.rename(newimagefile)
    data = data.replace(imagename, f"../Images/{newimagefile.name}")

with open(filepath, 'w') as file:
    file.write(data)

print("Done!")
