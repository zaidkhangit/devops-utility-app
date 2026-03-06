import psutil

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    cpu_threshold = 10
    if cpu_percent > cpu_threshold:
        status = "high cpu"
    else:
        status ="healthy"
    return {
        "cpu percent": cpu_percent,
        "virtual memory ": memory_percent,
        "cpy threshold": cpu_threshold,
        "system status": status
    }