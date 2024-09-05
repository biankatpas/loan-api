import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    return result


if __name__ == "__main__":
    run_command("black .")
    run_command("isort .")
