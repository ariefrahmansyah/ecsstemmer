# ecsstemmer
ECS Stemmer for Indonesian Language

How to use:

from ecsstemmer import EcsStemmer

stemmer = EcsStemmer()

listOfWords = ["memakan", "mencintai"]
stemmer.stemm( listOfWords )

word = "mencintai"
stemmer.stemmWord( word )
