import os
import subprocess

def build_assigner():
    try:
        os.system("sudo apt install build-essential libssl-dev cmake clang-12 git curl pkg-config")
        os.system("git clone https://github.com/NilFoundation/zkLLVM.git")
        os.chdir('zkLLVM')
        
        # Using Ninja
        os.system('cmake -G "Ninja" -B build -DCMAKE_BUILD_TYPE=Release .')
        # C++ Compiler
        os.system("ninja -C build assigner clang -j$(nproc)")
        # Rust Compiler
        os.system('cmake -G "Ninja" -B build -DCMAKE_BUILD_TYPE=Release -DRSLANG_BUILD_EXTENDED=TRUE -DRSLANG_BUILD_TOOLS=cargo .')
        os.system("export LD_LIBRARY_PATH=\"$LD_LIBRARY_PATH:$(pwd)/build/libs/circifier/llvm/lib\"")
        os.system("ninja -C build rslang -j$(nproc)")
        
        # Check the version to verify install
        os.system("export RSLANG=\"$(pwd)/build/libs/rslang/build/host\"")
        os.system("RUSTC=$RSLANG/stage1/bin/rustc $RSLANG/stage1-tools-bin/cargo --version")
        
        print ("Assigner built successfully")

    except Exception as e:
        print(f"Error during assigner build: {e}")

def install_proof_producer():
    try:
        subprocess.run(["echo", "'deb [trusted=yes]  http://deb.nil.foundation/ubuntu/ all main'", ">>", "/etc/apt/sources.list"])
        subprocess.run(["apt", "update"])
        # Install dependencies
        subprocess.run(["sudo", "apt-get", "install", "-y", 
                        "build-essential", "liblz4-dev", "libgnutls28-dev", 
                        "libyaml-cpp-dev", "libsctp-dev", "ragel", 
                        "xfslibs-dev", "systemtap-sdt-dev", "libc-ares-dev", 
                        "libhwloc-dev", "libssl-dev", "libicu-dev", 
                        "libprotobuf-dev", "lsb-release", "gnutls-dev", 
                        "pkg-config", "lksctp-tools", "numactl"])
        
        subprocess.run(["mkdir", "build"])
        subprocess.run(["cd", "build"])
        subprocess.run(["cmake", ".."])
        subprocess.run(["make", "-j", "$(nrpoc)"])

        # Install the proof producer
        subprocess.run(["apt", "install", "proof-producer"])
        print ("Proof producer installed successfully.")

    except Exception as e:
        print(f"Error during proof generator install: {e}")

def install_template():
    try:
        print ("zkLLVM template installed successfully.")

    except Exception as e:
        print(f"Error during template install: {e}")

def install_vargrind_visualizer():
    try:
        # Install Valgrind and Massif-Visualizer
        subprocess.run(['sudo', 'apt-get', 'install', 'valgrind', 'massif-visualizer'], check=True)
        print("Valgrind and Massif-Visualizer installed successfully.")

    except Exception as e:
        print(f"Error during install: {e}")        

def file_updates(repo, main_cpp, main_input ):
    try:
        # Changing the main.cpp file with provided data
        final_cpp_path = os.path.join(repo, 'src', 'main.cpp')
        with open(main_cpp, 'r') as main_file:
            updated_cpp_content = main_file.read()
        with open(final_cpp_path, 'w') as final_cpp_file:
            final_cpp_file.write(updated_cpp_content)        

        # Changing the main_input.json file with provided data
        final_input_path = os.path.join(repo, 'src', 'main-input.json')
        with open(main_input, 'r') as main_file:
            updated_input_content = main_input.read()              
        with open(final_input_path, 'w') as final_input_file:
            final_input_file.write(updated_input_content)  

        print("main.cpp and main-input.json in '{repo}' updated successfully.")  

    except Exception as e:
        print(f"Error updating files: {e}")      

def circuit_compilation(repo):
    try:
        subprocess.run(["./scripts/run.sh", "--docker", "compile"], check=True)
        print("Circuit compiled successfully.")

    except Exception as e:
        print(f"Error running circuit: {e}")

def assigner_measurements(repo):
    # A byte-code file ./build/src/template.ll 
    # is generated on the circuit compilation step
    try:
        memory_result = subprocess.run(["valgrind", "--tool=massif", "assigner", "-b", "build/src/template.ll", "-p"], capture_output=True, text=True)
        time_result = subprocess.run(["time", "assigner", "-b", "build/src/template.ll", "-p", "./src/main-input.js"], capture_output=True, text=True)
        print(f"Assigner memory: {memory_usage:.1f} GB")
        print(f"Assigner time: {time:.1f} s")

    except Exception as e:
        print(f"Error getting assigner measurements: {e}")
    

def proof_measurements(repo):
    try:
        print(f"Proof memory: {memory_usage:.1f} GB")
        print(f"Proof generator time: {time:.1f} s") 
     
    except Exception as e:
        print(f"Error getting Proof measurements: {e}")
       

if __name__ == "__main__":
    build_assigner()
    install_proof_producer()
    install_template()
    install_vargrind_visualizer()
    file_updates("./zkllvm-template","updated_main.txt","updated_main_input.json")
    circuit_compilation("./zkllvm-template")
    assigner_measurements("./zkllvm-template")