# 后端 (FastAPI)

此目录包含 FastAPI 后端应用程序。

## 设置与运行

1.  **导航到 `backend` 目录：**
    ```bash
    cd backend
    ```

2.  **创建/激活虚拟环境 (推荐)：**
    尽管初始设置可能已全局安装了依赖项作为临时解决方案，但为了保证开发的一致性，强烈建议使用虚拟环境。
    ```bash
    # 创建虚拟环境 (如果尚未创建)
    python3 -m venv .venv 

    # 激活虚拟环境
    # macOS 和 Linux:
    source .venv/bin/activate
    # Windows:
    # .venv\Scripts\activate
    ```

3.  **安装依赖项：**
    如果您已激活虚拟环境，或者需要重新安装/更新依赖项：
    ```bash
    pip install -r requirements.txt
    ```
    *注意：`requirements.txt` 文件是在初始设置过程中生成的。它包含了 FastAPI, Uvicorn, SQLAlchemy 等。*

4.  **运行开发服务器：**
    在 `backend` 目录下运行：
    ```bash
    uvicorn main:app --reload
    ```
    服务器通常会在 `http://127.0.0.1:8000` 上可用。

## 项目结构

-   `main.py`: FastAPI 应用程序的主文件，包含 API 路由和 CORS 配置。
-   `crud.py`: 包含数据库的 CRUD (创建, 读取, 更新, 删除) 操作。
-   `database.py`: 处理数据库连接 (SQLite) 和会话管理。
-   `models.py`: 定义 SQLAlchemy 数据库模型。
-   `schemas.py`: 定义用于请求/响应数据验证的 Pydantic 模型。
-   `requirements.txt`: 列出 Python 依赖项。
-   `sql_app.db`: SQLite 数据库文件 (将在应用程序运行并与数据库交互时创建)。
