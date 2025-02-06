
def main():

    with open("books/frankenstein.txt") as f: 
        file_contents = f.read()
        print(file_contents)
        
def count_words():
    f = open("books/frankenstein.txt")
    strings = f.read()
    words = strings.split()
    print(len(words))
    

def weird():
    with open("books/frankenstein.txt") as f:
        string = f.read()
        lowered = string.lower()

        count = {}

        for char in lowered: 
            if char in count:
                count[char] += 1 
        
            else: 
                count[char] = 1


    return count

character_count = weird()

def reported(count):

    for char in count: 
        if char.isalpha():
            print(f"the '{char}' character was found '{count[char]}' times")
    

  



reported(character_count)