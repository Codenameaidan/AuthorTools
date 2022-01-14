__version__ = "0.0.2"

from authortools import authortools

#Some ways to isolate parts of the text.
chapters = authortools.chapters
sentences = authortools.sentences
sentences_by_punctuation = authortools.sentences_by_punctuation
words = authortools.words
quotes = authortools.quotes


#Some ways to isolate parts of the text by splitting.
split_into_parts = authortools.split_into_parts
split_by_size = authortools.split_by_size

#Other tools
letter_count = authortools.letter_count
word_count = authortools.word_count
avg_word_length = authortools.avg_word_length
percent_char_in_quotes = authortools.percent_char_in_quotes

reading_time = authortools.reading_time
reading_time_minutes = authortools.reading_time_minutes
word_frequency = authortools.word_frequency

word_counts = authortools.word_counts
word_count_change = authortools.word_count_change
word_repetitions = authortools.word_repetitions

avg_sentence_word_count = authortools.avg_sentence_word_count
