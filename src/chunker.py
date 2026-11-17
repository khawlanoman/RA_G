import os



def chunking(folder_vllm) -> None:
   
    text = (".txt",".h",".hpp",".sh",".json",".cpp",".cu",".cuh",
            ".cc",".toml",".yaml",".yml",".cfg",".ini",".sh")
    list_files_py = []
    list_files_markdown = []
    list_files_text = []
    for dirpath, dirname, filesname in os.walk(folder_vllm):

        for k in filesname:
            if k.endswith('.py'):
               list_files_py.append(os.path.join(dirpath,k))
            elif k.endswith('.md') or k.endswith('.rst'):
               list_files_markdown.append(os.path.join(dirpath,k))
            elif k.endswith(text):
               list_files_text.append(os.path.join(dirpath,k))
            else:
                continue
    return(list_files_py,list_files_markdown,list_files_text)


def chunk_py(py_file_list:list) -> None:
   
   try:
      all_chunks = []

      for k in py_file_list:

         with open(k) as file:
            lines = file.readlines()


      for l in lines:
         
   except Exception as er:
      print(er)