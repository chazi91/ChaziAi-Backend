from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# إنشاء Blueprint للمسارات
gemini_bp = Blueprint('gemini', __name__)

@gemini_bp.route('/chat', methods=['POST'])
@cross_origin()
def chat_with_gemini():
    """
    نقطة نهاية للمحادثة مع Gemini AI (نسخة مبسطة للاختبار)
    """
    try:
        # الحصول على البيانات من الطلب
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'رسالة مطلوبة',
                'success': False
            }), 400
        
        user_message = data['message']
        
        # رد تجريبي (يمكن استبداله بـ API حقيقي لاحقاً)
        response_text = f"مرحباً! تلقيت رسالتك: '{user_message}'. هذا رد تجريبي من ChaziAi. سيتم تفعيل Gemini API قريباً."
        
        return jsonify({
            'response': response_text,
            'success': True
        })
            
    except Exception as e:
        print(f"خطأ في API: {str(e)}")
        return jsonify({
            'error': 'حدث خطأ في الخادم',
            'success': False
        }), 500

@gemini_bp.route('/health', methods=['GET'])
@cross_origin()
def health_check():
    """
    فحص حالة الخدمة
    """
    return jsonify({
        'status': 'healthy',
        'gemini_api': 'demo_mode',
        'success': True
    })

@gemini_bp.route('/capabilities', methods=['GET'])
@cross_origin()
def get_capabilities():
    """
    الحصول على قدرات النموذج
    """
    return jsonify({
        'model': 'gemini-demo',
        'capabilities': [
            'معالجة اللغة الطبيعية',
            'الإجابة على الأسئلة',
            'التلخيص',
            'الترجمة',
            'كتابة المحتوى',
            'حل المشاكل',
            'البرمجة'
        ],
        'languages': ['العربية', 'الإنجليزية', 'وأكثر من 100 لغة أخرى'],
        'success': True
    })

