# 📄 CV Checker - 简历智能分析系统

这是一个基于 **FastAPI + OpenAI GPT + Next.js (TypeScript + Tailwind CSS)** 的简历智能分析系统。  
用户可以上传简历文件（如 PDF），系统自动提取简历文本并调用 GPT 模型进行打分与优化建议反馈。

---

## 📁 项目结构

```
.
├── backend/           # FastAPI 后端服务
│   ├── main.py        - 主接口逻辑，处理简历上传与 GPT 调用
│   ├── temp_cv.pdf    - 临时存储简历 PDF（不建议提交）
│   ├── .env           - 后端环境变量（请使用 .env.example）
│   └── requirements.txt
├── frontend/          # Next.js 前端页面
│   ├── src/           - 页面与组件目录
│   ├── public/        - 静态资源
│   └── .env.local     - 前端环境变量（可选）
```

---

## 🚀 快速开始

### 📦 1. 安装后端依赖

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### ⚙️ 2. 配置后端环境变量

创建 `backend/.env` 文件，内容如下：

```
OPENAI_API_KEY=your-openai-api-key-here
```

> ✅ 推荐提交 `.env.example` 到仓库，用于团队参考。

### ▶️ 3. 启动 FastAPI 后端服务

```bash
uvicorn main:app --reload
```

访问自动文档：[http://localhost:8000/docs](http://localhost:8000/docs)

---

### 📦 4. 安装前端依赖

```bash
cd frontend
npm install
```

### ▶️ 5. 启动前端开发服务器

```bash
npm run dev
```

访问前端页面：[http://localhost:3000](http://localhost:3000)

---

## 📑 示例 API（POST `/api/analyze-cv`）

上传简历文件（PDF），返回分析结果：
```json
{
  "status": "success",
  "analysis": "简历评分：85分，建议优化..."
}
```

---

## 📚 技术栈

- **前端**：Next.js (React + TypeScript + Tailwind CSS)
- **后端**：FastAPI
- **模型服务**：OpenAI GPT-3.5 Turbo
- **PDF解析**：PyMuPDF (fitz)

---

## 📂 TODO / Roadmap

- [ ] 支持 .docx / .txt 文件解析
- [ ] GPT 输出结构化 JSON（评分、建议等字段）
- [ ] 用户系统与简历历史管理
- [ ] 多语言支持（中文/英文简历）
- [ ] Docker 一键部署

---

## 📄 License

MIT License © 2025 CV Checker Team
