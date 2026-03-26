# 从 0 到 1 上手 GitHub：安装、配置与核心操作全指南

## 前言

对于开发者而言，GitHub 早已不只是“代码托管平台”——它是协作开发的工作台、开源项目的聚集地，更是技术成长中不可或缺的工具。但对刚接触的新手来说，从安装客户端到第一次提交代码，往往会被“仓库”“分支”“commit”这些术语劝退。别担心，这篇教程就是为你准备的！

**你将学到：**

- 为什么每个程序员都应该会用 GitHub？
- Git 与 GitHub 是什么关系？
- 如何安装 Git 并配置你的身份？
- 如何用 SSH 实现免密提交？
- 如何创建仓库、修改文件并提交代码？（图形化 + 命令行两种方式）
- 常见错误的解决办法
- 进阶学习路线图

**学习目标：** 学完本教程，你将能够独立使用 GitHub 管理自己的代码，为后续参与团队协作或开源项目打下基础。

------

## 一、先搞懂：为什么需要 GitHub？不是“存代码”这么简单

很多同学一开始会觉得：我本地存代码不就够了，为什么要折腾 GitHub？其实 GitHub 的核心价值，远不止“备份代码”：

- **协作开发**：多人开发同一个项目时，GitHub 能帮你管理代码版本，避免“张三改了 A 文件，李四覆盖了 B 文件”的混乱。通过 **Pull Request（PR）** 机制，可以实现代码审核，保证代码质量。
- **开源参与**：全球数百万开源项目（比如 Linux、Vue.js、Spring Boot）都托管在 GitHub 上。你可以通过 **Fork + PR** 向喜欢的项目贡献代码，积累真实的开发经验，甚至成为知名项目的贡献者。
- **个人名片**：一份维护良好的 GitHub 仓库，能直观展示你的技术栈和编码风格。很多面试官会主动查看候选人的 GitHub，优秀的项目甚至能帮你获得内推机会。
- **版本回溯**：不小心删了关键代码？改崩了项目？GitHub 能让你轻松回滚到任意历史版本，相当于给代码加了“时光机”。
- **学习资源**：GitHub 上有无数优秀的开源项目源码，你可以通过阅读源码提升技术，还可以在 Issues 区向大牛提问。

------

## 二、Git 与 GitHub：先分清两个概念

很多新手容易混淆 **Git** 和 **GitHub**：

- **Git**：是一个 **版本控制工具**，安装在你的电脑上，用来记录代码的每一次修改，并支持多人协作合并代码。它是一个**命令行工具**，也可以配合图形化界面使用。
- **GitHub**：是一个 **基于 Git 的代码托管平台**，它把 Git 仓库存储在云端，让你可以和他人共享代码。类似的服务还有 Gitee（码云）、GitLab 等。

**简单来说：Git 是工具，GitHub 是存放代码的“云盘 + 社交平台”。**

------

## 三、第一步：安装 Git 与 GitHub 客户端

### 1. 安装 Git（必装）

Git 是核心工具，无论你用不用 GitHub 客户端，都必须先安装 Git。

#### Windows 系统

1. 打开 Git 官网（https://git-scm.com/），点击右上角“Download for Windows”，下载安装包（通常选择 64-bit 版本）。
2. 双击安装包，一路“Next”即可（默认选项足够新手使用）。注意在“Select Components”步骤，建议勾选“Git GUI Here”和“Git Bash Here”（方便右键菜单启动）。
3. 安装完成后，在桌面空白处右键，如果看到“Git Bash Here”选项，说明安装成功。
4. 验证：按下 `Win + R`，输入 `cmd` 打开命令提示符，输入 `git --version`，如果显示 `git version 2.x.x...`，说明安装成功。

#### Mac 系统

1. 打开终端（Launchpad → 其他 → 终端），输入 `git --version`，如果没安装，系统会提示“是否安装开发者工具”，点击“安装”即可。
2. 或者通过 Homebrew 安装（需要先安装 Homebrew，官网：https://brew.sh/）：`brew install git`

#### Linux 系统（以 Ubuntu 为例）

bash

```
sudo apt update
sudo apt install git
git --version   # 验证
```



