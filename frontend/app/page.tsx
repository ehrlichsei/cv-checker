// ✅ app/page.tsx
'use client';
import { useState } from 'react';
import { FileUploader } from '../components/FileUploader';
import { AnalysisDisplay } from '../components/AnalysisDisplay';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { ErrorAlert } from '../components/ErrorAlert';

export default function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUpload = async (file: File) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const res = await fetch('http://127.0.0.1:8000/api/analyze-cv', {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) throw new Error('分析失败，请重试。');

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : '未知错误');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="max-w-3xl mx-auto p-6">
      <h1 className="text-4xl font-bold mb-6 text-center">📄 CV Checker 简历分析系统</h1>
      <FileUploader onFileUpload={handleUpload} />
      {loading && <LoadingSpinner />}
      {error && <ErrorAlert message={error} />}
      {result && <AnalysisDisplay result={result} />}
    </main>
  );
}
