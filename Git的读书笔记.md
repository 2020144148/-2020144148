---

---



#                             Git的读书笔记



#### 班级：20201441                      学号：2020144148                   姓名：曾朝勇

#### 一、Git基本概念：

- git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。 也是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件
- .git的目录保存元数据和对象数据库的地方。克隆镜像仓库的时候，实际拷贝的就是该目录
- 从项目中取出某个版本的所以文件和目录，用以开始后续工作的叫做工程目录
- Git并不保存这些文件前后的差异数，而是保存每次更新时的文件快照

#### 二、Git工作流程：

- ##### 基本工作流程
  
   1.工作目录中修改某些文件
   2.对修改后的文件进行快照，然后保存到暂存区域
   3.提交更新，将文件快照永久转储到Git目录
   
- ##### git在本地实际上维护了“三棵树”：
  
   1.工作目录：持有实际文件
   2.缓存区（Index）：临时保存你的改动
   3.Head：最后一次提交后的结果
   

#### 三、简单命令

- 建立一个文件夹

  ```
  mkdir learngit
  cd learngit
  pwd
  ```

- 编写一个程序，并建立git仓库

```python
vim ex_03_01.py
git init
```

- 将源代码文件加入git仓库并确认，同时添加备注信息

```python
git add ex_03_01.py
git commit -M "wrote the first rersion of exercise 3-1"
```

- 提交修改后的程序并修改

```python
git add ex_03_01.py
git commit -M "add try/except to capture traceback"
git status
```

- 检查当前文件状态

```python
git status
```



- 跟踪新文件，或把已跟踪文件放到暂存区

```python
git add [filename]
```



- 要查看尚未暂存的文件更新了哪些部分

```python
git diff
```

- 查看已暂存文件和上次提交快照之间的差异

```python
git diff -- cached
```

- 提交更新


```python
git commit
或者
git commit -m '提交的说明注释'
```

- 跳过 git add 直接提交

```python
git commit -a
```

- 移除文件

```python
git rm [filename]
```

- 从Git仓库中删除，但仍保留在当前工作目录

```python
git rm -- cached [filename]
```

- 移动文件

```python
git mv [file_name_from] [file_name_to]
```

- 版本回退

```python
git log

```

- 查看所有commit

```python
git reflog
```

- 修改最后一次提交

```python
git commit --amend
具体过程
git commit -m 'commit'                      第二次提交
git add [forgotten_file]                       修正第一个
git commit --amend
```

- 取消对文件修改

```python
git checkout -- [filename]
```

- 克隆

  ```python
  git clone [url]
  ```

- 尝试推送python程序到远程仓库

```python
vim test.py
git add test.py
git commit -m "message"
git push
```

- 查看远程仓库

```python
git remote
git remote -v 
```

- 上传远程仓库

```python
cd mycode
git init
git add
git commit -m"submit files"
```

- 抓取数据

```python
git fetch [remote_name]
```

- 创建标签

```python
git tag -a [v1.4] -m 'my version 1.4'
```

- 列显已有标签

```python
git tag
或者
git tag -l 'v1.4.2.*'
```

- 展示标签版本信息

```python
git show [v1.4]
```

- 创建分支

```python
git branch [name]
仅仅是建立一个新分支，不会自动切换到该分支中去
```

- 切换分支

```python
git checkout [name]
```

- 删除分支

```python
git branch -d [name]
```

- SSH生成公钥

```python
ssh-keygen
```

- 整合远程再上传

```python
git fetch origin
git merge orign/master
git push origin master
当修改代码后发现已经有人改动其他代码，需要先fetch再merge后才push
```

- 操作的url可以是本地路径，如

```python
git clone /opt/git/project.git
或
git clone file://opt/git/project.git
```

- 回溯

```python
git check 
```

#### 四、Git 的三种状态

###### 在 Git 内都只有三种状态：已提交（committed），已修改（modified）和已暂存（staged）。

- 已提交表示该文件已经被安全地保存在本地数据库中了；
- 已修改表示修改了某个文件，但还没有提交保存；
- 已暂存表示把已修改的文件放在下次提交时要保存的清单中。

