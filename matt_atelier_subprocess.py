# %%
########### exemple de creation de projet python

from pathlib import Path
import subprocess

def create_new_project(name):
    project_folder = Path.cwd().absolute() / name
    project_folder.mkdir()
    # création de fichier avec Path
    (project_folder / "README.md").touch()
    with open(project_folder / ".gitignore", mode="w") as f:
        f.write("\n".join(["v_env/", "__pycache__/"]))
    # commandes tokenisées
    commands = [
        [
            "python",
            "-m",
            "venv",
            f"{project_folder}/v_env",
        ],
        ["git", "-C", project_folder, "init"],
        ["git", "-C", project_folder, "add", "."],
        ["git", "-C", project_folder, "commit", "-m", "root commit"],
    ]
    for command in commands:
        try:
            # check True => déclenche une exception en cas de code de retour non-zero
            subprocess.run(command, check=True, timeout=60)
        except FileNotFoundError as exc:
            print(
                f"Command {command} failed because the process "
                f"could not be found.\n{exc}"
            )
        except subprocess.CalledProcessError as exc:
            print(
                f"Command {command} failed because the process "
                f"did not return a successful return code.\n{exc}"
            )
        except subprocess.TimeoutExpired as exc:
            print(f"Command {command} timed out.\n {exc}")


if __name__ == "__main__":
    # create_new_project("toto")
    # process = subprocess.run(["git", "status", "--short"], capture_output=True)
    # idem
    process = subprocess.run(
        ["git", "status", "--short"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    print(process.stdout.decode("utf-8"))
    # utiliser les flux
    # process = subprocess.run(
    #     ["bash", "-c", "ls /usr/bin | grep python3"],
    #     capture_output=True
    # )
    # ou
    # process = subprocess.run(
    #     ["ls /usr/bin | grep python3"],
    #     shell=True,
    #     capture_output=True
    # )
    # ou
    ls_process = subprocess.run(
        ["ls", "/usr/bin"],
        stdout=subprocess.PIPE
    )
    grep_process = subprocess.run(
        ["grep", "python"],
        input=ls_process,
        stdout=subprocess.PIPE
    )
    print(grep_process.stdout.decode("utf-8"))

