"""Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik,
 następnie zmodyfikuje go i wyświetli w terminalu jego zawartość,
  a na końcu zapisze w wybranej lokalizacji.

Uruchomienie programu przez terminal:
python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>

 <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
 <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość,
  np. out.csv, out.json, out.txt lub out.pickle
 <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz)
 są współrzędnymi liczonymi od 0, natomiast "wartosc" zmianą która ma trafić na
 podane miejsce.

Przykładowy plik wejściowy znajduje się w repozytorium pod nazwą "in.json”.

Przykład działania:
python reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
Z pliku in.json ma wyjść plik out.csv:
gitara,3,7,0
kanapka,12,5,kubek
pedzel,17,34,5
plakat,czerwony,8,0
Wymagane formaty:

.csv
.json
.txt
.pickle"""
import csv
import json
import pickle
import sys

class DataProcessor:
    def __init__(self, input_file):
        self.data = []
        try:
            with open(input_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.data.append(row)
        except FileNotFoundError:
            print(f"Nie znaleziono pliku: {input_file}")
            sys.exit(1)

    def apply_changes(self, changes):
        for change in changes:
            x, y, value = change.split(',')
            try:
                self.data[int(y)][int(x)] = value
            except IndexError:
                print(f"Nieprawidłowe współrzędne: {change}")

    def display_data(self):
        print(json.dumps(self.data, indent=2))

    def save_data(self, output_file):
        extension = output_file.split('.')[-1]
        if extension == 'csv':
            with open(output_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.data)
        elif extension == 'json':
            with open(output_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        elif extension == 'txt':
            with open(output_file, 'w') as f:
                for row in self.data:
                    f.write('\t'.join(row) + '\n')
        elif extension == 'pickle':
            with open(output_file, 'wb') as f:
                pickle.dump(self.data, f)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Użycie: python data_processor.py input_file output_file [changes]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    processor = DataProcessor(input_file)
    processor.apply_changes(changes)
    processor.display_data()
    processor.save_data(output_file)
