from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# إنشاء Blueprint للمسارات
gemini_bp = Blueprint('gemini', __name__)

# محاولة استيراد Gemini API
try:
    import google.generativeai as genai
    
    # تكوين Gemini API
    GEMINI_API_KEY = "AIzaSyAQqiR_f5DuUN98Dvdp2aYfmwoQxk0fwa0"
    genai.configure(api_key=GEMINI_API_KEY)
    
    # إنشاء نموذج Gemini
    model = genai.GenerativeModel('gemini-1.5-flash')
    GEMINI_AVAILABLE = True
    print("Gemini API loaded successfully!")
    
except Exception as e:
    print(f"Failed to load Gemini API: {e}")
    GEMINI_AVAILABLE = False
    model = None

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
        
        if GEMINI_AVAILABLE and model:
            try:
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
                        'success': True,
                        'source': 'gemini_api'
                    })
                else:
                    raise Exception("No response from Gemini")
                    
            except Exception as gemini_error:
                print(f"Gemini API error: {gemini_error}")
                # Fallback to demo response
                pass
        
        # رد تجريبي في حالة عدم توفر Gemini
        response_text = f"مرحباً! تلقيت رسالتك: '{user_message}'. أنا ChaziAi، مساعدك الذكي. كيف يمكنني مساعدتك اليوم؟"
        
        return jsonify({
            'response': response_text,
            'success': True,
            'source': 'demo_mode'
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
    if GEMINI_AVAILABLE:
        return jsonify({
            'status': 'healthy',
            'gemini_api': 'available',
            'success': True
        })
    else:
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
    model_name = 'gemini-1.5-flash' if GEMINI_AVAILABLE else 'gemini-demo'
    
    return jsonify({
        'model': model_name,
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
        'gemini_available': GEMINI_AVAILABLE,
        'success': True
    })

