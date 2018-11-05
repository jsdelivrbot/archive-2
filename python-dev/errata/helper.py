import os

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir) if os.path.isdir(os.path.join(a_dir, name))]

def get_immediate_files(a_dir):
    return [name for name in os.listdir(a_dir) if not os.path.isdir(os.path.join(a_dir, name))]

class Helper:
  def __init__(self):
    tmp={}
    dirs = get_immediate_subdirectories('static/img/');
    for dir in dirs:
      tmp[int(dir)]=[]
      pages = get_immediate_files('static/img/' + dir)
      for page in pages:
        tmp[int(dir)].append(int(os.path.splitext(page)[0]))

    self.content = []
    for key in sorted(tmp.keys()):
      self.content.append([key, sorted(tmp[key])]);
    
  @property
  def Content(self):
    return self.content
