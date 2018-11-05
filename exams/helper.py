import os

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def get_immediate_files(a_dir):
    return [name for name in os.listdir(a_dir) if not os.path.isdir(os.path.join(a_dir, name))]

class Helper:
  def __init__(self):
    exam_path = '/home/amir/workspace/repositories/gingolda/exams/tau/0366-1111/15-16-1-1/'
    self.content = []
    questions = get_immediate_subdirectories(exam_path)
    for question in questions:
      question_path = exam_path + '/' + question +  '/'
      current_question = []
      sections = get_immediate_subdirectories(question_path)
      for section in sections:
        section_path = question_path + '/' + section +  '/'
        myFile = open(section_path + '/' + 'question.txt')
        question_text = myFile.read()
        myFile.close()
        current_question.append([question_text])
      self.content.append(current_question)

  @property
  def Content(self):
    return self.content
