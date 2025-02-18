# Evaluation with LMDeploy

We now support evaluation of models accelerated by the [LMDeploy](https://github.com/InternLM/lmdeploy). LMDeploy is a toolkit designed for compressing, deploying, and serving LLM. **TurboMind** is an efficient inference engine proposed by LMDeploy. OpenCompass is compatible with TurboMind. We now illustrate how to evaluate a model with the support of TurboMind in OpenCompass.

## Setup

### Install OpenCompass

Please follow the [instructions](https://opencompass.readthedocs.io/en/latest/get_started.html) to install the OpenCompass and prepare the evaluation datasets.

### Install LMDeploy

Install lmdeploy via pip (python 3.8+)

```shell
pip install lmdeploy
```

## Evaluation

We take the InternLM as example.

### Step-1: Get InternLM model

```shell
# 1. Download InternLM model(or use the cached model's checkpoint)

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/internlm/internlm-chat-7b /path/to/internlm-chat-7b

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1

# 2. Convert InternLM model to turbomind's format, which will be in "./workspace" by default
python3 -m lmdeploy.serve.turbomind.deploy internlm-chat-7b /path/to/internlm-chat-7b

```

### Step-2: Launch Triton Inference Server

```shell
bash ./workspace/service_docker_up.sh
```

\*\*Note: \*\*In the implementation of turbomind, inference is "persistent". The "destroy" operation can lead to unexpected issues. Therefore, we temporarily use service interfaces for model evaluation. And we will integrate the Python API to OpenCompass when turbomind supports "destroy".

### Step-3: Evaluate the Converted Model

In the home folder of OpenCompass

```shell
python run.py configs/eval_internlm_chat_7b_turbomind.py -w outputs/turbomind
```

You are expected to get the evaluation results after the inference and evaluation.

\*\*Note: \*\*In `eval_internlm_chat_7b_turbomind.py`, the configured Triton Inference Server (TIS) address is `tis_addr='0.0.0.0:33337'`. Please modify `tis_addr` to the IP address of the machine where the server is launched.
