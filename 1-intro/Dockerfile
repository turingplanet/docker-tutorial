# 将 image 文件继承与官方的3.7版本的Python
FROM python:3.7
# 将当前目录下的所有文件（除了 .dockerignore 排除的路径），都拷贝进 image 文件的 /app 目录。
COPY . /app 
# 指定接下来的工作路径为 /app
WORKDIR /app 
# 在 /app 目录下，运行 python 文件
CMD python3 hello.py 
