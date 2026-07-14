
from anthropic import Anthropic

client = Anthropic()  # نیاز به ANTHROPIC_API_KEY در محیط

def generate_caption(style, color, vibe):
    prompt = f"یک کپشن اینستاگرامی لوکس برای کت {color} با سبک {style} و حال‌و‌هوای {vibe} بنویس."

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

if __name__ == "__main__":
    caption = generate_caption("استریت فشن", "کرم", "لوکس و مینیمال")
    print("کپشن پیشنهادی:")
    print(caption)
