from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# 添加 CORS（允许前端访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyze-cv")
async def analyze_cv(file: UploadFile = File(...)) -> Dict:
    try:
        # 读取 PDF 文件内容
        contents = await file.read()

        with open("temp_cv.pdf", "wb") as f:
            f.write(contents)

        # 提取简历文本
        doc = fitz.open("temp_cv.pdf")
        cv_text = ""
        for page in doc:
            cv_text += page.get_text()
        doc.close()

        # 构建 prompt
        prompt = f"""请你帮我分析下面这份简历内容，并按照如下 JSON 格式回答：
        {{
            "score": 0-100 分之间的整数,
            "feedback": "整体反馈一句话",
            "recommendations": ["建议一", "建议二", "..."]
        }}
        简历内容如下：
        {cv_text}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位资深的简历评估专家，具有多年人力资源和招聘经验，请用 JSON 格式返回内容。"},
                {"role": "user", "content": prompt}
            ]
        )

        # 尝试解析 AI 返回的 JSON
        import json
        content = response.choices[0].message.content
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            print("❌ GPT 返回格式不合法：", content)
            raise HTTPException(status_code=500, detail="AI返回格式错误")

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 

