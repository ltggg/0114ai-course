# **第一章：Git 团队协作 —— 6 组分支管理实战**

## **🎯 本章目标**

* 掌握 Git 分支的核心机制与多人协作工作流。  
* 熟悉“组长分支制”：6 个组长各建分支，组员通过组长汇入主分支。  
* 理解 Pull Request（合并请求）的审批流程。  
* 完成从建仓到多人协作提交的完整闭环。

## **一、为什么要用分支？**

一个词：**隔离**。

* 你在分支上写代码，不影响主分支（main）。  
* 写完、测完、没问题了，再合并回去。  
* 翻车了？直接删分支，主分支毫发无损。

      main ────●────●────●────●────●──── (稳定版本)  
                    \\                 /  
      feature        ●──●──● (你在这里折腾)

## **二、我们的协作模型**

main (郝老师主分支) ← 合并需要老师审批  
├── group1 (1组组长分支) ← 组员直接推送  
├── group2 (2组组长分支)  
├── group3 (3组组长分支)  
├── group4 (4组组长分支)  
├── group5 (5组组长分支)  
└── group6 (6组组长分支)

**规则说明：**

| 角色 | 权限 | 操作 |
| :---- | :---- | :---- |
| **组长** | 管理组分支 | 创建分支、审核组员代码、向 main 提 PR |
| **组员** | 推送到组分支 | clone 仓库 → 切到组分支 → push 代码 |
| **郝老师** | 管理 main | 审批 PR、合并到 main、发布课件 |

## **三、组长操作手册**

**Step 1：克隆仓库**

git clone git@github.com:haowenlong/0114ai-course.git  
cd 0114ai-course

**Step 2：创建组分支并推送**

git checkout \-b group1  
git push \-u origin group1

**Step 3：日常工作流**

git add .  
git commit \-m "第1组-张三：Day1作业提交"  
git push

**Step 4：向主分支发起合并请求（PR）**

1. 打开 GitHub 仓库页面。  
2. 点击 "Pull Requests" → "New Pull Request"。  
3. 选择 group1 → main。  
4. 填写说明，提交 PR。  
5. 等待郝老师审批合并。

## **四、组员操作手册**

**Step 1：克隆仓库**

git clone git@github.com:haowenlong/0114ai-course.git  
cd 0114ai-course

**Step 2：切换到自己组的分支**

git checkout group1

**Step 3：拉取最新代码（每次开始前必做）**

git pull origin group1

**Step 4：提交自己的代码**

git add .  
git commit \-m "张三-Day1-逻辑门作业"  
git push origin group1

## **五、常用 Git 命令速查**

| 命令 | 作用 |
| :---- | :---- |
| git branch | 查看本地分支 |
| git branch \-a | 查看所有分支（含远程） |
| git checkout \<分支名\> | 切换分支 |
| git checkout \-b \<新分支\> | 创建并切换分支 |
| git pull origin \<分支\> | 拉取远程分支最新内容 |
| git push origin \<分支\> | 推送到远程分支 |
| git merge \<分支\> | 合并指定分支到当前分支 |
| git log \--oneline \-5 | 查看最近 5 条提交记录 |
| git status | 查看当前改动状态 |
| git diff | 查看具体改了什么 |

## **六、冲突处理**

当两个人同时改了同一个文件同一行时，Git 会标记冲突：

\<\<\<\<\<\<\< HEAD  
这是你的代码  
\=======  
这是别人的代码  
\>\>\>\>\>\>\> group1

**处理方法：** 手动选择保留哪段代码，删掉标记符号，然后执行 git add . 与 git commit。

💡 **本章小结**

* **分支隔离**：在自己的地盘折腾，不影响主线。  
* **PR 审批**：组长向 main 提交 PR，老师审批后合并。  
* **每次开工先 pull**：避免冲突的最好方式。

# **第二章：环境准备 —— 搭建 Python 开发环境**

在正式写 Python 代码之前，我们需要配置好统一的开发环境。我们将使用 Miniconda 创建独立的虚拟环境，并在其中安装 PyTorch，这样所有同学的环境一致，且不会与电脑上的其他 Python 项目冲突。

## **一、安装 Miniconda**

Miniconda 是一个轻量级的 Python 环境管理工具，让你可以为每个项目创建独立的“小房间”。

**1\. 下载安装程序**

* 访问官网：[https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)  
* 选择 **Windows 64-bit** 版本（.exe 文件）下载。

**2\. 执行安装**

* 双击安装包，**不要安装在 C 盘**。建议放在其他盘符，例如 D:\\miniconda3 或 E:\\miniconda3，且路径中不要包含空格或中文。  
* **关键选项：** 勾选 Add Miniconda3 to my PATH environment variable，这样在命令行中可以直接使用 conda 命令。  
* 其他选项保持默认，完成安装。

**3\. 验证安装**

打开命令提示符（cmd）或 Anaconda Prompt，输入：

conda \--version

如果显示版本号（如 conda 25.1.1），则安装成功。

## **二、创建虚拟环境并安装 PyTorch**

**1\. 创建环境**

我们创建一个名为 ai\_env 的环境，指定 Python 3.12（PyTorch 官方对 3.12 支持良好）：

conda create \-n ai\_env python=3.12

出现提示时输入 y 确认。

**2\. 激活环境**

conda activate ai\_env

激活后命令行前缀会变成 (ai\_env)，说明你正在这个独立环境中操作。

