#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API配置示例
作为OpenAI API的替代方案
"""

import os
import requests
import json

class DeepSeekAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY', 'sk-bd2a7e8394c745338a15f926c0e611a0')
        self.base_url = "https://api.deepseek.com/v1"
        
    def chat_completion(self, messages, model="deepseek-chat", max_tokens=1000):
        """调用DeepSeek聊天API"""
        url = f"{self.base_url}/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"DeepSeek API调用失败: {str(e)}")
            return None

def test_deepseek_api():
    """测试DeepSeek API"""
    print("🔧 测试DeepSeek API...")
    
    api = DeepSeekAPI()
    
    messages = [
        {"role": "user", "content": "Hello, this is a test message."}
    ]
    
    try:
        response = api.chat_completion(messages, max_tokens=50)
        if response:
            print("✅ DeepSeek API调用成功!")
            print(f"回复: {response['choices'][0]['message']['content']}")
            return True
        else:
            print("❌ DeepSeek API调用失败")
            return False
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    test_deepseek_api() 