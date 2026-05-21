# QGIS Earth Engine Integration 

This repository contains a modular Python setup for running Google Earth Engine (GEE) scripts directly inside QGIS. 

Unlike standard QGIS project files (`.qgz`), this structure separates the core Earth Engine logic from the QGIS execution environment. This makes the code **100% plain text, easily committable to Git, and editable in your favorite IDE (like VS Code)** without needing to restart QGIS to see your changes.

## 📂 Project Structure

* `gee_logic.py`: Contains pure Earth Engine logic. Safe to run headlessly or test independently.
* `qgis_runner.py`: The bridge script. You run this inside QGIS. It automatically reloads `gee_logic.py` so you never have to deal with cached modules.
* `.gitignore`: Prevents QGIS lock files and Python cache binaries from cluttering your repository.

## ⚙️ Prerequisites

1. **QGIS** installed on your machine.
2. The **Google Earth Engine Plugin** installed in QGIS:
   * Open QGIS -> `Plugins` -> `Manage and Install Plugins...`
   * Search for `Google Earth Engine Plugin` and install it.
3. An active **Google Earth Engine Account**.
   * You will need to authenticate the plugin the first time you use it by clicking the Earth Engine icon in the QGIS toolbar.

## 🚀 How to Run the Code

Follow these steps to execute the script and render the Earth Engine data onto your QGIS map canvas:

1. **Open QGIS** and create a new, empty project.
2. Open the **Python Console** by clicking `Plugins` -> `Python Console` (or press `Ctrl + Alt + P` / `Cmd + Option + P`).
3. Click the **Show Editor** icon (it looks like a small notepad/pencil) at the top of the Python Console.
4. Click the **Open Script** icon (the folder icon) in the editor panel.
5. Navigate to this repository folder and open **`qgis_runner.py`**.
6. Click the green **Run Script** button (the play triangle).

You should see the console print a success message, and the Earth Engine layer (e.g., the SRTM Elevation Model) will appear on your map canvas!

## 💻 Development Workflow (The "Git" Way)

Because QGIS caches Python modules aggressively, developing directly inside QGIS can be frustrating. This repository uses dynamic reloading to solve that.

**To edit your code:**
1. Open this repository in your preferred IDE (e.g., VS Code, PyCharm).
2. Make your edits to the math, bounds, or visualization parameters inside `gee_logic.py` and save the file.
3. Switch back to QGIS (leave `qgis_runner.py` open in the QGIS editor).
4. Click the **Run** button again. 

The `qgis_runner.py` script will automatically fetch your freshest edits from `gee_logic.py`, bypass the QGIS cache, and update your map canvas instantly. You can now freely `git commit` your `gee_logic.py` file!
