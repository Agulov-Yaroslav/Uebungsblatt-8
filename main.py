#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Übungsblatt 08"""

KNIGHTS = [
    ('Arthur', 34),
    ('Bedevere', 33),
    ('Galahad', 32),
    ('Lancelot', 36)
]


# Aufgabe 1

def sort_by_age(knights):
    """
    Parameter knights übergebene Liste von
    Rittern nach deren Alter in aufsteigender Reihenfolge sortiert wird

    :param knights:
    :return:
    """
    return sorted(knights, key=lambda x: x[1])


# Aufgabe 2

def young_knights(knights):
    """
    aus der als Parameter knights übergebenen
    Liste nur diejenigen Ritter
    (in unveränderter Reihenfolge) zurückgibt,
    welche jünger als 34 Jahre sind.

    :param knights:
    :return:
    """
    return list(filter(lambda x: x[1] < 34, knights))


# Aufgabe 3

def get_knight_names(knights):
    """
    aus der als Parameter knights übergebenen Liste das erste Element
    der in der Liste enthaltenen Tupel extrahiert und als Liste zurückgibt.

    :param knights:
    :return:
    """
    return [e[0] for e in knights]


# Aufgabe 4

def convert_to_dict(knights):
    """
    die als Parameter knights übergebene
    Liste in ein Dictionary konvertiert, wobei das erste Element
    der in der Liste enthaltenen Tupel den
    Schlüssel darstellt und das zweite Element den Wert.
    Der zunächst als Integer vorliegende Wert (das
    Alter) soll dabei zu einem String umgewandelt werden.

    :param knights:
    :return:
    """
    return {e[0]: str(e[1]) for e in knights}


# Aufgabe 5

def prime_numbers():
    """
    Generator, welcher - in aufsteigender Reihenfolge
    eine Primzahl nach der anderen bestimmt und zurückgibt.

    :return:
    """
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1


# Testaufrufe

if __name__ == "__main__":
    print(sort_by_age(KNIGHTS))
    print(young_knights(KNIGHTS))
    print(get_knight_names(KNIGHTS))
    print(convert_to_dict(KNIGHTS))
    NUMBERS = prime_numbers()
    print([next(NUMBERS) for _ in range(20) if NUMBERS is not None])
