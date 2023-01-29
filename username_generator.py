import sys

def getUsername():

    print("Usernames file found \n"
          "Start generating username variation\n###############")
    with open(usernameFile, 'r') as i:
        lines = i.readlines()
        for name in lines:
            try:
                if name.strip():
                    tmp = name.split()
                    fname = tmp[0].lower()
                    lname = tmp[1].lower()
                    letterFirstname = fname[0]
                    letterLastname = lname[0]

                    generateVariation(fname,lname,letterFirstname,letterLastname)
                    generateVariation(lname,fname,letterLastname,letterFirstname)

                    letterFirstname = letterFirstname.upper()
                    letterLastname = letterLastname.upper()
                    generateVariation(fname,lname,letterFirstname,letterLastname)
                    generateVariation(lname,fname,letterLastname,letterFirstname)

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
    mutations.append(letterFirstname +  fname + letterLastname + "\n")
    mutations.append(letterFirstname +  fname + "." + letterLastname + "\n")
    mutations.append(letterFirstname + fname + " " + letterLastname + lname + "\n")
    mutations.append(letterFirstname + fname  + letterLastname + lname + "\n")


    with open(fileToWrite, 'a') as f:
        f.writelines(mutations)


if __name__ == '__main__':
    try:
        usernameFile = sys.argv[1]
        fileToWrite = sys.argv[2]
    except:
        print("\nTo use the Username_builder.py you need to give the following arguments :\n" \
        "- Path to the list of username \n" \
        "- Name of the file for output \n" \
        "\n" \
        "Example of use : python username_builder.py username.txt outputWordlist.txt \n")
        sys.exit()
    getUsername()
    print("\rThe scripts finished successfully !\n"
          "Happy hacking ;) ", flush=True)
