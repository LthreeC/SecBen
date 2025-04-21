# !bin/bash
set -x
model="deepseek-chat"
url=""

tasks=$1

model_name=$model # This actually is real model_name
max_gen_toks=$2
temperature=0

python ../src/eval.py \
    --model "$model" \
    --url "$url" \
    --tasks "$tasks" \
    --model_args max_gen_toks=$max_gen_toks,temperature=$temperature \
    --no_cache \
    --write_out \
    --output_path "../outputs" \
    --output_base_path "$model_name"
