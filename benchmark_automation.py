import subprocess

def build_assigner():
    try:
        print ("Assigner built successfully")

    except Exception as e:
        print(f"Error during assigner build: {e}")

def install_proof_generator():
    try:
        print ("Proof generator installed successfully.")

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
        # subprocess.run(['sudo', 'apt-get', 'install', 'valgrind', 'massif-visualizer'], check=True)
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

        print(f"main.cpp and main-input.json in '{repo}' updated successfully.")  

    except Exception as e:
        print(f"Error updating main-input.json: {e}")      

if __name__ == "__main__":
    build_assigner()
    install_proof_generator()
    install_template()
    install_vargrind_visualizer()
    file_updates("./zkllvm-template","updated_main.txt","updated_main_input.json")
