<div align="center">
  <a href="./README.md">
    <h1>📸 Mobile Photo Organizer</h1>
  </a>

  <p align="center">
    <strong>一款适用于 macOS 和 Windows 的手机照片整理工具 (支持 iPhone & Android)。</strong>
  </p>

  <p align="center">
    <a href="README.md">English</a> •
    <a href="README_zh.md">简体中文</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue" alt="Python Version">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows-lightgrey" alt="Platform">
  </p>
</div>

---

## 📖 简介

**Mobile Photo Organizer** 帮助您将 iPhone / Android 照片和视频备份到 Mac / Windows 电脑（或外接硬盘），同时保留：
- **实况照片 (Live Photos)**：保持 `.HEIC` 图片和 `.MOV` 视频成对存放。
- **Android 支持**：兼容 Android 的 `.JPG` 和 `.MP4` 文件。
- **元数据**：保留原始拍摄日期和时间。
- **地理位置**：根据拍摄地点自动整理文件夹（例如：`2023/10/2023-10-01_Shanghai`）。

## ✨ 功能特性

- **实况照片支持**：自动检测并分组 `IMG_X.HEIC` 和 `IMG_X.MOV`。
- **智能地理编码**：将 GPS 坐标转换为可读的城市名称（需要联网）。
- **按日期排序**：将文件整理为 `年 -> 月 -> 日期_地点` 的结构。
- **重复处理**：导入时智能处理重复文件。
- **友好界面**：基于 Streamlit 构建的 Web 界面，操作简单直观。

## 🚀 快速开始

### 前置要求
- macOS 或 Windows 系统
- 已安装 Python 3

### 安装与使用

#### macOS / Linux

1.  **克隆或下载** 本仓库。
2.  **运行启动脚本**：
    在项目文件夹中打开终端并运行：
    ```bash
    chmod +x start.sh
    ./start.sh
    ```
    *此脚本会自动配置环境并启动应用程序。*

#### Windows

1.  **克隆或下载** 本仓库。
2.  **运行启动脚本**：
    在项目文件夹中双击运行 `start.bat`。
    *此脚本会自动配置环境并启动应用程序。*

3.  **使用 Web 应用**：
    - 应用将在浏览器中自动打开（通常为 `http://localhost:8501`）。
    - 选择 **源文件夹**（iPhone 或 Android 的原始备份）。
    - 选择 **目标文件夹**（您希望存放整理后照片的位置）。
    - 点击 **开始整理**。

## 🛠 手动安装 (可选)

如果您不想使用 `start.sh`，可以手动运行：

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run app.py
```

## 📄 许可证

本项目采用 MIT 许可证。
