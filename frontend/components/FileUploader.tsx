// ✅ components/FileUploader.tsx
'use client';
import React from 'react';

export function FileUploader({ onFileUpload }: { onFileUpload: (file: File) => void }) {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && file.type === 'application/pdf') {
      onFileUpload(file);
    } else {
      alert('请上传 PDF 文件');
    }
  };

  return (
    <div className="bg-white p-4 rounded-lg shadow mb-6">
      <label className="block font-medium mb-2">上传你的简历 PDF：</label>
      <input type="file" accept="application/pdf" onChange={handleChange} />
    </div> 
  );
}