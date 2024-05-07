import pynvml
import csv
import psutil
from datetime import datetime
import time

def write_gpu_info():
    # gpu_info = [
    #    [gpuid, xx, xx],
    #    [gpuid, xx, xx],
    #    [gpuid, xx, xx],
    #    [gpuid, xx, xx],
    #    [username, pid, xx]
    #    ...
    #]
    GPU_info = []
    current_time = datetime.now()
    GPU_info.append([current_time.strftime('%Y-%m-%d %H:%M:%S')])
        
    for i in range(device_count):
        # GPU info
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        # gpu_name = pynvml.nvmlDeviceGetName(handle)
        gpu_memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        
        # B -> GB
        used_memory = gpu_memory_info.used / 1024**3
        total_memory = gpu_memory_info.total / 1024**3
        free_memory = gpu_memory_info.free / 1024**3
        
        single_GPU_info = [f'GPU{i}', used_memory, total_memory, free_memory]
        GPU_info.append(single_GPU_info)
        
        # info of process on this GPU
        running_processes = pynvml.nvmlDeviceGetComputeRunningProcesses(handle) 
        for process in running_processes:
            pid = process.pid
            username = psutil.Process(pid).username()
            usedGpuMemory = process.usedGpuMemory
            GPU_info.append([username, pid, usedGpuMemory])

    # save info
    with open('gpu_monitor.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(GPU_info)
        writer.writerow([])

        # print(GPU_info)
        

if __name__ == '__main__':
    
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    csv_file = "gpu_usage.csv"

    while True:
        # print('log ')
        write_gpu_info()
        time.sleep(900) # 15 min
    else:
        pynvml.nvmlShutdown()

    pynvml.nvmlShutdown()   