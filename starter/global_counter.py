counter = 0

def increment_counter() -> None:
    global counter
    counter += 1
    
def check_threshold(threshold: int) -> bool:
    global counter
    return counter > threshold

if __name__ == "__main__":
    increment_counter()
    increment_counter()
    increment_counter()
    print("Counter:", counter)
    print("Threshold 2:", check_threshold(2))
    print("Threshold 5:", check_threshold(5))