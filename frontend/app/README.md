# Frontend (Vue.js App)

This directory contains the Vue.js frontend application, created using Vue CLI.

## Setup and Running

1.  **Navigate to the frontend app directory:**
    ```bash
    cd frontend/app 
    ```
    *(Assuming you are at the root of the project)*

2.  **Install Dependencies:**
    If this is the first time or if you've pulled new changes:
    ```bash
    npm install
    ```

3.  **Run the Development Server:**
    ```bash
    npm run serve
    ```
    The server will typically be available at `http://localhost:8080` (or another port if 8080 is busy, check the output in your terminal).

## Project Structure (Key Files/Directories)

-   `public/`: Static assets.
-   `src/`: Main application source code.
    -   `main.js`: The entry point of the application.
    -   `App.vue`: The main root Vue component.
    -   `components/`: Contains reusable Vue components (e.g., `ItemComponent.vue`).
    -   `services/`: Contains services like `api.js` for backend communication.
    -   `assets/`: Static assets like images, fonts used within the Vue app.
-   `package.json`: Lists project dependencies and scripts.
-   `vue.config.js`: (Optional) Vue CLI configuration file if you need to customize the build process.
