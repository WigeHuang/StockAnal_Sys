#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API测试脚本
"""

import os
import requests
import json

def test_deepseek_api():
    """测试DeepSeek API"""
    print("🔧 测试DeepSeek API...")
    
    # API配置
    api_key = "sk-bd2a7e8394c745338a15f926c0e611a0"
    api_url = "https://api.deepseek.com/v1/chat/completions"
    model = "deepseek-chat"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Hello, this is a test message. Please respond with a short greeting."}
        ],
        "max_tokens": 50,
        "temperature": 0.7
    }
    
    try:
        print("🧪 发送API请求...")
        response = requests.post(api_url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        print("✅ API调用成功!")
        print(f"回复: {result['choices'][0]['message']['content']}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API调用失败: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"响应状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text}")
        return False
    except Exception as e:
        print(f"❌ 其他错误: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_deepseek_api()
    if success:
        print("\n🎉 DeepSeek API测试成功！")
    else:
        print("\n⚠️ DeepSeek API测试失败！") 