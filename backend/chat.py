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
            model = genai.GenerativeModel('gemini-pro')
            
            # Add system prompt context
            system_prompt = "You are an expert Italian Pizza Chef assistant. You help users with pizza dough recipes, fermentation, and baking tips. Keep answers concise and helpful."
            full_prompt = f"{system_prompt}\n\nUser: {user_message}\nChef:"
            
            response = model.generate_content(full_prompt)
            return jsonify({'response': response.text})
        except Exception as e:
            print(f"Gemini API Error: {e}")
            # Fallback to local logic if API fails
            pass

    # 2. Fallback to Local Logic (Mock AI)
    user_message = user_message.lower()
    response_text = "I'm not sure about that. Try asking about flour, yeast, or fermentation time!"

    if 'hello' in user_message or 'hi' in user_message:
        response_text = "Ciao! I'm your Pizza Helper Chef. Ask me anything about your dough!"
    
    elif 'flour' in user_message:
        response_text = "For pizza, '00' flour is usually best because it's finely ground and has the right protein content for a stretchy dough. Bread flour is a good alternative."
        
    elif 'yeast' in user_message:
        response_text = "Fresh yeast is traditional, but Instant Dry Yeast (IDY) is very convenient. Use about 1/3 the amount of IDY compared to fresh yeast."
        
    elif 'water' in user_message or 'hydration' in user_message:
        response_text = "Hydration is the ratio of water to flour. 60% is standard and easy to work with. Higher hydration (70%+) makes for a airier crust but is stickier to handle."
        
    elif 'temp' in user_message or 'heat' in user_message:
        response_text = "Pizza loves heat! If you're using a home oven, crank it to the max (usually 250°C/500°F) and use a pizza stone or steel if you have one."
        
    elif 'time' in user_message or 'proof' in user_message:
        response_text = "Longer fermentation usually means better flavor. A 24-hour cold ferment in the fridge develops amazing complexity."

    elif 'sticky' in user_message:
        response_text = "If your dough is too sticky, try wetting your hands instead of adding more flour. Adding too much flour can make the crust tough."

    return jsonify({'response': response_text})
