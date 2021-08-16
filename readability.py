# Sets the educational level of the text

from cs50 import get_string
# --------------------------------------------------------


def main():
    
    # Request the user for text
    TEXT = get_string("Text: ")
    
    # Returns the number of letters in the string
    N_letters = get_letters(TEXT)
    
    # Returns the number of words in the string
    N_words = get_words(TEXT)
    
    # Returns the number of sentences in the string
    N_sentences = get_sentences(TEXT)
    
    # Returns Grade level
    grade_level = Glevel(N_letters, N_words, N_sentences)
    
    # Returns print of Grade level
    print_Glevel(grade_level)
    
# FUNCTIONS------------------------------------------------


def get_letters(TEXT):
    """"letter counter."""
    count = 0
    
    for c in TEXT:
        if c.isalpha():
            count += 1
            
    return count
# ------------------------FUNCTIONS--------------------------


def get_words(TEXT):
    """Words counter."""
    count = 0
    
    for c in TEXT:
        if c == ' ':
            count += 1
        
    return count + 1
# ------------------------FUNCTIONS--------------------------


def get_sentences(TEXT):
    """Sentences counter."""
    count = 0
    
    for c in TEXT:
        if c == '.' or c == '!' or c == '?':
            count += 1
        
    return count
# ------------------------FUNCTIONS--------------------------


def Glevel(letters, words, sentences):
    """Grade level cauculate."""
    L = (letters / float(words)) * 100
    
    S = (sentences / float(words)) * 100

    return round(0.0588 * L - 0.296 * S - 15.8)
# ------------------------FUNCTIONS--------------------------


def print_Glevel(Grelevel):
    """Print grade level."""
    if Grelevel >= 16:
        print("Grade 16+")
    
    elif Grelevel <= 1:
        print("Before Grade 1")
    
    else:
        print(f"Grade {Grelevel}")
# ------------------------FUNCTIONS--------------------------


# END-LINE
if __name__ == "__main__":
    main()