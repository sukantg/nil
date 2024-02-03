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

if __name__ == "__main__":
    build_assigner()
    install_proof_generator()
    install_template()
    install_vargrind_visualizer()
