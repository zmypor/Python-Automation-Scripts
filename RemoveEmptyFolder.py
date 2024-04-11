def remove_empty_folders(directory_path):
  for root, dirs, files in os.walk(directory_path, topdown=False):
    for folder in dirs:
      folder_path = os.path.join(root, folder)
      if not os.listdir(folder_path):
        os.rmdir(folder_path)