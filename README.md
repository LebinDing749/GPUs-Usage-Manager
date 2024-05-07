# GPU Usage Manager

Single machine with one or multiple GPUs, record and visualize GPUs usage information.

## Get Start

##### Clone this project

```python
mkdir gpu_usage
cd gpu_usage
git clone git@github.com:LebinDing749/GPUs-Usage-Manager.git
```

##### Install dependencies

```
# a python environment is needed
pip install pynvml
pip install psutil
```

##### Run backstage

```
nohup python gpu_monitor.py
```

##### Cat process

```
ps -u {user} -f
# if there is 'python gpu_monitor.py', the precess is ruuning

# kill the process
kill -9 {pid}
```

