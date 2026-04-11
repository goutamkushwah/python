from os import chdir
from pathlib import Path
import os


def main() -> None:
    cwd = Path.cwd()
    home = Path.home()
    print(f"Current working directory: {cwd}")
    print(f"Home directory: {home}")

    # OS-specific path
    if os.name == "nt":
        path = Path(r"C:\Windows\System32\cmd.exe")
    else:
        path = Path("/usr/bin/python3")

    # reading file safely
    path = Path.cwd() / "settings.yaml"
    if path.exists():
        print(path.read_text())
    else:
        print("settings.yaml file not found!")

    # resolve path
    full_path = path.resolve()
    print(f"Full path: {full_path}")

    # file checks
    print(f"Is directory: {full_path.is_dir()}")
    print(f"Is file: {full_path.is_file()}")

    # create file
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch(exist_ok=True)
    new_file.write_text("Hello World!")

    # delete file
    new_file.unlink()

    # create directory
    new_dir = Path.cwd() / "new_dir"
    new_dir.mkdir(exist_ok=True)

    # change directory
    chdir(new_dir)
    print(f"Current working directory: {Path.cwd()}")

    # go back and delete directory
    chdir(Path.cwd().parent)
    new_dir.rmdir()


if __name__ == "__main__":
    main()