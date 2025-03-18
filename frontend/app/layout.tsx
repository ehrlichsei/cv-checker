// ✅ app/layout.tsx
export const metadata = {
  title: 'CV Checker',
  description: '智能简历分析平台',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-800">{children}</body>
    </html>
  );
}