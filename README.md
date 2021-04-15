# flask-restful-demo

一个使用 flask-restful 写的 版本控制的小 demo

```
# 安装pipenv
pip install pipenv    # 全局安装

# 进入虚拟环境（需要在项目目录上执行，如果当前目录没有，则会新建）
pipenv shell  

# 退出虚拟环境
exit

# 使用pipenv按照类库
pipenv install #{package}

# 卸载类库
pipenv uninstall #{package}

# 查看按照包的依赖关系
pipenv graph

# 查看虚拟环境执行文件路径
pipenv --venv

# 安装 flask 
```

```
python3 run.py
curl http://localhost:5000/v1/hello
curl http://localhost:5000/v2/hello

```
