# ChaziAi Backend

مشروع الخادم الخلفي لتطبيق ChaziAi - مساعد ذكي يعمل بتقنية Gemini AI من Google.

## الوصف

ChaziAi هو مساعد ذكي يستخدم تقنية Gemini AI لتقديم إجابات ذكية ومفيدة باللغة العربية. يوفر هذا المشروع واجهة برمجة تطبيقات (API) للتفاعل مع نموذج Gemini AI.

## المميزات

- 🤖 تكامل مع Gemini AI API
- 🌐 دعم كامل للغة العربية
- 🔄 واجهة برمجة تطبيقات RESTful
- 📱 دعم CORS للتطبيقات الأمامية
- 🗄️ قاعدة بيانات SQLite مدمجة
- 🎯 واجهة ويب مدمجة

## التثبيت والتشغيل

### المتطلبات

- Python 3.11+
- pip3

### خطوات التثبيت

1. استنساخ المستودع:
```bash
git clone https://github.com/chazi91/chaziai-backend.git
cd chaziai-backend
```

2. تثبيت التبعيات:
```bash
pip3 install -r requirements.txt
```

3. تشغيل الخادم:
```bash
python3 src/main.py
```

الخادم سيعمل على العنوان: `http://localhost:5000`

## واجهة برمجة التطبيقات (API)

### نقاط النهاية المتاحة

#### 1. فحص حالة الخدمة
```
GET /api/gemini/health
```

#### 2. الحصول على قدرات النموذج
```
GET /api/gemini/capabilities
```

#### 3. المحادثة مع الذكاء الاصطناعي
```
POST /api/gemini/chat
Content-Type: application/json

{
  "message": "رسالتك هنا"
}
```

### أمثلة على الاستخدام

#### اختبار حالة الخدمة:
```bash
curl -X GET http://localhost:5000/api/gemini/health
```

#### إرسال رسالة للذكاء الاصطناعي:
```bash
curl -X POST http://localhost:5000/api/gemini/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "مرحبا، كيف حالك؟"}'
```

## هيكل المشروع

```
chaziai-backend/
├── src/
│   ├── main.py              # الملف الرئيسي للتطبيق
│   ├── models/              # نماذج قاعدة البيانات
│   │   └── user.py
│   ├── routes/              # مسارات API
│   │   ├── gemini_hybrid.py # مسارات Gemini AI
│   │   └── user.py          # مسارات المستخدمين
│   ├── static/              # الملفات الثابتة للواجهة الأمامية
│   └── database/            # قاعدة البيانات
├── requirements.txt         # التبعيات المطلوبة
└── README.md               # هذا الملف
```

## التكوين

### مفتاح Gemini API

المشروع يستخدم مفتاح Gemini API المكون مسبقاً. في حالة الحاجة لتغييره، يمكن تعديل المتغير `GEMINI_API_KEY` في ملف `src/routes/gemini_hybrid.py`.

### قاعدة البيانات

يستخدم المشروع قاعدة بيانات SQLite محلية تُنشأ تلقائياً عند التشغيل الأول.

## الأمان

- تأكد من عدم مشاركة مفتاح API في الكود المصدري العام
- استخدم متغيرات البيئة لتخزين المفاتيح الحساسة في البيئة الإنتاجية

## المساهمة

نرحب بالمساهمات! يرجى إنشاء Pull Request أو فتح Issue لأي اقتراحات أو تحسينات.

## الترخيص

هذا المشروع مرخص تحت رخصة MIT.

## الدعم

للحصول على الدعم أو الإبلاغ عن مشاكل، يرجى فتح Issue في المستودع.

---

تم تطوير هذا المشروع بواسطة فريق ChaziAi 🚀

