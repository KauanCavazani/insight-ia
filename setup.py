import os
import subprocess

def detect_python_executable():
    try:
        # Tenta usar python3
        subprocess.check_call(['python3', '--version'])
        return 'python3'
    except subprocess.CalledProcessError:
        pass
    except FileNotFoundError:
        pass

    try:
        # Tenta usar python
        subprocess.check_call(['python', '--version'])
        return 'python'
    except subprocess.CalledProcessError:
        pass
    except FileNotFoundError:
        pass

    raise EnvironmentError("Nenhum executável Python encontrado.")

def create_virtualenv(python_executable):
    if not os.path.exists('venv'):
        subprocess.check_call([python_executable, '-m', 'venv', 'venv'])
        print("Ambiente virtual criado com sucesso.")
    else:
        print("Ambiente virtual já existe.")

def install_requirements():
    pip_executable = os.path.join('venv', 'Scripts', 'pip') if os.name == 'nt' else os.path.join('venv', 'bin', 'pip')
    subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
    print("Dependências instaladas com sucesso.")

def setup_environment():
    python_executable = detect_python_executable()
    create_virtualenv(python_executable)
    install_requirements()

if __name__ == '__main__':
    setup_environment()
