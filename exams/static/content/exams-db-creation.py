#!/usr/bin/env python3

import sqlite3

db = sqlite3.connect('/tmp/exams.db')
cursor = db.cursor()

cursor.execute('''
  CREATE TABLE exams (
    id INTEGER NOT NULL,
    year INTEGER,
    semester INTEGER,
    is_second_chance INTEGER,
    is_third_chance INTEGER,
    duration INTEGER,
    PRIMARY KEY(id));
''')

cursor.execute('''
  CREATE TABLE lecturers (
    id INTEGER NOT NULL,
    first_name TEXT,
    last_name  TEXT,
    PRIMARY KEY(id));
''')

cursor.execute('''
  CREATE TABLE exams_lecturers (
    exam_id INTEGER NOT NULL,
    lecturer_id	INTEGER NOT NULL,
    PRIMARY KEY(exam_id,lecturer_id),
    FOREIGN KEY(exam_id) REFERENCES exams(id) ON DELETE SET NULL,
    FOREIGN KEY(lecturer_id) REFERENCES lecturers(id) ON DELETE SET NULL);
''')

cursor.execute('''
  CREATE TABLE questions (
    id INTEGER,
    exam_id INTEGER,
    question_number INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(exam_id) REFERENCES exams(id) ON DELETE SET NULL) WITHOUT ROWID;
''')

cursor.execute('''
  CREATE TABLE sections (
    id INTEGER,
    question_id	INTEGER,
    section_number INTEGER,
    question_text TEXT,
    score INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(question_id) REFERENCES questions(id) ON DELETE SET NULL) WITHOUT ROWID;
''')

cursor.execute('''
  CREATE TABLE answers (
    id INTEGER NOT NULL,
    section_id	INTEGER,
    answer_text	TEXT,
    PRIMARY KEY(id),
    FOREIGN KEY(section_id) REFERENCES sections(id) ON DELETE SET NULL) WITHOUT ROWID;
''')

#######################################################################################
#######################################################################################
#######################################################################################

root_dir = '/home/amir/workspace/repositories/gingolda/exams/static/content/'

def read_from_file(relative_path):
    with open(root_dir + relative_path, 'r') as f:
        return f.read()

yuli = 'יולי'
eidelman = 'אידלמן'
semion = 'סמיון'
alesker = 'אלסקר'

lecturers = [(1, semion, alesker),
             (2, yuli, eidelman)]

exams = [(1, 2016, 1, 0, 0, 3),
         (2, 2016, 1, 1, 0, 3)]

exams_lecturers = [(1, 1),
                   (1, 2),
                   (2, 1),
                   (2, 2)]

questions = [(1, 1, 1),
             (2, 1, 2),
             (3, 1, 3),
             (4, 2, 1),
             (5, 2, 2),
             (6, 2, 3)]

sections = [( 1, 1, 1, read_from_file('1/q_1_1.txt'), 18),
            ( 2, 1, 2, read_from_file('1/q_1_2.txt'), 18),
            ( 3, 2, 1, read_from_file('1/q_2_1.txt'), 18),
            ( 4, 2, 2, read_from_file('1/q_2_2.txt'), 18),
            ( 5, 3, 1, read_from_file('1/q_3_1.txt'), 18),
            ( 6, 3, 2, read_from_file('1/q_3_2.txt'), 18),
            ( 7, 4, 1, read_from_file('2/q_1_1.txt'), 18),
            ( 8, 4, 2, read_from_file('2/q_1_2.txt'), 18),
            ( 9, 5, 1, read_from_file('2/q_2_1.txt'), 18),
            (10, 5, 2, read_from_file('2/q_2_2.txt'), 18),
            (11, 6, 1, read_from_file('2/q_3_1.txt'), 19),
            (12, 6, 2, read_from_file('2/q_3_2.txt'), 17)]

#######################################################################################
#######################################################################################
#######################################################################################

cursor.executemany('''
  INSERT INTO lecturers(id, first_name, last_name)
              VALUES(?,?,?)''', lecturers)

cursor.executemany('''
  INSERT INTO exams(id, year, semester, is_second_chance, is_third_chance, duration)
              VALUES(?,?,?,?,?,?)''', exams)

cursor.executemany('''
  INSERT INTO exams_lecturers(exam_id, lecturer_id)
              VALUES(?,?)''', exams_lecturers)

cursor.executemany('''
  INSERT INTO questions(id, exam_id, question_number)
              VALUES(?,?,?)''', questions)

cursor.executemany('''
  INSERT INTO sections(id, question_id, section_number, question_text, score)
              VALUES(?,?,?,?,?)''', sections)

db.commit()
db.close()
