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


# Print the API key
print("API Key:", OPENAI_API_KEY)

@app.post("/api/analyze-cv")
async def analyze_cv(file: UploadFile = File(...)) -> Dict:
    try:
        # 读取 PDF 文件内容（为二进制）
        contents = await file.read()

        # 使用 PyMuPDF 从二进制中读取文本
        with open("temp_cv.pdf", "wb") as f:
            f.write(contents)

        # 用 PyMuPDF 打开 PDF 文件
        doc = fitz.open("temp_cv.pdf")
        cv_text = ""
        for page in doc:
            cv_text += page.get_text()
        doc.close()

        # 构建 prompt
        prompt = f"""请你帮我分析下面这份简历内容，并提供以下几点内容：
                1. 总体评分（0-100 分）
                2. 简历中的优点
                3. 简历中需要改进的地方
                4. 格式排版方面的建议
                5. 内容补充/优化建议

                简历内容如下：
                {cv_text}
                """


        # GPT 调用
        response =  client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一位资深的简历评估专家，具有多年人力资源和招聘经验，请用中文分析并提供专业建议。"},
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "status": "success",
            "analysis": response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 

