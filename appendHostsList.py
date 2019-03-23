# Authors: CP, RP

import sys

systemHostFile = sys.argv[1]
updatesHostFile = sys.argv[2]

if len(sys.argv) < 3:
    print("Usage: sudo python addHostsList.py [/etc/hosts] [/tmp/newhosts]")
    system.exit(1);

customTagText = "# Managed by Swachh - Control Ads"

oldFile = open(systemHostFile, "r")
existingEntries = set()

swachhAdTag = False
for line in oldFile:
    line = line.replace("\n", "")
    if swachhAdTag:
       a = line.split()
       if len(a) > 1:
           existingEntries.add(a[-1])

    else:
        if line == customTagText:
            swachhAdTag = True

print("swachhAdTag: {}, Existing entries: {}".format(swachhAdTag, len(existingEntries)))

newEntries = set()

newFile = open(updatesHostFile, "r")
with newFile as f:
    for line in f:
        newEntries.add(line.replace("\n", ""))

entriesToAdd = set(newEntries - existingEntries)
print ("New entries to be added: {}".format(len(entriesToAdd)))

oldFile.close()
newFile.close()
with open(systemHostFile, "a") as editFile:
    if not swachhAdTag:
        editFile.write(customTagText + "\n")
    for site in entriesToAdd:
        newEntry = "127.0.0.1 {}\n".format(site)
        editFile.write(newEntry)
