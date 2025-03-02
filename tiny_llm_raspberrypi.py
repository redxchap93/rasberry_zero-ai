import os
import subprocess
import urllib.request

# Define constants
MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-GGUF/resolve/main/tinyllama-1b-chat.Q4_K_M.gguf"
MODEL_NAME = "tinyllama-1b-chat.Q4_K_M.gguf"
LLAMA_CPP_REPO = "https://github.com/ggerganov/llama.cpp"

def install_dependencies():
    """Installs necessary dependencies on Raspberry Pi Zero."""
    print("🔹 Updating system and installing dependencies...")
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system("sudo apt install -y python3-pip git cmake make g++")

def clone_and_build_llama_cpp():
    """Clones and compiles llama.cpp for efficient inference."""
    if not os.path.exists("llama.cpp"):
        print("🔹 Cloning llama.cpp repository...")
        os.system(f"git clone {LLAMA_CPP_REPO}")
    
    print("🔹 Building llama.cpp for Raspberry Pi Zero...")
    os.system("cd llama.cpp && make -j4")

def download_model():
    """Downloads and saves the TinyLLama model in GGUF format."""
    if not os.path.exists(MODEL_NAME):
        print(f"🔹 Downloading {MODEL_NAME} (this may take a while)...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_NAME)
        print("✅ Model downloaded successfully!")
    else:
        print("✅ Model already exists. Skipping download.")

def run_llm():
    """Runs the TinyLLama model for testing."""
    print("🚀 Running TinyLLama on Raspberry Pi Zero...")
    command = f"./llama.cpp/main -m {MODEL_NAME} -p 'Hello, what can you do?'"
    process = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("\n🧠 AI Response:\n", process.stdout)

def main():
    """Main function to execute all steps."""
    print("🛠️ Setting up TinyLLM on Raspberry Pi Zero ($10 AI!)")
    install_dependencies()
    clone_and_build_llama_cpp()
    download_model()
    run_llm()
    print("✅ TinyLLM is now running on Raspberry Pi Zero!")

if __name__ == "__main__":
    main()
