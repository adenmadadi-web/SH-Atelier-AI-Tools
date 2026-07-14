import numpy as np

def generate_size_chart(base_size=38):
    sizes = [34, 36, 38, 40, 42, 44]
    bust = [84, 88, 92, 96, 100, 104]
    waist = [66, 70, 74, 78, 82, 86]
    hip = [90, 94, 98, 102, 106, 110]

    chart = []
    for i, s in enumerate(sizes):
        chart.append({
            "size": s,
            "bust": bust[i],
            "waist": waist[i],
            "hip": hip[i]
        })
    return chart

if __name__ == "__main__":
    chart = generate_size_chart()
    print("جدول سایزبندی کت زنانه:")
    for row in chart:
        print(f"سایز {row['size']}: سینه {row['bust']}، کمر {row['waist']}، باسن {row['hip']}")
