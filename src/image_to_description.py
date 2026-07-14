from anthropic import Anthropic
from PIL import Image

client = Anthropic()

def describe_garment_from_text_prompt(text_hint):
    prompt = (
        f"بر اساس این توضیح کوتاه: {text_hint} "
        "یک توضیح فنی کامل برای لباس بنویس (نوع پارچه، جزئیات دوخت، فرم، استایل، کاربرد)."
    )

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=350,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

if __name__ == "__main__":
    hint = "کت کرم زنانه با برش مینیمال، مناسب استایل لوکس و رسمی"
    desc = describe_garment_from_text_prompt(hint)
    print("توضیح فنی لباس:")
    print(desc)
