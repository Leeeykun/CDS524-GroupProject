# 糖尿病预测系统

![Python](https://img.shields.io/badge/Python-3.12-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange) ![Flask](https://img.shields.io/badge/Flask-2.3.3-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 项目概述

糖尿病预测系统是一个基于机器学习的预测工具，旨在通过患者的健康数据预测其是否可能患有糖尿病。该系统使用多种特征选择方法和机器学习模型对数据进行分析，并通过一个基于 **Flask** 的 Web 服务提供批量预测功能。前端通过 HTML 页面与后端交互，用户可以上传 CSV 文件以获取预测结果。

本项目包含以下主要功能：
- 数据清理和预处理
- 多种特征选择方法（F 检验、互信息法、RFE、随机森林特征重要性、L1 正则化）
- 多种机器学习模型（逻辑回归、随机森林、XGBoost、MLP、集成模型）的训练和评估
- Flask Web 服务，支持批量预测并返回 JSON 格式的结果

## 数据集

项目使用的数据集为 `data.csv`，包含 1879 条记录和 46 个特征，主要包括：
- 患者基本信息（如年龄、性别、BMI）
- 生活方式特征（如吸烟、饮酒、运动）
- 临床指标（如血压、血糖、HbA1c）
- 目标变量 `Diagnosis`（0 表示未患糖尿病，1 表示患糖尿病）

## 功能

1. **数据清理**：
   - 检查缺失值和重复值

2. **特征选择**：
   - 使用多种方法选择重要特征：
     - F 检验（`SelectKBest` with `f_classif`）
     - 互信息法（`SelectKBest` with `mutual_info_classif`）
     - 递归特征消除（RFE with RandomForestClassifier）
     - 随机森林特征重要性
     - L1 正则化（Lasso）

3. **模型训练与评估**：
   - 基线模型：逻辑回归
   - 其他模型：随机森林、XGBoost、MLP、集成模型（Stacking）
   - 评估指标：交叉验证准确率、混淆矩阵、分类报告、ROC 曲线和 AUC 分数

4. **Flask Web 服务**：
   - 使用 Flask 构建后端服务，支持批量预测
   - 用户通过前端页面上传 CSV 文件，获取糖尿病预测结果
   - 返回 JSON 格式的预测结果，包含部分原始特征和预测结果（`Diabetic` 列，值为 "Yes" 或 "No"）

## 安装

### 环境要求
- Python 3.12 或以上
- 推荐使用虚拟环境（如 `venv` 或 `conda`）

### 安装步骤
1. 克隆项目仓库：
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-system.git
   cd diabetes-prediction-system

2. 安装依赖：
   ```bash
   pip install -r requirements.txt

3. 启动 Flask 应用：
  在项目根目录下运行以下命令：
  Flask 应用将启动
   ```bash
   python app.py
 默认地址为 http://127.0.0.1:5000
 
4.使用 Web 界面：
 打开浏览器，访问 http://127.0.0.1:5000。
 在页面上上传一个 CSV 文件（确保包含所有必需的特征列）。
 提交后，页面将显示预测结果（以 JSON 格式返回）。
