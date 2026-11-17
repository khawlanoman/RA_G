from .chunker import chunking, chunk_py


if __name__ == "__main__":
    folder_vllm ="./data/raw/vllm-0.10.1"

    py, mark,text = chunking(folder_vllm)
   
    print(chunk_py(py))