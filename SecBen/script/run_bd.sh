# !bin/bash
set -x
model="ERNIE-3.5-8K"
url=""
tasks=$1

model_name=$model # This actually is real model_name
max_gen_toks=500
temperature=0.5

# only max_gen_toks
python ../src/eval.py \
    --model "$model" \
    --url "$url" \
    --tasks "$tasks" \
    --model_args max_gen_toks=$max_gen_toks,temperature=$temperature \
    --no_cache \
    --write_out \
    --output_path "../outputs" \
    --output_base_path "$model_name"
