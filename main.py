import sys
from Password import Password


def main():
    wordfile = "linkedin.txt"
    outputFile = "my_passwords.csv"
    if len(sys.argv) != 3:
        print "Number of arguments dif than 2, default filenames will be used"
    else:
        wordfile = sys.argv[1]
        outputFile = sys.argv[2]

    # delete the content of the output file if there are any
    with open(outputFile, 'w'):
        pass

    print "starting"


    letter_frequencies = dict()
    with open(outputFile, 'a') as output:
        with open(wordfile, 'r') as words:
            for simpleWord in words:
                # below should be the logic for the creation of the new dictionary
                password = Password(simpleWord)
                password.analyze_frequencies()
                for c in password.letter_frequencies:
                    if c in letter_frequencies:
                        letter_frequencies[c] += password.letter_frequencies[c]
                    else:
                        letter_frequencies[c] = password.letter_frequencies[c]
                # password.print_frequencies()
                # mutations = password.mutate()

                # write results to output file
                # output.write('\n'.join(mutations) + "\n")
            for c in letter_frequencies:
                output.write(c + "," + str(letter_frequencies[c]) + "\n")
    print "done"


if __name__ == "__main__":
    main()
