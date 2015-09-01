import sys

def countingVowels(s):
    count = 0
    s = s.lower()
    for vowel in 'aeiou':
        count += s.count(vowel)
    #print 'Number of vowels: {0}'.format(count)
    return count


def countingBobs(s):
    count = 0
    s = s.lower()
    index = s.find('bob')
    while index >= 0:
        count += 1
        s = s[index+1:]
        index = s.find('bob')
    print 'Number of times bob occurs is: {0}'.format(count)
    return count

def alphabeticalSubs(s):
    longest_count = 0
    longest_start = 0

    count = 0
    start = 0
    for index, char in enumerate(s):
        if (index == 0) or (char >= s[index-1]):
            count += 1
        else:
            if count > longest_count:
                longest_count = count
                longest_start = start
            count = 1
            start = index

    if count > longest_count:
        longest_count = count
        longest_start = start

    ans = s[longest_start:longest_start+longest_count]
    print 'Longest substring in alphabetical order is: {0}'.format(ans)
    return ans


def main():
    #print countingVowels("IIIhello, my name Is Thomas")
    #print countingBobs('azcbobobegghakl')
    alphabeticalSubs('mnuwglewbuixbtlh')
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))

