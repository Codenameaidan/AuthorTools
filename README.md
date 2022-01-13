# AuthorTools
AuthorTools provides a multitude of functions for easily analyzing (your?) writing.  AuthorTools is made especially for creative writers with some python skills, or developers of writing applications.  It contains tools to split strings in a variety of ways, such as into sentences or by chapter, and functions to analyze text, like counting the percent of a text that is composed of dialogue (in quotes).
## Installation
AuthorTools is available on PyPI.
```
pip install authortools
```

## Usage
AuthorTools provides its functions in authortools.py.  After installation, you will need to import the tools.
```python
import authortools
```
Then, all functions should be available to you.
```python
import authortools
authortools.word_count("Sample Text.")
```
There is also another module that contains samples of many of the functions in authortools.py.  It's useful if you just want to see a bunch of results on some writing, without going too deep into the tools here.
```python
from authortools import writing_analysis
writing_analysis.run_tests("Sample Text.")
```
The easiest way to get started with the tools is to copy-paste your story (or whatever) into a .txt file, and read it into a string in Python.  Then run the functions on it.
```python
import authortools

text_file = open("input.txt", "r", encoding="utf8")
text = text_file.read()
text_file.close()

print(authortools.avg_word_length(text))
```
## Functions
### Sentences
```python
authortools.sentences("First Sentence.  Second Sentence\nThird Sentence.")
```
Returns an array of individual sentences found in the text.  Based on spaces (two spaces, \n, or \t).

### Sentences by punctuation
```python
authortools.sentences_by_punctuation("First Sentence.  Second Sentence\nStill the second sentence.")
```
Returns an array of individual sentences found in the text.  Based on punctuation (.?!).

### Words
```python
authortools.words("There's like six different words there.")
```
Returns an array of individual words found in the text.  Splits at all spaces and removes most punctuation except those part of the word itself.

### Quotes
```python
authortools.quotes("\"This quote will be added to the returned array,\" he said. \"This one will be too; but mine ends with an exclaimation point, which won't be removed, like your comma will be!\" I clarified.")
```
Returns an array of quotes found in the text.  Trailing comma and quotation marks are trimmed from the resulting array.

### Chapters
```python
authortools.chapters("Title: Whether this is included is optional.  Chapter 1\nThis is the first chapter.\nChapter 2: This is the second chapter.")
```
Returns an array of chapters found in the text.  Chapters need to be in the format: "Chapter 00".  Spacing and case don't matter.
Note that "Chapter XIV" and "Chapter Fourteen" will NOT be found and split by this function.  

Two optional parameters: num_chapters (int) -- This is in case you wanted to limit it.  num_chapters defaults to 100, but the function returns when it can't find any more chapters.  include_title defaults to False; Should any text found _before_ the first chapter be included as the first element of the returned list?

### Split into parts
```python
authortools.split_into_parts("Part one  Part two  Part three", 3)
```
Splits text into an array of n equally sized parts.  Good for analyzing writing that doesn't have defined chapters; like, split into three parts, and run avg_sentence_word_count on each part to see if your style changed.

### Split by size
```python
authortools.split_by_size("Part one  Part two  Part three", 10)
```
Splits text into an array with each part being of size n.

### Letter count
```python
authortools.letter_count("Ten letters!")
```
Counts the letters (a-z and A-Z) in a given string.

### Word count
```python
authortools.word_count("There are five words here.")
```
Returns the number of words in a given string. 

### Average word length
```python
authortools.avg_word_length("avg len is 2.5") 
```
Returns the average word length in a given string.  

### Percent char in quotes
```python
authortools.percent_char_in_quotes("\"0.35,\" he said.") 
```
Returns the percent (0.0-1.0) of characters that are in quotes.  Quotation marks not counted as characters.  Great for analyzing how frequently one uses dialogue.

### Reading time
```python
authortools.reading_time("Not much.") 
```
Returns the reading time in seconds.

### Reading time in minutes
```python
authortools.reading_time_minutes("Even less.") 
```
Returns the reading time in minutes.

### Word counts
```python
my_sentences = authortools.sentences("First Sentence.  Second Sentence\nThird Sentence.")
my_word_counts = authortools.word_counts(my_sentences) 
```
Returns the word counts for multiple items in a list as a list.  Sentence word count should vary in good writing!

### Word count change
```python
my_sentences = authortools.sentences("First Sentence.  Second Sentence\nThird Sentence.")
my_word_counts = authortools.word_count_change(my_sentences) 
```
Returns the word counts change (current - previous) for every item in the list as a list.  Sentence word count should vary in good writing!

### Average sentence word count
```python
authortools.avg_sentence_word_count("Three words here.  Few here, too.  Average is three.") 
```
Returns the average amount of words per sentence in a given text.

### Word repetitions
```python
authortools.word_repetitions("Words; do any words repeat in this sentence made of words?")
```
Returns an array containing any words that repeat in the given string.  It isn't good to repeat yourself in the same sentence, generally speaking.  Pair with authortools.sentences and a loop if you want a per-sentence basis, since this function looks for repetitions in the whole string you give it.  

### Word frequency
```python
authortools.word_frequency("Two times that two appears in this text.")
```
Returns a dictionary, with the keys being a word, and the value being the amount of times that word appears in the text.  Good for seeing which words are frequently used in a peice of writing.