### 2. 安装 GitHub 客户端（新手强烈推荐）

如果你觉得命令行记不住，GitHub 官方提供了图形化客户端 **GitHub Desktop**，操作非常直观，适合新手入门。

- 下载地址：https://desktop.github.com/，根据系统选择 Windows 或 Mac 版本。
- 安装后打开，点击 “Sign in to [GitHub.com](https://github.com/)”，用你的 GitHub 账号登录（如果没有账号，先去 [GitHub 官网](https://github.com/) 注册，用户名建议用英文，避免后续踩坑）。
- 登录成功后，客户端会自动关联你的 Git 配置，后续操作再也不用敲命令了！

------

## 四、核心配置：让 GitHub 认识“你是谁”（关键一步）

安装完成后，必须做一件事：**告诉 Git 你的 GitHub 账号信息**，否则 GitHub 无法识别你的代码提交身份（相当于“给代码签名，证明这是你提交的”）。

### 1. 命令行配置（无论用不用客户端，都建议做）

打开终端（Windows 用命令提示符或 Git Bash，Mac/Linux 用终端），输入以下两条命令，**注意把 `your-github-username` 换成你的 GitHub 用户名，`your-github-email` 换成你注册 GitHub 时用的邮箱**：

bash

```
git config --global user.name "your-github-username"
git config --global user.email "your-github-email"
```



- **验证配置**：输入 `git config --global --list`，如果能看到刚才配置的用户名和邮箱，说明配置成功。
- **为什么加 `--global`？** 这个参数表示“全局配置”，后续所有 Git 仓库都会用这个身份，不用每个仓库都配一次。如果你想为某个特定仓库设置不同身份，可以在仓库目录下不加 `--global` 重新配置。

### 2. 配置 SSH 密钥（免密码提交，强烈推荐）

默认情况下，每次向 GitHub 提交代码，都需要输入用户名和密码（或个人访问令牌），比较麻烦。配置 SSH 密钥后，可以实现“免密码提交”，更高效。

#### 什么是 SSH 密钥？

SSH 密钥是一对文件：公钥（`.pub`）和私钥。你把**公钥**放在 GitHub 上，本地保留**私钥**，当你的电脑连接 GitHub 时，GitHub 会用公钥验证你的身份，全程无需输入密码。

#### 生成 SSH 密钥

打开终端，输入以下命令（邮箱还是你 GitHub 的注册邮箱）：

bash

```
ssh-keygen -t ed25519 -C "your-github-email"
```



- 如果系统不支持 ed25519 算法（比如旧系统），换成：`ssh-keygen -t rsa -b 4096 -C "your-github-email"`
- 然后一路按回车（不用输入任何内容），密钥会保存在默认路径：`~/.ssh/id_ed25519`（或 `id_rsa`）。

#### 找到并复制公钥

- **Windows**：打开 `C:\Users\你的用户名\.ssh\` 文件夹，用记事本打开 `id_ed25519.pub` 文件，**全选复制**里面的内容（从 “ssh-ed25519” 开始，到你的邮箱结束，不要漏字符）。
- **Mac/Linux**：终端输入 `cat ~/.ssh/id_ed25519.pub`，复制输出的内容。

#### 添加到 GitHub

1. 登录 GitHub，点击右上角头像 → “Settings” → 左侧菜单 “SSH and GPG keys” → 点击 “New SSH key”。
2. “Title” 随便填（比如“我的 Windows 电脑”），“Key type” 选 “Authentication Key”，“Key” 粘贴刚才复制的内容，点击 “Add SSH key”。

#### 验证是否生效

终端输入：

bash

```
ssh -T git@github.com
```



第一次会提示 “Are you sure you want to continue connecting (yes/no)?”，输入 `yes`，如果显示：

text

```
Hi [你的用户名]! You've successfully authenticated...
```



说明配置成功！

------

## 五、实战操作：从“创建仓库”到“提交代码”

接下来用 **GitHub Desktop 客户端** 和 **命令行** 两种方式，演示最核心的流程：创建仓库 → 本地修改 → 提交代码 → 推送到 GitHub。

### 方式 1：用 GitHub Desktop（图形化操作，新手推荐）

#### 1. 创建仓库（两种方法）

##### 方法 A：先在 GitHub 官网创建，再克隆到本地

- 登录 GitHub 官网，点击右上角 “+” → “New repository”。
- 填写仓库信息：
  - **Repository name**：仓库名（比如 `my-first-project`，用英文和横杠，不要用中文和空格）。
  - **Description**：可选，填仓库描述（比如“我的第一个 GitHub 项目”）。
  - **Public/Private**：公开/私有（新手选 Public，免费；Private 别人看不到，但免费账号也能创建）。
  - 勾选 **“Add a README file”**（生成一个说明文件，方便别人了解项目）。
  - 点击 “Create repository”，仓库就创建好了。
- 打开 GitHub Desktop，点击 “File” → “Clone repository”，在 “[GitHub.com](https://github.com/)” 标签下找到刚才创建的仓库，选择本地保存路径（比如 `D:\Projects\my-first-project`），点击 “Clone”，仓库就克隆到本地了。

##### 方法 B：先在本地创建项目，再推送到 GitHub

- 在本地创建一个文件夹（比如 `my-second-project`），里面放一些文件（比如新建一个 `hello.txt`，写上“Hello GitHub!”）。
- 打开 GitHub Desktop，点击 “File” → “Add local repository”，选择刚才创建的本地文件夹，点击 “Add repository”。
- 此时客户端会检测到这是一个未初始化的文件夹，点击 “Publish repository”，填写仓库名和描述，选择 “Public/Private”，点击 “Publish repository”，本地项目就推送到 GitHub 了。

#### 2. 修改文件并提交代码

- 找到本地仓库文件夹（比如 `D:\Projects\my-first-project`），用记事本或 VS Code 打开 `README.md` 文件，添加一行内容（比如“这是我第一次修改 README 文件！”），保存。
- 回到 GitHub Desktop，你会看到 “Changes” 面板显示了修改的文件（`README.md`）。下方 “Summary” 框填写提交说明（**必须填**，简要说明这次改了什么，比如 `update README: add first edit note`），“Description” 可选填详细描述。
- 点击 **“Commit to main”**（main 是默认分支名），这一步是将修改**提交到本地 Git 仓库**。
- 点击右上角 **“Push origin”**，这一步是将本地提交**推送到 GitHub 远程仓库**。
- 验证：打开 GitHub 官网的仓库页面，刷新一下，你会看到 `README.md` 的内容已经更新，说明操作成功！

#### 3. 查看历史版本

- 在 GitHub Desktop 中，点击 “History” 标签，可以看到所有提交记录，点击某条记录可以查看具体修改了哪些内容。
- 如果想回退到某个版本，可以在该记录上右键 → “Revert this commit”，但要注意这可能覆盖当前修改，建议先了解 Git 撤销操作后再使用。

------

### 方式 2：用命令行（适合想深入学习的同学）

#### 1. 创建仓库并克隆到本地

- 先在 GitHub 官网创建仓库（步骤同上），但**不要勾选 “Add a README file”**（或者勾选也行，但克隆下来后需要合并，为了简单，建议不勾选）。
- 创建完成后，点击绿色的 “Code” 按钮，复制仓库的 SSH 地址（比如 `git@github.com:your-username/my-first-project.git`）。如果你没配置 SSH，可以复制 HTTPS 地址，但推送时需要输入用户名和令牌。
- 在本地选择一个文件夹（比如 `D:\Projects`），打开终端（Git Bash），输入：

bash

```
git clone git@github.com:your-username/my-first-project.git
cd my-first-project
```



#### 2. 创建或修改文件并提交

- 在 `my-first-project` 文件夹下新建一个 `hello.txt` 文件，写入内容（比如“Hello from command line!”）。
- 在终端中执行以下命令：

bash

```
# 查看当前仓库状态（哪些文件被修改了）
git status

# 把 hello.txt 添加到暂存区（准备提交）
git add hello.txt

# 也可以用 git add . 添加当前目录所有修改（注意 add 和 . 之间有空格）

# 提交到本地仓库，-m 后面是提交说明
git commit -m "add hello.txt with greeting"

# 推送到 GitHub 远程仓库
git push origin main
```



- 如果这是第一次推送，且远程仓库是空的，可能还需要设置上游分支，但 Git 通常会提示你使用 `git push -u origin main`，这样以后就可以直接 `git push`。

#### 3. 拉取远程更新（多人协作时常用）

如果你在 GitHub 网页上直接修改了文件，或者你的队友推送了新代码，你需要在本地同步这些更新：

bash

```
git pull origin main
```



这个命令会从远程仓库拉取最新代码并自动合并到当前分支。

------

## 六、核心概念解析：工作区、暂存区、本地仓库、远程仓库

为了更好理解 Git 的工作原理，我们需要知道四个概念：

- **工作区（Working Directory）**：就是你电脑上看到的项目文件夹，你在这里修改文件。
- **暂存区（Staging Area / Index）**：一个临时存放区域，当你执行 `git add` 后，修改会进入暂存区，等待被提交。
- **本地仓库（Local Repository）**：Git 在你电脑上创建的隐藏文件夹（`.git`），里面记录了所有历史版本。当你执行 `git commit` 后，暂存区的修改会被永久记录到本地仓库。
- **远程仓库（Remote Repository）**：托管在 GitHub 等服务器上的仓库，当你执行 `git push` 后，本地仓库的更新会被推送到远程仓库；执行 `git pull` 则从远程拉取更新。

**流程图：**

text

```
工作区 → git add → 暂存区 → git commit → 本地仓库 → git push → 远程仓库
                ← git reset  ←                   ← git pull  ←
```



------

## 七、新手常见问题与避坑指南

### ❓ 执行 `git add.` 提示 `git: 'add.' is not a git command`

- **原因**：`add` 和 `.` 之间缺少空格，Git 将其解析为一个命令 `add.`。
- **解决**：确保命令是 `git add .`（`add` 和 `.` 之间有空格）。`.` 表示当前目录，意思是添加当前目录下的所有修改。

### ❓ `git add .` 和 `git add -A`、`git add -u` 有什么区别？

- `git add .`：添加当前目录下所有修改（包括新增、修改、删除），但不包括父目录的修改。
- `git add -A`：添加整个工作区所有修改（包括父目录），效果等同于 `git add --all`。
- `git add -u`：只添加已跟踪文件的修改和删除，不包括新文件。
- 日常开发中，`git add .` 足够常用，如果想一次添加所有改动（包括删除和新增），可以用 `git add -A`。

### ❓ `git push` 时提示 `permission denied`（权限拒绝）

- **原因**：SSH 密钥配置错误，或没配置 SSH 密钥，用了 HTTPS 地址却没输对密码。
- **解决**：
  - 如果用了 SSH，检查密钥是否添加（`ssh -T git@github.com` 测试），公钥是否粘贴正确。
  - 如果用了 HTTPS，注意 **GitHub 从 2021 年起不再支持密码登录**，需要用 **个人访问令牌（Personal Access Token）**。生成方式：GitHub → Settings → Developer settings → Personal access tokens → Generate new token，勾选 “repo” 权限，生成后复制，推送时在密码框粘贴令牌即可。

### ❓ 提交代码时提示 `nothing to commit`（没有可提交的内容）

- **原因**：没修改文件，或修改的文件没加入暂存区（没执行 `git add`）。
- **解决**：先修改本地文件，再用 `git status` 查看状态，确认有修改后执行 `git add`。

### ❓ 克隆仓库时提示 `fatal: repository not found`（仓库找不到）

- **原因**：复制的仓库地址错误，或仓库不存在，或没有访问权限（比如克隆别人的私有仓库）。
- **解决**：重新复制仓库地址（确认用户名和仓库名正确），或检查仓库是否存在，或请求仓库所有者授权。

### ❓ 执行 `git commit` 时没加 `-m` 参数，进入了奇怪的界面怎么办？

- **原因**：Git 默认会打开文本编辑器（通常是 Vim）让你输入提交信息。如果忘了加 `-m`，就会进入 Vim。

- **解决**：在 Vim 中，按 `i` 进入插入模式，输入提交信息，按 `Esc` 退出插入模式，然后输入 `:wq` 按回车保存退出。如果不想保存，可以输入 `:q!` 强制退出，然后重新执行带 `-m` 的 commit 命令。

- **小技巧**：可以配置 Git 默认使用其他编辑器（如 VS Code）：

  bash

  ```
  git config --global core.editor "code --wait"
  ```

  

### ❓ 推送时遇到 Gitee LFS 错误：`LFS only supported repository in paid or trial enterprise`

- **原因**：你推送的仓库中包含被 Git LFS 追踪的大文件，而 **Gitee 的 LFS 功能仅对付费企业用户开放**，个人免费账户无法使用。

- **解决**：

  - **快速方案**：删除本地的 pre-push 钩子，绕过 LFS 检查，然后强制推送。

    bash

    ```
    rm .git/hooks/pre-push
    git push -u origin master -f
    ```

    

  - **彻底方案**：移除 LFS 配置，改用普通 Git 管理文件（需编辑 `.gitattributes` 文件并重新提交）。

  - **长期方案**：升级 Gitee 企业版，或改用 GitHub（免费版有 LFS 配额）等支持 LFS 的平台。

### ❓ 推送时提示 `src refspec main does not match any`

- **原因**：本地没有名为 `main` 的分支（可能是 `master`），但你试图推送 `main`。
- **解决**：
  - 查看当前分支：`git branch`
  - 如果当前分支是 `master`，推送 `master`：`git push origin master`
  - 或将本地 `master` 分支推送到远程 `main` 分支：`git push origin master:main`
  - 或重命名本地分支为 `main`：`git branch -m master main`，然后再推送

### ❓ 如何撤销刚刚的 commit（还没有 push）？

- 如果你刚刚 commit 但发现写错了，想重新提交：

  bash

  ```
  git commit --amend -m "新的提交信息"
  ```

  

  这个命令会修改最近一次 commit 的信息，并包含当前暂存区的修改。

- 如果你想撤销 commit，但保留工作区的修改：

  bash

  ```
  git reset --soft HEAD~1
  ```

  

  `HEAD~1` 表示回到上一个版本，`--soft` 表示保留工作区和暂存区的内容。

- 如果你想彻底撤销 commit，并丢弃修改：

  bash

  ```
  git reset --hard HEAD~1
  ```

  

  **注意**：`--hard` 会丢失所有未提交的修改，慎用！

### ❓ 如何解决合并冲突（merge conflict）？

当两个人修改了同一文件的同一部分，Git 无法自动合并时，就会产生冲突。冲突文件会包含类似这样的标记：

text

```
<<<<<<< HEAD
你的修改
=======
别人的修改
>>>>>>> branch-name
```



你需要手动编辑文件，保留想要的内容，删除冲突标记，然后：

bash

```
git add 文件名
git commit -m "解决冲突"
```



------

## 八、团队协作基础：分支与 Pull Request

### 1. 什么是分支（Branch）？

分支就像平行宇宙，让你可以在不影响主线（`main`）的情况下，独立开发新功能或修复 Bug。开发完成后，再把分支合并回主线。

**常用分支命令：**

bash

```
# 查看所有分支（当前分支前有 * 号）
git branch

# 创建新分支
git branch feature-login

# 切换到新分支
git checkout feature-login

# 创建并切换（一步到位）
git checkout -b feature-login

# 合并分支（先切换到目标分支，再合并）
git checkout main
git merge feature-login

# 删除分支（合并后可删除）
git branch -d feature-login
```



### 2. 什么是 Pull Request（PR）？

PR 是 GitHub 的核心协作机制。当你开发完一个功能，想把它合并到主分支时，可以发起一个 PR，通知团队成员审核你的代码。审核通过后，再由管理员合并。

**基本流程：**

1. 在 GitHub 上 Fork 别人的仓库（或者在自己仓库中创建新分支）。
2. 克隆到本地，修改代码，提交并推送到你的仓库。
3. 在 GitHub 上点击 “New pull request”，选择你的分支和目标分支，填写说明。
4. 等待审核，根据反馈修改，最终合并。

------

## 九、进阶学习路线

掌握了以上内容，你已经可以独立使用 GitHub 了。如果想更上一层楼，可以学习这些技能：

- **Git 高级操作**：
  - `git rebase`：变基，让提交历史更整洁
  - `git cherry-pick`：挑选特定提交合并到当前分支
  - `git stash`：暂存当前工作，切换到其他分支
  - `git reflog`：查看所有操作历史，找回丢失的提交
- **GitHub 特色功能**：
  - **GitHub Actions**：自动化 CI/CD，比如代码推送后自动运行测试、部署到服务器
  - **GitHub Pages**：免费托管静态网站，可以用 Markdown 写博客、项目文档
  - **GitHub Projects**：项目管理看板，类似 Trello
  - **GitHub Insights**：查看仓库活跃度、贡献者统计
- **开源参与**：
  - 找一个感兴趣的开源项目，阅读文档，从 `good first issue` 开始贡献
  - 学习如何写规范的 README、CONTRIBUTING 文档
- **Git 钩子（Hooks）**：在特定操作前自动执行脚本，比如提交前检查代码格式

------

## 十、附：国内代码托管平台简介

除了 GitHub，国内也有优秀的托管平台，访问速度快，适合国内开发者：

### Gitee（码云）

- **官网**：https://gitee.com/
- **特点**：国内用户量最大，免费私有仓库，Pages 服务免费，但 **LFS 大文件存储需要企业版**。
- **适合**：国内团队协作、个人项目，尤其是需要快速 clone/push 的场景。

### GitCode

- **官网**：https://gitcode.net/
- **特点**：CSDN 出品，与 CSDN 社区深度打通，可以引流到博客，Pages 免费。
- **适合**：希望借助 CSDN 增加项目曝光度的开发者。

### CODING（腾讯云）

- **官网**：https://coding.net/
- **特点**：提供 DevOps 全套工具（代码托管、项目协同、CI/CD），深度集成腾讯云。
- **适合**：企业级开发，需要一站式 DevOps 解决方案。

**如何选择？**

- 个人学习/参与国际开源：首选 GitHub
- 国内项目/访问速度要求高：Gitee 或 GitCode
- 企业 DevOps：CODING、阿里云 Codeup、华为云 CodeArts、服务器部署

------

## 十一、Git 常用命令速查表

| 命令                       | 说明                                     |
| :------------------------- | :--------------------------------------- |
| `git init`                 | 在当前目录初始化一个 Git 仓库            |
| `git clone <url>`          | 克隆远程仓库到本地                       |
| `git status`               | 查看当前工作区状态                       |
| `git add <file>`           | 将文件添加到暂存区                       |
| `git add .`                | 添加当前目录所有修改到暂存区             |
| `git commit -m "message"`  | 提交暂存区内容到本地仓库                 |
| `git push origin <branch>` | 推送本地提交到远程仓库                   |
| `git pull origin <branch>` | 拉取远程更新并合并                       |
| `git fetch origin`         | 拉取远程更新但不合并                     |
| `git branch`               | 查看本地分支                             |
| `git branch <name>`        | 创建新分支                               |
| `git checkout <branch>`    | 切换分支                                 |
| `git checkout -b <branch>` | 创建并切换分支                           |
| `git merge <branch>`       | 合并指定分支到当前分支                   |
| `git log`                  | 查看提交历史                             |
| `git diff`                 | 查看工作区与暂存区的差异                 |
| `git reset HEAD <file>`    | 将文件从暂存区移除（但保留修改）         |
| `git reset --hard HEAD~1`  | 回退到上一个版本，并丢弃所有修改（慎用） |
| `git stash`                | 暂存当前工作，恢复干净工作区             |
| `git stash pop`            | 恢复最近一次暂存的工作                   |
| `git remote -v`            | 查看远程仓库地址                         |
| `git config --list`        | 查看 Git 配置                            |

------

## 结语

GitHub 的核心逻辑其实很简单：**“本地修改 → 提交到本地仓库 → 推送到远程仓库”**。刚开始可能会记不住命令，但多练习几次，尤其是实际开发中用起来，很快就能上手。如果在操作中遇到其他问题，欢迎随时查阅 [Git 官方文档](https://git-scm.com/doc) 或 [GitHub 帮助文档](https://docs.github.com/)。

别忘了，GitHub 也是你展示自己的舞台——从今天开始，用 GitHub 记录你的代码成长之路吧！