#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for word in dir(hidden_4):
        if word[0] != "_":
            print(word)
