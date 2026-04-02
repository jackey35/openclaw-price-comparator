#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw 云比价价格更新脚本
用于定期检查和更新价格数据
"""

import os
import json
from datetime import datetime

# 价格数据文件
PRICE_FILE = "/Users/brtc/.openclaw/workspace/cloud-price-comparator/index.html"

# 手动更新的价格数据 (需要定期检查各官网更新)
CURRENT_PRICES = {
    "aliyun": {
        "name": "阿里云",
        "logo": "🏢",
        "color": "aliyun",
        "type": "一键部署OpenClaw",
        "price": "¥9.9起",  # 首月
        "note": "轻量服务器+CodingPlan"
    },
    "tencent": {
        "name": "腾讯云",
        "logo": "🔷", 
        "color": "tencent",
        "type": "一键部署OpenClaw",
        "price": "¥7.9起",  # 首月
        "note": "轻量服务器+CodingPlan"
    },
    "volcengine": {
        "name": "火山引擎",
        "logo": "🌋",
        "color": "volcengine", 
        "type": "ArkClaw",
        "price": "¥9.9起",
        "note": "新用户免费"
    }
}

def check_updates():
    """检查价格更新"""
    print("=" * 50)
    print("OpenClaw 云比价价格检查")
    print(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    
    print("\n当前价格:")
    for key, data in CURRENT_PRICES.items():
        print(f"  {data['name']}: {data['price']} ({data['note']})")
    
    print("\n需要手动检查的官网:")
    print("  - 阿里云: https://www.aliyun.com/activity/ecs/clawdbot")
    print("  - 腾讯云: https://cloud.tencent.com/act/pro/lighthouse-moltbot")
    print("  - 火山引擎: https://www.volcengine.com/experience/ark")
    
    print("\n" + "=" * 50)
    print("提示: 价格由各云厂商官网活动决定，需定期手动检查更新")
    print("=" * 50)

def main():
    check_updates()

if __name__ == "__main__":
    main()
