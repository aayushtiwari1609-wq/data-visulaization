import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# ── Sample Data ──────────────────────────────────────────
categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales      = [4200, 3800, 5100, 4700, 6200, 5800]
returns    = [300,  420,  390,  510,  480,  620]
products   = ['Laptops', 'Phones', 'Tablets', 'Watches', 'Earbuds']
market_share = [35, 28, 18, 12, 7]

df = pd.DataFrame({'Month': categories, 'Sales': sales, 'Returns': returns})

sns.set_theme(style='whitegrid', palette='muted')
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Sales Dashboard', fontsize=16, fontweight='bold', y=1.02)

# ── 1. Bar Chart ─────────────────────────────────────────
ax1 = axes[0]
sns.barplot(data=df, x='Month', y='Sales', palette='Blues_d', ax=ax1)
ax1.set_title('Monthly Sales', fontsize=13, fontweight='bold')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales ($)')
for bar in ax1.patches:
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 50,
        f"${int(bar.get_height()):,}",
        ha='center', va='bottom', fontsize=9
    )

# ── 2. Line Chart ────────────────────────────────────────
ax2 = axes[1]
ax2.plot(df['Month'], df['Sales'],   marker='o', linewidth=2.5,
         color='#2a78d6', label='Sales',   markersize=7)
ax2.plot(df['Month'], df['Returns'], marker='s', linewidth=2.5,
         color='#e34948', label='Returns', markersize=7, linestyle='--')
ax2.fill_between(df['Month'], df['Sales'], alpha=0.08, color='#2a78d6')
ax2.set_title('Sales vs Returns Trend', fontsize=13, fontweight='bold')
ax2.set_xlabel('Month')
ax2.set_ylabel('Amount ($)')
ax2.legend()
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x):,}'))

# ── 3. Pie Chart ─────────────────────────────────────────
ax3 = axes[2]
colors = ['#2a78d6', '#1baf7a', '#eda100', '#4a3aa7', '#e34948']
wedges, texts, autotexts = ax3.pie(
    market_share,
    labels=products,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    pctdistance=0.82,
    wedgeprops=dict(width=0.6)   # donut style
)
for text in autotexts:
    text.set_fontsize(9)
    text.set_color('white')
ax3.set_title('Market Share by Product', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('charts.png', dpi=150, bbox_inches='tight')
plt.show()