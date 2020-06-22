# Our contains Script
import argparse


parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')


args = parser.parse_args()
snippet = args.snippet.lower()


words = open('words').readlines()
print([word.strip() for word in words if snippet in word.lower()])
