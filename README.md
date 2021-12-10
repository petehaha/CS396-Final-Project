# Linguistics-Final-Project

## Installation

- Clone the repo
``` sh
git clone https://github.com/wenet-e2e/wenet.git
```

- Install Conda: please see https://docs.conda.io/en/latest/miniconda.html
- Create Conda env:

``` sh
conda create -n wenet python=3.8
conda activate wenet
pip install -r requirements.txt
conda install pytorch=1.10.0 torchvision torchaudio=0.10.0 cudatoolkit=11.1 -c pytorch -c conda-forge
```

- To use the x86 runtime, run

``` sh
# runtime build requires cmake 3.14 or above
cd wenet/runtime/server/x86
mkdir build && cd build && cmake .. && cmake --build .
```

- To run an audio file, run

```sh
export GLOG_logtostderr=1
export GLOG_v=2
wav_path=your_test_wav_path
model_dir=your_model_dir
```

replacing `your_test_wav_path` with the wav path of your file, at a 16000Hz sampling rate and with mono channels.
and replacing `model_dir` with the upper-most directory of the model which can be downloaded [here](http://mobvoi-speech-public.ufile.ucloud.cn/public/wenet/gigaspeech/20210728_u2pp_conformer_server.tar.gz).

- Then, run 

```sh
./build/decoder_main \
    --chunk_size -1 \
    --wav_path $wav_path \
    --model_path $model_dir/final.zip \
    --dict_path $model_dir/words.txt 2>&1 | tee log.txt
```

using `--output_nbest` if you would like to output the n-best results of the model, and `--result file_name` to store the output.

- To run WER analysis, call `wer.py` with the following arguments

```sh
python wer.py reference_file prediction_file
```

keep in mind that the prediction file outputted by the model includes the word "test" at the beginning of every run.
