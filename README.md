# GPU Usage Manager

Single machine with one or multiple GPUs, record and visualize GPUs usage information.

## Get Start

##### Clone this project

```python
mkdir gpu_usage
cd gpu_usage
git clone git@github.com:LebinDing749/GPUs-Usage-Manager.git
cd GPUs-Usage-Manager
```

##### Install dependencies

```
# a python environment is needed
pip install pynvml
pip install psutil
```

##### Run backstage

```
nohup python gpu_monitor.py &
```

##### Cat process

```
ps -u {user} -f
#or 
jobs
# if there is 'python gpu_monitor.py', the precess is ruuning

# kill the process
ps -u {user} -f
kill -9 {pid}

or
jobs
kill -9 %{jobs_id}
```

# tip of kill all python command of a user
pkill -u {user} -f python

