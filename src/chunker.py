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
