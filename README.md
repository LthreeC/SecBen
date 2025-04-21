# SecBen

The open FinLLM leaderboard are available on [SecBen](https://huggingface.co/spaces/lthc/secben).

SecBen is a comprehensive cybersecurity benchmark featuring 12 datasets and 18k samples, with pre-defined labels and extensible metrics. 

Sourced from high-quality open-source corpora and expert-annotated prompts, it evaluates LLMs across three skill levels based on Bloom's cognitive model: CyberKUT, CyberNLP, and CyberDSA.

## Tasks

| Task       | Language | Dataset     | Size | Metrics             | Length Type | NLP Type            | License         |
|------------|----------|-------------|------|---------------------|-------------|---------------------|-----------------|
| CyberKUT   | zh       | NetQA       | 2000 | ROUGE, BERTScore    | Sentence    | Generation (GEN)    | WTFPL           |
| CyberKUT   | en       | Embed       | 1539 | ROUGE, BERTScore    | Sentence    | Generation (GEN)    | Public          |
| CyberKUT   | en       | Metric      | 2558 | ACC, F1             | Sentence    | Classification (CLS)| Public          |
| CyberKUT   | zh       | CodeQA      | 2000 | CodeBERTScore       | Paragraph   | Generation (GEN)    | CC-BY-NC-4.0    |
| CyberNLP   | en       | Corpus      | 200  | ACC, F1             | Sentence    | Classification (CLS)| Public          |
| CyberNLP   | zh       | CDTier      | 520  | ACC, F1             | Paragraph   | Classification (CLS)| Public          |
| CyberNLP   | en       | NER         | 841  | EntityF1            | Paragraph   | Reasoning (REA)     | MIT License     |
| CyberNLP   | en       | HackerNews  | 748  | ROUGE, BERTScore    | Passage     | Generation (GEN)    | Public          |
| CyberDSA   | en       | MaliURLs    | 2000 | ACC, F1             | Sentence    | Classification (CLS)| Public          |
| CyberDSA   | en       | CSIC2010    | 2000 | ACC, F1             | Paragraph   | Classification (CLS)| Public          |
| CyberDSA   | en       | BETH        | 2000 | ACC, F1             | Paragraph   | Classification (CLS)| Public          |
| CyberDSA   | en       | MITRE       | 2000 | ACC, F1             | Sentence    | Classification (CLS)| Apache-2.0      |

## LLMs

| Model            | Parameters | Pre-trained | Fine-tuned | Access   | Base LLM              | Release Date  |
|------------------|------------|-------------|------------|----------|-----------------------|---------------|
| Gemma            | 7B         | ✓           | ✗          | Weights  | –                     | 06/27/2024    |
| Llama3           | 8B         | ✓           | ✗          | Weights  | –                     | 04/18/2024    |
| Mistral-V0.3     | 7B         | ✓           | ✗          | Weights  | –                     | 05/22/2024    |
| ChatGPT          | 175B       | ✓           | ✗          | API      | –                     | 11/30/2022    |
| Atom             | 7B         | ✗           | ✓          | Weights  | LLaMA2-7B             | 08/28/2023    |
| Baichuan2        | 7B         | ✓           | ✗          | Weights  | –                     | 09/06/2023    |
| DeepSeek-R1      | 7B         | ✗           | ✓          | Weights  | Qwen2.5-Math-7B       | 02/09/2025    |
| ERNIE-3.5-8K     | ~1000B     | ✓           | ✗          | API      | –                     | 07/01/2024    |
| GLM-4            | 9B         | ✓           | ✗          | Weights  | –                     | 06/05/2024    |
| InternLM2        | 7B         | ✓           | ✗          | Weights  | –                     | 01/17/2024    |
| Qwen2            | 7B         | ✓           | ✗          | Weights  | –                     | 06/06/2024    |
| Yi               | 6B         | ✓           | ✗          | Weights  | –                     | 11/02/2023    |
| AutoAudit        | 7B         | ✗           | ✓          | Weights  | Alpaca-Lora-7B        | 07/03/2023    |
| SecGPT           | 13B        | ✗           | ✓          | Weights  | Baichuan-13B          | 11/22/2023    |


## Overall Results

| Model          | Cybersecurity Task |              |              | NLP Main Task |              |              | Overall |
|----------------|--------------------|--------------|--------------|---------------|--------------|--------------|---------|
|                | CyberKUT           | CyberNLP     | CyberDSA     | CLS           | GEN          | REA          |         |
| Gemma          | 0.255              | 0.175        | 0.325        | 0.263         | 0.254        | 0.000        | 0.250   |
| Llama3         | 0.312              | 0.149        | 0.222        | 0.198         | 0.295        | 0.000        | 0.242   |
| Mistral-V0.3   | 0.230              | 0.141        | 0.285        | 0.235         | 0.218        | 0.001        | 0.219   |
| ChatGPT        | **0.513**          | 0.461        | 0.599        | 0.617         | **0.458**    | 0.154        | 0.520   |
| Atom           | 0.277              | 0.095        | 0.166        | 0.135         | 0.261        | 0.000        | 0.196   |
| Baichuan2      | 0.191              | 0.133        | 0.168        | 0.170         | 0.178        | 0.000        | 0.168   |
| DeepSeek-R1    | 0.355              | 0.244        | 0.341        | 0.321         | 0.338        | 0.000        | 0.319   |
| ERNIE-3.5-8K   | 0.503              | **0.518**    | **0.613**    | **0.661**     | 0.443        | **0.269**    | **0.536** |
| GLM-4          | 0.445              | 0.459        | 0.544        | 0.578         | 0.402        | 0.203        | 0.475   |
| InternLM2      | 0.377              | 0.347        | 0.451        | 0.425         | 0.378        | 0.007        | 0.387   |
| Qwen2          | 0.367              | 0.260        | 0.368        | 0.329         | 0.363        | 0.002        | 0.336   |
| Yi             | 0.244              | 0.202        | 0.291        | 0.280         | 0.226        | 0.021        | 0.244   |
| AutoAudit      | 0.186              | 0.153        | 0.164        | 0.170         | 0.182        | 0.000        | 0.171   |
| SecGPT         | 0.357              | 0.132        | 0.311        | 0.242         | 0.330        | 0.000        | 0.280   |


## Detailed Results



## Evaluation

### Preparation

#### Locally install
```bash
cd SecBen
pip install -r requirements.txt
cd src/sec-evaluation
pip install -e .[multilingual]
```

#### Automated Task Assessment

Evaluate model hosted on HuggingFace
```bash
bash scripts/run_evaluation.sh
```

or 

Use Commercial API
```bash
bash scripts/run_api.sh
```

### Create new tasks

Creating a new task for FinBen involves creating a Huggingface dataset and implementing the task in a Python file. This guide walks you through each step of setting up a new task using the FinBen framework.

#### Creating your dataset in Huggingface

Your dataset should be created in the following format:

```python
{
    "query": "...",
    "answer": "...",
    "text": "..."
}
```

In this format:

- `query`: Combination of your prompt and text
- `answer`: Your label
- `choices`: Set of labels
- `gold`: Index of the correct label in choices (Start from 0)
- `label`: List of token labels
- `token`: List of tokens
- `label`: List of sentence labels