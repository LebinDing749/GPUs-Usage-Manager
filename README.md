# GPU Usage Manager

Single machine with one or multiple GPUs, record and visualize GPUs usage information.

## Get Start

##### Clone this project

```python
mkdir gpu_usage
git clone 
```

##### Install dependencies

```
# a python environment is needed
pip install pynvml
pip install psutil
```

##### Run backstage

```
python gpu_monitor.py
```

##### Cat process

```
ps -u {user} -f
# if there is 'python gpu_monitor.py', the precess is ruuning

# kill the process
kill -9 {pid}
```

