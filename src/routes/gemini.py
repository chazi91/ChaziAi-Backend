import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# إنشاء Blueprint للمسارات
gemini_bp = Blueprint('gemini', __name__)

# تكوين Gemini API
GEMINI_API_KEY = "AIzaSyAQqiR_f5DuUN98Dvdp2aYfmwoQxk0fwa0"
genai.configure(api_key=GEMINI_API_KEY)

# إنشاء نموذج Gemini
model = genai.GenerativeModel('gemini-1.5-flash')

@gemini_bp.route('/chat', methods=['POST'])
@cross_origin()
def chat_with_gemini():
    """
    نقطة نهاية للمحادثة مع Gemini AI
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
        
        # إضافة سياق للرسالة لجعل الرد باللغة العربية
        context = """أنت مساعد ذكي اسمه ChaziAi. أجب باللغة العربية دائماً وكن مفيداً ومهذباً. 
        أنت متخصص في الذكاء الاصطناعي والتكنولوجيا. إليك سؤال المستخدم:"""
        
        full_message = f"{context}\n\n{user_message}"
        
        # إرسال الرسالة إلى Gemini
        response = model.generate_content(full_message)
        
        # التحقق من وجود رد
        if response.text:
            return jsonify({
                'response': response.text,
                'success': True
            })
        else:
            return jsonify({
                'error': 'لم أتمكن من إنشاء رد مناسب',
                'success': False
            }), 500
            
    except Exception as e:
        print(f"خطأ في Gemini API: {str(e)}")
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
    try:
        # فحص بسيط للتأكد من تكوين API
        if GEMINI_API_KEY:
            return jsonify({
                'status': 'healthy',
                'gemini_api': 'configured',
                'success': True
            })
        else:
            return jsonify({
                'status': 'unhealthy',
                'gemini_api': 'not_configured',
                'success': False
            }), 500
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'gemini_api': 'error',
            'error': str(e),
            'success': False
        }), 500

@gemini_bp.route('/capabilities', methods=['GET'])
@cross_origin()
def get_capabilities():
    """
    الحصول على قدرات النموذج
    """
    return jsonify({
        'model': 'gemini-1.5-flash',
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

