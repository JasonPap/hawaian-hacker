import sys
import random
from Password import Password
from PasswordClassifier import PasswordClassifier
import PasswordGen


def classify_and_generate():
    wordfile = "input_dictionaries/linkedin.txt"
    outputFile = "output_dictionaries/mutations.txt"
    if len(sys.argv) != 3:
        print "Number of arguments dif than 2, default filenames will be used"
    else:
        wordfile = sys.argv[1]
        outputFile = sys.argv[2]

    # delete the content of the output file if there are any
    with open(outputFile, 'w'):
        pass

    print "Creating classifier"
    classifier = PasswordClassifier()
    classifier.train(wordfile)
    print "Classifier built"

    count = 10000000  # """ <<==== minimum number of passwords to be generated"""
    letter_frequencies = dict()
    with open(outputFile, 'a') as output:
        with open(wordfile, 'r') as words:
            print "Calculating letter frequencies"
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
                # mutations = password.append_numbers()

                # write results to output file
                # output.write('\n'.join(mutations) + "\n")
            # for c in letter_frequencies:
            #    output.write(c + "," + str(letter_frequencies[c]) + "\n")
            print "Generating new passwords"
            n_created = 0
            while n_created <= count:
                tentative_passwords = PasswordGen.generate_passwords(letter_frequencies, 1000, random.randint(7, 14))
                output_buffer = []
                for p in tentative_passwords:
                    if classifier.predict(p):
                        output_buffer.append(p)
                        P = Password(p)
                        mutations = P.mutate(change_factor=3)
                        output_buffer.extend(mutations)
                        n_created += len(mutations) + 1
                output.write('\n'.join(output_buffer) + "\n")
                print "Created: " + str(n_created)

    print "done"


def mutate():
    wordfile = "input_dictionaries/linkedin.txt"
    outputFile = "output_dictionaries/mutations.txt"
    chng = 2
    mx_res = 10
    if len(sys.argv) != 5:
        print "Number of arguments dif than 2, default filenames will be used"
    else:
        wordfile = sys.argv[1]
        outputFile = sys.argv[2]
        chng = int(sys.argv[3])
        mx_res = int(sys.argv[4])

    # delete the content of the output file if there are any
    with open(outputFile, 'w'):
        pass
    with open(outputFile, 'a') as output:
        with open(wordfile, 'r') as words:
            print "Mutating passwords"
            for simpleWord in words:
                # below should be the logic for the creation of the new dictionary
                password = Password(simpleWord)

                mutations = password.mutate(change_factor=chng, max_results=mx_res)
                # mutations = password.append_numbers()

                # write results to output file
                output.write('\n'.join(mutations) + "\n")
                # print simpleWord + " + " + str(len(mutations))
    return


def append_numbers():
    wordfile = "input_dictionaries/linkedin.txt"
    outputFile = "output_dictionaries/mutations.txt"

    if len(sys.argv) != 3:
        print "Number of arguments dif than 2, default filenames will be used"
    else:
        wordfile = sys.argv[1]
        outputFile = sys.argv[2]

    # delete the content of the output file if there are any
    with open(outputFile, 'w'):
        pass
    with open(outputFile, 'a') as output:
        with open(wordfile, 'r') as words:
            print "Mutating passwords"
            for simpleWord in words:
                # below should be the logic for the creation of the new dictionary
                password = Password(simpleWord)

                # mutations = password.mutate(change_factor=chng, max_results=mx_res)
                mutations = password.append_numbers()

                # write results to output file
                output.write('\n'.join(mutations) + "\n")
                # print simpleWord + " + " + str(len(mutations))
    return


if __name__ == "__main__":
    if False:
        classify_and_generate()
    elif True:
        append_numbers()
    else:
        mutate()