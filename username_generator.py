import sys, time


def getUsername():
    print("Usernames file found \n\n" + 40 * "#" + "\n#  Start generating username variation  #\n" + 40 * "#" + "\n")
    createUpperCase = ''
    while createUpperCase not in ['y', 'Y', 'n', 'N']:
        createUpperCase = input("Create upper case variation (add 36 variation per username) ? [Y/N]")

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
                    letterf = fname[0]
                    letterl = lname[0]

                    # All variations in lower cases
                    generation(fname, lname)
                    generation(lname, fname)
                    generation(letterf, lname)
                    generation(letterl, fname)
                    generation(letterl, letterf)
                    generation(letterf, letterl)

                    # Create all upper case variation if the user want it
                    if createUpperCase in ['y', 'Y']:
                        generation(fname.upper(), lname.upper())
                        generation(lname.upper(), fname.upper())
                        generation(fname.capitalize(), lname.capitalize())
                        generation(lname.capitalize(), fname.capitalize())
                        generation(letterl.upper(), letterf.upper())
                        generation(letterf.upper(), letterl.upper())

                        # Same as before but only the first part the username will be capitalized
                        generation(fname.upper(), lname)
                        generation(lname.upper(), fname)
                        generation(fname.capitalize(), lname)
                        generation(lname.capitalize(), fname)
                        generation(letterl.upper(), letterf)
                        generation(letterf.upper(), letterl)
            except Exception as e:
                print("An error occured while reading the usernames file\n"
                      "Be sure that all username are in the following structure => firstname lastname ", flush=True)


def generation(fname, lname):
    mutations = []
    mutations.append(fname + lname + "\n")
    mutations.append(fname + "." + lname + "\n")
    mutations.append(fname + " " + lname + "\n")
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
