// ✅ components/LoadingSpinner.tsx
'use client';
export function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center py-4">
      <div className="h-12 w-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
      <p className="mt-2 text-sm text-gray-600">正在分析简历，请稍候…</p>
    </div>
  );
}