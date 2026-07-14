from anthropic import Anthropic

client = Anthropic()

def tailoring_advice(garment_type, fabric, issue):
    prompt = (
        f"برای یک {garment_type} با پارچه {fabric}، "
        f"مشکل/نیاز: {issue}. "
        "به صورت نکته‌وار، چند پیشنهاد حرفه‌ای خیاطی و اصلاح الگو بده."
    )

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

if __name__ == "__main__":
    tips = tailoring_advice(
        garment_type="کت زنانه",
        fabric="کرپ کرم",
        issue="کت روی شانه‌ها کمی آزاد است و می‌خواهم فیت لوکس‌تر شود"
    )
    print("پیشنهادهای خیاطی:")
    print(tips)
