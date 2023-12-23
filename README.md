# Documentation Retrieval

![image](https://miro.medium.com/v2/resize:fit:50/format:webp/1*OARpkeBkn_Tw3vk8H769OQ.png)
![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)
![image](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)

With this app, you can upload your PDF file and search for a specific words, phrase and etc. The main algorithm can describe bellow:\

![image](https://github.com/shirindehghani/Information-Retrieval/blob/main/imgs/algorithm.png)


## Deployment
To deploy this project run: \
1: clone the repository:
```bash
git clone git@github.com:shirindehghani/Information-Retrieval.git
```

2: install requirements
```bach
pip install -r requirement.txt 
```

3: Enter your openai api_key on "configs/configs.json" directory

## Docker
For build an image please run: 
```bash
docker build -t your-image-name .
```
