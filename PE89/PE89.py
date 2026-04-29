# Project Euler problem 89

""" There are two main ways I could go about this. I could transform roman to roman directly, developing a number of rules for transforming roman numerals into minimal roman numerals.
Or, I could transform everything into arabic numerals (regular numbers), and then go back into roman numerals. I'm not sure which approach is easier or requires less work.
"""

denomination = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

subtractive_combinations = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}

all_combinations = denomination | subtractive_combinations
values_to_numerals = {v:k for k,v in all_combinations.items()}


def read_roman(numerals: str) -> int:
    """ My plan with this function is to scan from right to left. So XLIX would be read 10, -1, 50, -10.
    if an equal or larger numeral is encountered to the left of the current position, it is added to the current sum. however, if a smaller numeral is encountered, it is subtracted from the current sum.
    """

    numerals = numerals.upper()
    total = 0
    previous_letter = ''
    for letter in numerals[::-1]:
        letter_value = denomination[letter]
        if previous_letter:
            if letter_value >= denomination[previous_letter]:
                total += letter_value
            else:
                total -= letter_value
        else:
            total += letter_value
        previous_letter = letter
    return(total)


def write_roman(number: int) -> str:
    # Get the numerals corresponding to the largest value that is still less than the number
  
    numerals = ''
    while number:
        threshold = max(key for key in values_to_numerals.keys() if key <= number)
        number -= threshold
      
        numeral = values_to_numerals[threshold]
        numerals += numeral
  
    return(numerals)
    
    
def minimize(numerals):
    number = read_roman(numerals)
    return(write_roman(number))
    
    
if __name__ == "__main__":
    with open('0089_roman.txt', 'r') as file:
        non_minimal_numerals = file.readlines()
        non_minimal_numerals = [numerals.strip() for numerals in non_minimal_numerals]
  
    minimal_numerals = [minimize(numerals) for numerals in non_minimal_numerals]
    non_minimal_total_length = sum([len(n) for n in non_minimal_numerals])
    minimal_total_length = sum([len(n) for n in minimal_numerals])
  
    print(non_minimal_total_length-minimal_total_length)

