import string
import random

# common substitutions
substitutions = {'s': ['$', 'S', '5'], 'i': ['1', 'l', '!'], 'a': ['@', 'A'], 't': ['+', '7', 'T'], 'e': ['3', 'E'],
                 'g': ['9', 'G', '6'], 'o': ['0', 'O'], 'b': ['8', 'B'], 'c': ['(', 'C'], 'd': ['6', 'D'],
                 'f': ['#', 'F'], 'h': ['#', 'H'], 'k': ['<', 'K'], 'l': ['i', '1', 'L'], 'q': ['9', 'Q'],
                 'v': ['<', '>', 'V'], 'w': ['uu', 'W', '2u'], 'x': ['%', 'X'], 'y': ['?', 'Y'], 'j': ['J'], 'm': ['M'],
                 'n': ['N'], 'p': ['P'], 'r': ['R'], 'u': ['U'], 'z': ['Z'], 'A': ['a', '@'], 'B': ['b'], 'C': ['c'],
                 'D': ['d'], 'E': ['e'], 'F': ['f'], 'G': ['g'], 'H': ['h'], 'I': ['i'], 'K': ['k'], 'M': ['m'],
                 'N': ['n'], 'O': ['o'], 'P': ['p'], 'Q': ['q'], 'R': ['r'], 'S': ['s'], 'T': ['t'], 'L': ['l'],
                 'J': ['j'], 'W': ['w'], 'V': ['v'], 'U': ['u'], 'X': ['x'], 'Y': ['y'], 'Z': ['z']}

# possible years contained in passwords
years = []
for i in range(1900, 2017):
    years.append(str(i))

ages = []
for i in range(0, 99):
    ages.append(str(i))


class Password:
    def __init__(self, password):
        tmp = password
        self.password = list(tmp.rstrip('\n'))
        self.letter_frequencies = dict()
        self.others = []

    def analyze_frequencies(self):
        """
        This function will find the frequencies of each letter
        of the string and store them in a dictionary.
        """
        for l in string.ascii_letters:
            self.letter_frequencies[l] = 0
        for n in range(0, 10):
            self.letter_frequencies[str(n)] = 0

        for c in self.password:
            if c in self.letter_frequencies:
                self.letter_frequencies[c] += 1
            else:
                self.others.append(c)

    def show(self):
        print ''.join(self.password)

    def print_frequencies(self):
        """
        Print the frequencies of each letter.
        """
        if not self.letter_frequencies and not self.others:
            self.analyze_frequencies()
        for c in string.ascii_letters:
            if c in self.letter_frequencies:
                if self.letter_frequencies[c] > 0:
                    print c + " : " + str(self.letter_frequencies[c])
        if self.others:
            print self.others

    def mutate(self, change_factor=2, max_results=10):
        """
        Mutations in this function are based on the substitution dictionary and are randomized.
        :param change_factor: set this param to 2 to change half the characters of the word,
        3 to change 1/3 rd of them etc.
        :param max_results: maximum number of results returned
        :return: list of different mutations of the original password
        """
        results = dict()
        s = list(range(0, len(self.password)))
        # alt = ""
        count = 0
        # while len(results) < max_results:
        #     random.shuffle(s)
        #     for i in range(0, len(self.password)/change_factor):
        #         c = self.password[s[i]]
        #         if c in substitutions:
        #             alt = random.choice(substitutions[c])
        #         else:
        #             alt = random.choice(string.ascii_letters)
        #     newpsw = self.password[:s[i]] + [alt] + self.password[s[i]+1:]
        #     results[''.join(newpsw)] = 1
        #     count += 1
        #     if count > 10*max_results:
        #         break

        while len(results) < max_results:
            random.shuffle(s)
            newpsw = self.password
            for i in range(0, len(self.password)/change_factor):
                c = self.password[s[i]]
                if c in substitutions:
                    newpsw[s[i]] = random.choice(substitutions[c])
                else:
                    newpsw[s[i]] = random.choice(string.ascii_letters)
            results[''.join(newpsw)] = 1
            count += 1
            if count > 10*max_results:
                break

        return results.keys()

    def append_numbers(self):
        # input word should be a string
        results = []
        word = ''.join(self.password)
        for year in years:
            results.append(word + year)
        for age in ages:
            results.append(word + age)
        results.append(word + "123")
        results.append(word + "1234")
        results.append(word + "12345")
        results.append(word + "123456")
        results.append("1" + word)

        return results

