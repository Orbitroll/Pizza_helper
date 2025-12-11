from flask import Blueprint, request, jsonify
import os
import google.generativeai as genai

chat_bp = Blueprint('chat', __name__)

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@chat_bp.route('/ask', methods=['POST'])
def ask_bot():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # 1. Try using Google Gemini (Free Tier) if Key is present
    if GEMINI_API_KEY:
        try:
            # Use gemini-flash-latest as it is available and likely has quota
            model = genai.GenerativeModel('gemini-flash-latest')
            
            # Add system prompt context
            system_prompt = "You are an expert Italian Pizza Chef assistant. You help users with pizza dough recipes, fermentation, and baking tips. You can speak many languages. If the user speaks Hebrew, reply in Hebrew. Keep answers concise and helpful."
            full_prompt = f"{system_prompt}\n\nUser: {user_message}\nChef:"
            
            response = model.generate_content(full_prompt)
            return jsonify({'response': response.text})
        except Exception as e:
            print(f"ERROR: Gemini API Error: {e}", flush=True)
            # Fallback to local logic if API fails
            pass

    # 2. Fallback to Local Logic (Mock AI)
    user_message_lower = user_message.lower()
    
    # Check for Hebrew characters
    is_hebrew = any("\u0590" <= c <= "\u05EA" for c in user_message)
    
    if is_hebrew:
        response_text = "אני לא בטוח לגבי זה. נסה לשאול על קמח, שמרים או זמן התפחה!"
        if 'שלום' in user_message or 'היי' in user_message:
            response_text = "צ'או! אני עוזר השף שלך לפיצה. תשאל אותי כל דבר על הבצק שלך!"
        elif 'קמח' in user_message:
            response_text = "לפיצה, קמח '00' הוא בדרך כלל הטוב ביותר כי הוא טחון דק ויש לו את תכולת החלבון הנכונה לבצק גמיש. קמח לחם הוא חלופה טובה."
        elif 'שמרים' in user_message:
            response_text = "שמרים טריים הם המסורתיים, אבל שמרים יבשים (IDY) נוחים מאוד. השתמש בכ-1/3 מהכמות של שמרים יבשים לעומת שמרים טריים."
        elif 'מים' in user_message or 'הידרציה' in user_message:
            response_text = "הידרציה היא היחס בין המים לקמח. 60% זה סטנדרט וקל לעבודה. הידרציה גבוהה יותר (70%+) נותנת קראסט אוורירי יותר אבל דביק יותר לעבודה."
    else:
        response_text = "I'm not sure about that. Try asking about flour, yeast, or fermentation time!"

        if 'hello' in user_message_lower or 'hi' in user_message_lower:
            response_text = "Ciao! I'm your Pizza Helper Chef. Ask me anything about your dough!"
        
        elif 'flour' in user_message_lower:
            response_text = "For pizza, '00' flour is usually best because it's finely ground and has the right protein content for a stretchy dough. Bread flour is a good alternative."
            
        elif 'yeast' in user_message_lower:
            response_text = "Fresh yeast is traditional, but Instant Dry Yeast (IDY) is very convenient. Use about 1/3 the amount of IDY compared to fresh yeast."
            
        elif 'water' in user_message_lower or 'hydration' in user_message_lower:
            response_text = "Hydration is the ratio of water to flour. 60% is standard and easy to work with. Higher hydration (70%+) makes for a airier crust but is stickier to handle."
        
    elif 'temp' in user_message or 'heat' in user_message:
        response_text = "Pizza loves heat! If you're using a home oven, crank it to the max (usually 250°C/500°F) and use a pizza stone or steel if you have one."
        
    elif 'time' in user_message or 'proof' in user_message:
        response_text = "Longer fermentation usually means better flavor. A 24-hour cold ferment in the fridge develops amazing complexity."

    elif 'sticky' in user_message:
        response_text = "If your dough is too sticky, try wetting your hands instead of adding more flour. Adding too much flour can make the crust tough."

    return jsonify({'response': response_text})
