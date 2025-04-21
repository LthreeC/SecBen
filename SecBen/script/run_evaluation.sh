model_path="/mnt/e/1DATA/models/openai-community_gpt2"
model_name=$(basename "$model_path") # This actually is real model_name

tasks="_frame__NER_29_cyner_TEST"


python ../src/eval.py \
    --model hf-causal-vllm \
    --tasks "$tasks" \
    --model_args use_accelerate=True,pretrained=$model_path,tokenizer=$model_path,use_fast=False,max_gen_toks=150,dtype=float16,trust_remote_code=True \
    --no_cache \
    --batch_size 1 \
    --output_path "../outputs" \
    --write_out \
    --output_base_path "$model_name"
