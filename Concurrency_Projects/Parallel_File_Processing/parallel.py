import concurrent.futures
import threading
total_errors = 0
lock = threading.Lock()
log_files = {
    "file1.log": [
        "INFO: Server started",
        "ERROR: Database connection failed",
        "INFO: User logged in",
        "ERROR: Timeout occurred",
        "ERROR: Disk full"],  
    "file2.log": [
        "INFO: Process started",
        "ERROR: Network error",
        "WARNING: Low memory",
        "ERROR: API failure"],
    "file3.log": [
        "INFO: Login successful",
        "INFO: Data loaded",
        "ERROR: Invalid input"]
}
def process_file(filename):
    global total_errors 
    error_count = 0
    for line in log_files[filename]:
        if "ERROR" in line:
            error_count += 1
    print(f"{filename} -> {error_count} errors")
    with lock:
        total_errors += error_count
def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_file, log_files.keys())
    print(f"\nTotal Errors = {total_errors}")
if __name__ == "__main__":
    main()


# OUTPUT:
# file1.log -> 3 errors
# file2.log -> 2 errors
# file3.log -> 1 errors

# Total Errors = 6