**3\. 安装 PyTorch（根据你的电脑情况选择）**

首先，确定你的电脑是否有 NVIDIA 显卡以及支持的 CUDA 版本：

* 打开命令提示符，运行 nvidia-smi（如果没有此命令，说明没有 NVIDIA 显卡或驱动未安装）。  
* 如果有输出，查看第一行右上角的 CUDA 版本（例如 CUDA Version: 11.8），记录下来。

然后，访问 PyTorch 官网：[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

在页面中选择你的系统环境（Windows、conda、Python、CUDA 版本等），官网会自动生成对应的安装命令。将生成的命令复制到命令行中执行。

**常见情况举例：**

* **无 NVIDIA 显卡（CPU 版本）：**  
  conda install pytorch torchvision torchaudio cpuonly \-c pytorch

* **有显卡且 CUDA 11.8：**  
  conda install pytorch torchvision torchaudio cudatoolkit=11.8 \-c pytorch \-c nvidia

⚠️ **请注意：** 不同 CUDA 版本对应的命令可能不同，务必以官网生成的命令为准。按提示输入 y 等待安装完成。

**4\. 验证安装**

在 (ai\_env) 环境下，运行：

python \-c "import torch; print(torch.\_\_version\_\_)"

如果输出版本号（例如 2.4.0），说明 PyTorch 安装成功。

## **三、在虚拟环境中安装 Jupyter（可选）**

如果你希望在 Jupyter Notebook 中编写代码，可以在 ai\_env 环境中安装 Jupyter：

conda install jupyter  
jupyter notebook

**注意：** Miniconda 默认不包含 Jupyter，因此需要手动安装。如果你使用的是 Anaconda，则可以跳过这一步。这样启动的 Notebook 会默认使用 ai\_env 环境中的 Python 内核。

## **四、在 PyCharm 中配置 conda 环境**

如果你使用 PyCharm 作为开发工具，需要将项目解释器设置为刚才创建的 ai\_env 环境，否则运行代码时会找不到 torch。

**1\. 打开项目设置**

* 在 PyCharm 中打开你的项目（例如 D:\\code\\AI\_0114\_MustWin）。  
* 点击菜单栏 File → Settings（或按 Ctrl \+ Alt \+ S）。  
* 在左侧导航栏找到 Project: 你的项目名 → Python Interpreter。

**2\. 添加 Conda 环境**

* 点击右上角的齿轮图标 ⚙️，选择 Add。  
* 在弹出的窗口中，左侧选择 Conda Environment。  
* 右侧选择 Existing environment。  
* 在 Interpreter 一栏，点击右侧的文件夹图标，浏览找到你之前创建的 ai\_env 环境中的 python.exe。  
  * 典型路径为：D:\\miniconda3\\envs\\ai\_env\\python.exe（如果你将 Miniconda 安装在了其他盘符，请根据实际路径选择）。  
* 勾选 Make available to all projects（可选）。  
* 点击 OK 保存。

**3\. 确认解释器**

* 现在 Python Interpreter 列表应该显示 ai\_env 环境。  
* 可以在下方的包列表中查看是否已包含 torch、torchvision 等。  
* 点击 Apply 和 OK 关闭设置窗口。

**4\. 验证环境**

在 PyCharm 中打开任意 Python 文件（或新建一个），输入：

import torch  
print(torch.\_\_version\_\_)

运行代码，如果没有报错且输出版本号，说明环境配置成功。

**5\. 在 PyCharm 终端中激活环境（可选）**

PyCharm 的终端（Terminal）通常会继承项目解释器的环境，但有时需要手动激活。如果运行上述代码后仍提示“ModuleNotFoundError”，可以：

* 在 PyCharm 底部打开 Terminal 标签。  
* 手动激活 conda 环境：  
  conda activate ai\_env

* 此时终端前缀会显示 (ai\_env)，然后你可以在该终端中运行脚本或使用 pip 安装包。

## **五、常用 conda 命令速查**

| 操作 | 命令 |
| :---- | :---- |
| 查看所有环境 | conda env list |
| 激活环境 | conda activate 环境名 |
| 退出环境 | conda deactivate |
| 安装包 | conda install 包名 |
| 删除环境 | conda remove \-n 环境名 \--all |

## **六、日常使用建议**

* 每次开始作业前，打开命令行，先执行 conda activate ai\_env 切换到课程环境，再进入你的项目目录（例如 cd D:\\code\\AI\_0114\_MustWin）。  
* 如果想省去每次 activate 的步骤，可以设置 conda 自动激活 ai\_env 环境，但考虑到后续可能需要切换其他项目环境，建议保持手动激活的习惯，以免环境混乱。

💡 **小提示：** 如果不想每次手动激活，可以创建批处理文件（如 start\_ai.bat）：

@echo off  
call conda activate ai\_env  
cd /d D:\\code\\AI\_0114\_MustWin  
cmd /k

双击这个文件就能直接进入课程环境。

💡 **本章小结**

* 用 Miniconda 创建独立环境，避免 Python 包冲突。  
* 通过 nvidia-smi 查看显卡支持情况，从 PyTorch 官网获取准确的安装命令。  
* 每次开工前激活环境，确保代码运行在统一的 Python 版本和依赖下。  
* 在 PyCharm 中正确配置项目解释器，才能使用已安装的 PyTorch。