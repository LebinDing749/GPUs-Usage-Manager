import csv

'''
2024-04-30 09:46:00
GPU0,3.92340087890625,24.0,20.07659912109375
zongyu,2048250,3867148288
GPU1,0.32183837890625,24.0,23.67816162109375
GPU2,0.32183837890625,24.0,23.67816162109375
GPU3,0.32183837890625,24.0,23.67816162109375

'''
def onetime_info(start_index, lines, lines_len):
    time = lines[start_index]
    gpu_info = []
    user_info = []
    next_satrt_index = 0
    for i in range(start_index+1, lines_len):
        line = lines[i]
        if line == []:
            next_start_index = i + 1
            break
        elif line[0].startswith('GPU'):
            gpu_info.append(line)
        else:
            user_info.append(line)
        
    return time, gpu_info, user_info, next_start_index

if __name__ == '__main__':
    time_info = []
    gpus_info = []
    users_info = []
    with open('gpu_monitor.csv', 'r') as file:
        lines = list(csv.reader(file))
        index = 0
        lines_len = len(lines)
        
        while index < lines_len:
            time, gpu_info, user_info, index = onetime_info(index, lines, lines_len)
            time_info.append(time)
            gpus_info.append(gpu_info)
            users_info.append(user_info)
    
    print(time_info[0])
    print(gpus_info[0])
    print(users_info[0])        
