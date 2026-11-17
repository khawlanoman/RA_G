from .chunker import chunking


if __name__ == "__main__":
    folder_vllm ="./data/raw/vllm-0.10.1"
    print(chunking(folder_vllm))