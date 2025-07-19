# استخدم صورة Python الرسمية
FROM python:3.10-slim

# إعداد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى داخل الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# تحديد المنفذ الذي سيعمل عليه التطبيق
EXPOSE 5000

# أمر التشغيل
CMD ["python", "app.py"]
