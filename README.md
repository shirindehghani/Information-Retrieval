# Doc Retrieval

![image](https://miro.medium.com/v2/resize:fit:50/format:webp/1*OARpkeBkn_Tw3vk8H769OQ.png)
![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)
![image](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)

With this app, you can upload your PDF file and search for a specific words, phrase and etc. The main algorithm can describe bellow:

![image](https://github.com/shirindehghani/Information-Retrieval/blob/main/imgs/algorithm.png)

# Deployment
To deploy this project run

1: Clone this repository:
```bash
git clone git@github.com:shirindehghani/Information-Retrieval.git
```
2: install requirements
```bash
pip install -r requirements.txt
```


# Docker
Run bellow command to make docker image:
```bash
docker build -t your_image_name .
```

You can also use this app base on streamlit UI:
link : https://information-retrieval-app.streamlit.app/

You should import you OpenAI api_key, input query and a PDF file:

![image](https://github.com/shirindehghani/Information-Retrieval/blob/main/imgs/Ui.png)

### Project Structure
```
|──IR_models ──|──Retrieval.py
|──configs ──|──configs.json
|──imgs ──|──algorithm.png
|         |──Ui.png
|──temp ──|──PDF-file.pdf
|──needded_pkgs ──|──Log-Handler
|──app.py
|──docker-compose.yml
|──Dockerfile
|──LICENCE
|──main.py
|──main2.py
|──README.md
|──requirements.txt
|──test_app.py
```

#### TODO:
- add LLMs like llama2, mistral and etc. for chat with PDF!
- Improve the UI
- Speed up the process

# References
```

@article{zhu2023large,
  title={Large language models for information retrieval: A survey},
  author={Zhu, Yutao and Yuan, Huaying and Wang, Shuting and Liu, Jiongnan and Liu, Wenhan and Deng, Chenlong and Dou, Zhicheng and Wen, Ji-Rong},
  journal={arXiv preprint arXiv:2308.07107},
  year={2023}
}
```
