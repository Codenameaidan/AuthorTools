#authortools.py
#Created by Aidan J. Walsh

import re

def chapters(text: str, num_chapters: int = 100, include_title: bool = False) -> list[str]:
    """
    Splits text into an array of individual chapters.
    This function expects chapter formatting to be something like:
        
        "Very probably, I'm afraid," she said.
        Chapter 14
        The Heart of Gold fled on silently through the night of space, now on conventional photon drive.
    
    (newlines not required.  Case insensitive.  "Chapter XIV" and "Chapter Fourteen" will NOT be found and split up.)

    Parameters
    ------------
    text: str
        The text to be split up.
    num_chapters: int, optional.
        How many chapters to look for.  Defaults to 100 chapters (will automatically break when it can't find any more.)
    include_title: bool, optional.
        Should any text found before the first chapter be included as the first element of the returned list?  Defaults to False.

    Returns
    ------------
    str[]
        An array of strings (chapters)
    """

    str_array = []
    remaining_str = text
    for i in range(1, num_chapters+1): #For chapters 1-num_chapters
        temp = re.split("chapter "+str(i), remaining_str, flags=re.IGNORECASE) #Split where we find chapter xx, ignore case
        if(len(temp) < 2): #If chapter wasn't split (wasn't found) exit
            break
        remaining_str = temp[1]
        str_array.append(temp[0].strip())
    str_array.append(remaining_str) 
    if(not include_title): #Pop off the title if include_title = False
        str_array.pop(0)
    return str_array


