import re


def analyze_log_file(filename="access.log"):
    try:
        with open(filename, "r") as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    url_counts = {}
    unique_ips = set()
    error_count = 0

    for line in log_lines:
        _, ip, url, status = extract_log_data(line)
        if ip and url and status:
            unique_ips.add(ip)
            url_counts[url] = url_counts.get(url, 0) + 1
            if int(status) >= 400:
                error_count += 1

    print(f"\n📊 Log File Summary:")
    print(f"🔴 Total Errors (4xx and 5xx): {error_count}")
    print(f"🧠 Unique IP Addresses: {len(unique_ips)}")
    print("📄 URL Access Counts:")
    for url, count in url_counts.items():
        print(f"    {url}: {count}")


def extract_log_data(line):
    match = re.search(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - "
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
        r"\"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        return match.groups()
    return None, None, None, None


# Run the analyzer
if __name__ == "__main__":
    analyze_log_file()

