from dataclasses import dataclass

@dataclass
class ModuleProgress:
    state: str = "Introductory Exercises"
    attempts: int = 0

def complete_task(m: ModuleProgress) -> None:
    if m.state == "Introductory Exercises":
        m.state = "Project"
    elif m.state == "Project":
        m.state = "Benchmark"
    elif m.state == "Benchmark":
        print("Error: Invalid transition")
    else:
        print(f"Error: Invalid transition")

def pass_task(m: ModuleProgress) -> None:
    if m.state == "Benchmark":
        m.state = "Module Complete"
        m.attempts = 0
    else:
        print(f"Error: Invalid transition")

def fail_task(m: ModuleProgress) -> None:
    if m.state == "Benchmark" and m.attempts == 2:
        m.state = "Failed"
    elif m.state == "Benchmark":
        m.state = "Project"
        m.attempts += 1
    else:
        print(f"Error: Invalid transition")



def main() -> None:
    progress = ModuleProgress()

    while progress.state != "Module Complete" and progress.state != "Failed":
        print(f"Current State: {progress.state}")
        action = input("> ").lower()
        if action != "pass" and action != "fail" and action != "complete":
            print("Error: Invalid action")
        elif progress.state == "Introductory Exercises":
            if action == "complete":
                complete_task(progress)
            else:
                print("Error: Invalid transition")
        elif progress.state == "Project":
            if action == "complete":
                complete_task(progress)
            else:
                print(f"Error: Invalid transition")
        elif progress.state == "Benchmark":
            if action == "pass":
                pass_task(progress)
            elif action == "fail":
                fail_task(progress)
            else:
                print(f"Error: Invalid transition")
    print(f"Current State: {progress.state}")
if __name__ == "__main__":
    main()