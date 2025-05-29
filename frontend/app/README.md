# 前端 (Vue.js 应用)

此目录包含使用 Vue CLI 创建的 Vue.js 前端应用程序。

## 设置与运行

1.  **导航到前端应用目录：**
    ```bash
    cd frontend/app 
    ```
    *(假设您位于项目的根目录下)*

2.  **安装依赖项：**
    如果是首次设置，或者您拉取了新的更改：
    ```bash
    npm install
    ```

3.  **运行开发服务器：**
    ```bash
    npm run serve
    ```
    服务器通常会在 `http://localhost:8080` 上可用 (如果 8080 端口被占用，则可能是其他端口，请检查您终端中的输出)。

## 项目结构 (主要文件/目录)

-   `public/`: 静态资源。
-   `src/`: 主要应用程序源代码。
    -   `main.js`: 应用程序的入口点。
    -   `App.vue`:主要的根 Vue 组件。
    -   `components/`: 包含可复用的 Vue 组件 (例如, `ItemComponent.vue`)。
    -   `services/`: 包含用于后端通信的服务 (例如, `api.js`)。
    -   `assets/`: Vue 应用内使用的静态资源，如图片、字体。
-   `package.json`: 列出项目依赖项和脚本。
-   `vue.config.js`: (可选) Vue CLI 配置文件，如果您需要自定义构建过程。
