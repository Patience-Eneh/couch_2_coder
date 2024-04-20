# OPEN SOURCE
# to install 3rd party documents on python, you go on pypi.org. click on browse projects. on the search icon, type in wikipedia as a file we want to import. Then click on the wikipedia API for python. Under documentation, click on quickstart.
# the first code line would show what to type on the new termina; the output terminal (python -m pip install wikipedia or pip install wikipedia). this will install wikipedia. then on the input console, we trype the below lines of code to import it.

# # pip install wikipedia
# # python -m pip install wikipedia

import wikipedia
print(wikipedia.search("London"))


london = wikipedia.page("London")
# # print(london.images)  



# # to find every sentence on london Wikipedia page where the word "population is mentioned".


# split_sentences = london.content.split(".")
# for sentence in split_sentences:
#     if("population" in sentence):
#         print(sentence)

        # to add this into a list, create a list below and append.
sentences_with_population_substring = []
split_sentences = london.content.split(".")
for sentence in split_sentences:
    if("population" in sentence):
        sentences_with_population_substring.append(sentence)

print(sentences_with_population_substring)

