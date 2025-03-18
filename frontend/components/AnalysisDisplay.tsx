// ✅ components/AnalysisDisplay.tsx
'use client';
export function AnalysisDisplay({ result }: { result: any }) {
  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <h2 className="text-2xl font-bold mb-2">分析结果</h2>
      <p className="text-lg font-semibold">评分：{result.score} 分</p>
      <p className="mt-2 text-gray-700">反馈：{result.feedback}</p>
      {result.recommendations && result.recommendations.length > 0 && (
        <div className="mt-4">
          <h3 className="font-bold">改进建议：</h3>
          <ul className="list-disc list-inside text-gray-600">
            {result.recommendations.map((item: string, idx: number) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
