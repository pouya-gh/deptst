from datetime import datetime
import getpass

if __name__ == "__main__":
    with open("output.txt", "w") as f:
        f.write(f"Hello, {getpass.getuser()}! (time {datetime.now()})\n")