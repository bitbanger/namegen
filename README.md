namegen
======

This is a name generator which ingests a list of names and excretes any number of similar names.

The core predictive functionality is the result of a 2nd-order (trigram) Markov model trained on the provided name corpus. Name length is modeled as a Gaussian distribution with mean and standard deviation dictated by the corpus.

requirements
======

Python 2.7 or similar

execution
======

python namegen.py \<corpus_file\> \<num_novel_names_desired\>

miscellanea
======
The male and female name corpora were obtained from Deron Meranda, who obtained them from the 1990 US Census. The corpora are kinda huge! This generally equates to more outlandish names. I recommend shuffling them and taking a subset for more focused names.

known issues
======
Ends-of-words are not currently modeled in the trigrams, which means that trigrams which traditionally conclude a word will tend to be followed by additional letters if the name hasn't yet reached its prescribed length.
