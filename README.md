# Concurrent Python

A minimal example of concurrent Python. Please refer to my [blog post](https://hfyeh.github.io/posts/a-minimal-example-of-concurrent-python) for detail explain.

### Single Thread Version

```shell
time python3 0_single_thread.py
```

### Multi-thread Version

```shell
time python3 1_multi_thread.py
```

### Multi-process Version

```shell
time python3 2_multi_process.py
```

### Multi-process with shell

```shell
time (python3 3_mp_mul.py | python3 3_mp_add.py)
```