def split_into_parts(text: str, num_parts: int) -> list[str]: 
    """
    Splits text into an array of size num_parts.

    Parameters
    ------------
    text: str
        The text to be split up.
    num_parts: int
        How many equally sized parts to split the text into.

    Returns
    ------------
    str[]
        An array of strings (parts).
    """
    #https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    #tixxit
    k, m = divmod(len(text), num_parts) 
    return list(text[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(num_parts))


def split_by_size(text: str, size: int) -> list[str]:
    """
    Splits text into an array with chunks of "size" characters.  The last part may be shorter than the other parts.

    Parameters
    ------------
    text: str
        The text to be split up.
    size:
        The size of each chunk

    Returns
    ------------
    str[]
        An array of strings (parts)
    """
    parts = []

    for i in range(0, len(text), size): 
        parts.append(text[i:i+size]) #Add parts of size

    return parts

def sentences(text: str) -> list[str]:
    """
    Splits text into an array of its sentences.  Finds two spaces, or newline, or tab, and splits there.

    Parameters
    ------------
    text: str
        The text to be split up.

    Returns
    ------------
    str[]
        An array of strings (sentences)
    """
    list_sentences = re.split('  |\n|\t', text) #Splits along spaces (no single space -- only double)
    list_sentences = list(filter(str.strip, list_sentences)) #Filters out 'sentences' that are only whitespace

    for i in range(0,len(list_sentences)): #Removes whitespace from remaining items
        list_sentences[i] = list_sentences[i].strip()
    return list_sentences


def sentences_by_punctuation(text:str) -> list[str]: 
    """
    Splits text into an array of its sentences.  Finds .?! and splits there.
    Note: John J. Doe will return ['John J.', 'Doe']...

    Parameters
    ------------
    text: str
        The text to be split up.

    Returns
    ------------
    str[]
        An array of strings (sentences)
    """

    #Note: John J. Doe returns ['John J.', 'Doe']...
    list_sentences = []
    start = 0
    for x in range(0, len(text)):
        if(text[x] in '.?!\n'):
            if(x - start <= 1): #In case the sentence ends like ... or ???
                if(len(list_sentences) == 0):
                    list_sentences.append(text[start:(x+1)].strip())
                    start = x+1
                    continue
                list_sentences[-1] += text[start:(x+1)] #Add that punctuation
                start = x+1 #Start is the next character
                continue
            list_sentences.append(text[start:(x+1)].strip())
            start = x+1 #Start is the next character

    #Return stuff found after last punctuation?
    if(start != len(text)):
        list_sentences.append(text[start:(x+1)].strip())
    return list_sentences


def words(text: str) -> list[str]:
    """
    Splits text into an array of its words.  Splits at all spaces and trims any punctuation.

    Parameters
    ------------
    text: str
        The text to be split up.

    Returns
    ------------
    str[]
        An array of strings (words)
    """
    list_words = re.split(' |\n|\t', text) #Splits along spaces
    for i in range(0, len(list_words)):
        list_words[i] = re.sub(r'\.|\?|!|\,|\;|\"|\(|\)|\:|\/|\“|\”', '', list_words[i])
    
    list_words = filter(str.strip, list_words) #Strips leading/trailing whitespaces 
                                                #and filters out 'sentences' that are only whitespace
    return list(list_words)

def quotes(text: str) -> list[str]:
    """
    Gets all peices of text enclosed in quotes.

    Parameters
    ------------
    text: str
        The text to read.

    Returns
    ------------
    str[]
        An array of strings (quotes found in the text)
    """
    list_quotes = []
    single_quote = ""
    counting_quotes = False
    for char in text:
        if(char == '\"' or char == "“" or char == "”"): #different kinds of quotes (especially if copy-pasted from word doc...)
            if(counting_quotes):
                if(len(single_quote) != 0):
                    if(single_quote[-1] == ','):
                        single_quote = single_quote[:(len(single_quote)-1)] #Remove trailing comma
                list_quotes.append(single_quote)
                single_quote = ""
            counting_quotes = not counting_quotes #Start or stop counting quotes
            continue
        if(counting_quotes):
            single_quote += char
        
    return list_quotes


def word_count(text: str) -> int:
    """
    Counts the total words in a string.

    Parameters
    ------------
    text: str
        The text to count the words of.

    Returns
    ------------
    int
        The number of words in the text.
    """
    list_words = re.split(' |\n|\t', text) #Splits along spaces
    list_words = list(filter(str.strip, list_words))
    return len(list_words)


def avg_word_length(text: str) -> float:
    """
    Calculates the average word length for a given string.

    Parameters
    ------------
    text: str
        The text to find the average word length of.

    Returns
    ------------
    float
        The average word length.
    """
    
    list_words = words(text)
    if(len(list_words) == 0): #Don't want /0 error later
        return 0
    total = 0
    for word in list_words:
        total+=len(word) #Add the length of every word to total
    return (total/len(list_words))


def avg_sentence_word_count(text: str) -> float:
    wc_list =  word_counts(sentences(text))
    if(len(wc_list) == 0):
        return 0
    total = 0
    for wordcount in wc_list: #Add word count of every sentence
        total+=wordcount
    return total / len(wc_list)




def letter_count(text: str) -> int:
    """
    Counts the number of letters (a-z and A-Z) in a given string.

    Parameters
    ------------
    text: str
        The text to count the letters of.

    Returns
    ------------
    int
        The number of letters in the given string.
    """
    count: int = 0
    for char in text:
        if(char.isalpha()):
            count+=1
    return count


def percent_char_in_quotes(text: str) -> float:
    """
    Calculates the percent of characters that appear enclosed in quotes. 
    (assuming correct quote usage.  Doesn't count block quotations.)
        
        "Oh, hi," he said.
        
        >> 7 characters in quotes and 15 total characters (since quotes themselves are not counted as characters)
            = 7/15 = 0.4375

    Parameters
    ------------
    text: str
        The text to read.

    Returns
    ------------
    float
        percent of characters in quotes (0.0-1.0)
    """
    if(len(text) == 0):
        return 0

    num_char_in_quotes = 0
    total_char = 0
    
    counting_quotes = False
    for char in text:
        if(char == '\"' or char == "“" or char == "”"): #different kinds of quotes (especially if copy-pasted from word doc...)
            counting_quotes = not counting_quotes #Start or stop counting quotes
            continue
        if(counting_quotes):
            num_char_in_quotes+=1
        total_char += 1 #Do this rather than len() because we aren't counting quotes themselves as characters!
    ratio = num_char_in_quotes/total_char
    return ratio


def reading_time(text: str, wpm:int = 200) -> float:
    """
    Returns the reading time of a given string in seconds.

    Parameters
    ------------
    text: str
        The text to find the reading time of.
    wpm: int, optional
        Words-per-minute.  Defaults to 200.

    Returns
    ------------
    float
        The reading time in seconds
    """
    return reading_time_minutes(text,wpm) * 60


def reading_time_minutes(text: str, wpm:int = 200) -> float:
    """
    Returns the reading time of a given string in minutes

    Parameters
    ------------
    text: str
        The text to find the reading time of.
    wpm: int, optional
        Words-per-minute.  Defaults to 200.

    Returns
    ------------
    float
        The reading time in minutes.
    """
    return (word_count(text)/wpm)


def word_frequency(text: str, use_cases: bool = False) -> dict[str,int]:
    """
    Returns a dictionary of the frequency of all words in given string.  
    All words turned to lowercase if use_cases left unspecified.

    Parameters
    ------------
    text: str
        The text to find the word frequency of.
    use_cases: bool, optional
        Should words be considered case-sensitive, and saved as keys with their cases?  Defaults to False.

    Returns
    ------------
    dict[str,int]
        The frequency (int) of every string (str) in text.
    """

    dictionary = {}
    list_words = words(text)
    for word in list_words:
        if(not use_cases):
            word = word.lower()

        if(word in dictionary):
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary
            

def word_counts(item_list: list[str]) -> list[int]:
    """
    Returns the word count of each item in given list.

    ex (for sentences): authortools.word_counts(authortools.sentences(my_text))

    Parameters
    ------------
    item_list: str[]
        An array of strings, the word count of each item to be calculated.

    Returns
    ------------
    int[]
        The word_count of each item in item_list
    """
    lengths_list = [None] * len(item_list)
    for i in range(0, len(item_list)):
        lengths_list[i] = word_count(item_list[i])
    return lengths_list


def word_count_change(item_list: list[str]) -> list[int]:
    """
    Returns the change in word count (current - previous) for each item in given list.

    ex (for sentence word count change): authortools.word_count_change(authortools.sentences(my_text))

    Parameters
    ------------
    item_list: str[]
        An array of strings, the word count of each item minus the previous item to be calculated.

    Returns
    ------------
    int[]
        The word count change of each item in item_list.
    """
    if(len(item_list) == 0):
        return []
    lengths_list = [None] * len(item_list)
    lengths_list[0] = 0
    prev_length = len(words(item_list[0]))
    for i in range(1, len(item_list)):
        new_length = word_count(item_list[i])
        lengths_list[i] = new_length-prev_length
        prev_length = new_length
    return lengths_list


def word_repetitions(text: str) -> list[str]:
    """
    Returns any words that repeats in the text 
    (ignores: 'the', 'a', 'an', 'and', 'or'). 

    ex: >> authortools.word_repetitions("He walked out of the supermarket with a cart; it was the supermarket with a sign out front.")
        >> ['out', 'supermarket', 'with']

    Parameters
    ------------
    text: str
        The text to find the reptititions in.

    Returns
    ------------
    str[]
        A list of any words that repeat in the text.
    """
    ignore_words = ['the','a','an', 'and', 'or', 'in', 'to']

    list_words = words(text)
    list_repetitions = []
    for x in range(0,len(list_words)):
        word = list_words[x].lower()
        if(list_words[x] in ignore_words):
            continue
        if(list_words[x] in list_repetitions):
            continue
        for y in range((x+1),len(list_words)):
            if(list_words[x] == list_words[y]):
                list_repetitions.append(list_words[x])
                break

    return list_repetitions