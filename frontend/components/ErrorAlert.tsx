// ✅ components/ErrorAlert.tsx
'use client';
export function ErrorAlert({ message }: { message: string }) {
  return (
    <div className="bg-red-100 text-red-700 border border-red-300 p-4 rounded mb-4">
      ❌ 错误：{message}
    </div>
  );
}