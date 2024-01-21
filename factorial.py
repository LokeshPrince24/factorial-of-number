# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Read the numbers from the input file
    numbers = [int(num.strip()) for num in infile.readlines()]

    for num in numbers:
        fact = 1 
        while(num > 1): 
            fact = fact * num 
            num = num - 1 

        # Write the factorial to the output file
        outfile.write(str(fact) + '\n')
