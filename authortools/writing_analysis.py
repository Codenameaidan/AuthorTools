#analysis.py

import authortools

def run_tests(text: str):
    """
    A sample method showing a basic use case for most of the functions in authortools.py.
    """
    chapters = authortools.chapters(text)
    sentences = authortools.sentences(text)
    words = authortools.words(text)
    quotes = authortools.quotes(text)

    print("General counts:")
    print("  # chapters: ", len(chapters))
    print("  # sentences: ", len(sentences))
    print("  # words: ", len(words)) #Can also just use word_count(text)
    print("  # quotes: ", len(quotes))
    print("  # characters: ", len(text))
    print("  # letters: ", authortools.letter_count(text))
    print()

    print("Analysis:")
    print("  Average word length: ",authortools.avg_word_length(text)," characters")
    print("  Average sentence word count: ",authortools.avg_sentence_word_count(text), " words")
    print("  Percent of text that is dialogue: ",authortools.percent_char_in_quotes(text)*100, "%")
    print()

    print("Time:")
    print("  Reading time (200wpm): ", authortools.reading_time(text)," seconds")
    print("  Reading time (200wpm): ", authortools.reading_time_minutes(text), " minutes")
    print()

    print("Word repetitions in sentences:")
    for sentence in sentences:
        rep = authortools.word_repetitions(sentence)
        if(len(rep) != 0):
            print("  WORDS REPEATING FOUND IN ("+sentence[:12]+"...) -> ",rep)
    print()

    print("Word Frequency:")
    wf = authortools.word_frequency(text)
    if('the' in wf):
        print("  Frequency of the word 'the': ",wf['the'])
    else:
        print("  'the' was not in the given string.")
    print()
        
    print("Change over time (split entire text into 3 equal parts):")
    parts = authortools.split_into_parts(text,3)
    print("  Avg sentence word count(pt.1) --> ",authortools.avg_sentence_word_count(parts[0]))
    print("  Avg sentence word count(pt.2) --> ",authortools.avg_sentence_word_count(parts[1]))
    print("  Avg sentence word count(pt.3) --> ",authortools.avg_sentence_word_count(parts[2]))

    print("Analysis complete!")







