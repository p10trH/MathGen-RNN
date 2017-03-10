# quick script to generate math (addition) data for training

# save to file
fileToSave = "data/math.txt"

# limit of for loops
limit = 500

def main():

    generateMath()

def generateMath():

    f = open(fileToSave, 'w')

    # calculate addition problems, store in string, write to file
    # example: 75 = 50 + 25
    for num_1 in range(1, limit):
        for num_2 in range(1, limit):
            added_sum = num_1 + num_2
            stringToAdd = str(added_sum) + " = " + str(num_1) + " + " + str(num_2)
            f.write(stringToAdd + "\n")

    f.close()

if __name__ == '__main__':
    main()
