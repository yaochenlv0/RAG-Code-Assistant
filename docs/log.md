# 项目迭代优化记录
## 2026-04-25 第一次创建仓库
### 问题
建立成长型项目，用于记录RAG代码仓库智能问答系统的代码和迭代优化过程
### 解决方案
创建GitHub仓库
建立基本的项目结构
## 2026-04-26 写初始代码
### 初始代码的主要功能
根据提供的文本地址，读取文本文件，然后对文本文件通过调用deepseek模型进行概括，打印概括内容，并保存
### 问题1 
'Chat' object has no attribute 'Completions'
### 解决方案
`client.chat.Completions.create`中的Completions的首字母应该小写，改为`client.chat.completions.create`
### 问题2
TypeError: write() argument must be str, not None
### 解决方案
根本错误原因在于response.choices[0].message.content()的括号不应该加",",去掉即可