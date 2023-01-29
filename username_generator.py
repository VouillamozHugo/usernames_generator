import sys, time


def getUsername():
    print("Usernames file found \n\n" + 40 * "#" + "\n#  Start generating username variation  #\n" + 40 * "#" + "\n")
    with open(usernameFile, 'r') as i:
        lines = i.readlines()
        with open(fileToWrite, 'w') as f:
            f.writelines("")

        for name in lines:
            try:
                if name.strip():
                    tmp = name.split()
                    fname = tmp[0].lower()
                    lname = tmp[1].lower()
                    letterFirstname = fname[0]
                    letterLastname = lname[0]

                    generateVariation(fname, lname, letterFirstname, letterLastname)
                    generateVariation(lname, fname, letterLastname, letterFirstname)

                    letterFirstname = letterFirstname.upper()
                    letterLastname = letterLastname.upper()
                    generateVariation(fname, lname, letterFirstname, letterLastname)
                    generateVariation(lname, fname, letterLastname, letterFirstname)

            except Exception as e:
                print("An error occured while reading the usernames file\n"
                      "Be sure that all username are in the following structure => firstname lastname ", flush=True)


def generateVariation(fname, lname, letterFirstname, letterLastname):
    mutations = []

    mutations.append(fname + lname + "\n")
    mutations.append(fname + "." + lname + "\n")
    mutations.append(fname + " " + lname + "\n")

    fname = fname[1:]
    lname = lname[1:]

    mutations.append(letterFirstname + letterLastname + lname + "\n")
    mutations.append(letterFirstname + "." + letterLastname + lname + "\n")
    mutations.append(letterFirstname + " " + letterLastname + lname + "\n")
    mutations.append(letterFirstname + "." + letterLastname + "\n")
    mutations.append(letterFirstname + " " + letterLastname + "\n")
    mutations.append(letterFirstname + letterLastname + "\n")
    mutations.append(letterFirstname + fname + letterLastname + "\n")
    mutations.append(letterFirstname + fname + "." + letterLastname + "\n")
    mutations.append(letterFirstname + fname + " " + letterLastname + lname + "\n")
    mutations.append(letterFirstname + fname + letterLastname + lname + "\n")
    with open(fileToWrite, 'a') as f:
        f.writelines(mutations)


if __name__ == '__main__':
    start = time.time()
    try:
        usernameFile = sys.argv[1]
        fileToWrite = sys.argv[2]
    except:
        print("\nTo use the Username_builder.py you need to give the following arguments :\n" 
              "- Path to the list of username \n" 
              "- Name of the file for output \n" 
              "\n" 
              "Example of use : python username_builder.py username.txt outputWordlist.txt \n")
        sys.exit()
    getUsername()
    end = time.time()
    with open(fileToWrite, 'r') as f:
        count = len(f.readlines())
    duration = round(end - start, 4)
    print("\rThe scripts finished successfully !")
    print(str(count) + " lines where generated in " + str(duration) + " seconde")
    print("Happy hacking ;) ", flush=True)
