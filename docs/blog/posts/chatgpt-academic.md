---
date: 2023-10-20
authors:
  - haiiliin
categories:
  - Academic
tags:
  - Python
comments: true
---

# 配置使用 ChatGPT Academic

## 离线安装包

你可以到 [GitHub Release](https://github.com/haiiliin/chatgpt-academic/releases) 页面下载 ChatGPT Academic 的离线安装包，解压后安装即可使用。

## 使用 Python 安装

首先，你需要安装 Python，可以从 [Python 官网](https://www.python.org/downloads/) 下载 Python 3.8 - 3.11 安装包（Python 3.12 暂不支持）。
安装时注意勾选 `Add Python to PATH` 选项将 Python 安装路径添加到环境变量 `PATH` 中。
安装完成后，打开命令行窗口 `cmd`，输入 `python --version`，如果显示 Python 版本号，则说明安装成功。使用以下命令安装 `chatgpt-academic`：

```sh
python -m pip install chatgpt-academic
```

## 配置环境变量

安装完成后，使用环境变量配置 ChatGPT Academic 项目，具体可查阅 [gpt-academic 项目文档](https://github.com/binary-husky/gpt_academic/wiki/项目配置说明)。
例如，配置 `gpt-3.5-turbo` 等 `OpenAI` 模型时，设置名为 `API_KEY` 的环境变量，值为 `OpenAI` 的 API 密钥，如：

```
sk-123456789xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx123456789
```

若需使用第三方代理服务提供的 `OpenAI` 模型，还需配置 `API_URL_REDIRECT` 环境变量，如：

```
{"https://api.openai.com/v1/chat/completions": "https://reverse-proxy-url/v1/chat/completions"}
```

配置完成后，在命令行窗口输入 `chatgpt-academic` 或 `gpta` 命令，即可启动 ChatGPT Academic 项目。
`chatgpt-academic.exe` 和 `gpta.exe` 可执行文件位于 Python 安装目录下的 `Scripts` 文件夹中，如：

```
C:\Users\{username}\AppData\Local\Programs\Python\Python311\Scripts
```

`{username}` 为当前用户名，`Python311` 为 Python 版本号。你可以为 `chatgpt-academic` 或 `gpta` 命令创建快捷方式，方便启动项目。