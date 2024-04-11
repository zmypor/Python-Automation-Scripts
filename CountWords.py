def count_words(file_path):
  with open(file_path, 'r') as f:
    text = f.read()
    word_count = len(text.split())
  return word_count