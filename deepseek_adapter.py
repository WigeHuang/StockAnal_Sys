#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DeepSeek API适配器
使DeepSeek API与OpenAI接口兼容
"""

import os
import requests
import json
import time
from typing import Dict, List, Optional, Any

class DeepSeekAdapter:
    """DeepSeek API适配器，模拟OpenAI接口"""
    
    def __init__(self, api_key=None, api_base=None):
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        self.api_base = api_base or os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1')
        self.model = os.getenv('DEEPSEEK_API_MODEL', 'deepseek-chat')
        
    def ChatCompletion(self):
        """返回ChatCompletion类"""
        return DeepSeekChatCompletion(self.api_key, self.api_base, self.model)

class DeepSeekChatCompletion:
    """模拟OpenAI的ChatCompletion类"""
    
    def __init__(self, api_key, api_base, model):
        self.api_key = api_key
        self.api_base = api_base
        self.model = model
    
    @staticmethod
    def create(**kwargs):
        """创建聊天完成请求"""
        adapter = DeepSeekChatCompletion._get_adapter()
        return adapter._create_chat_completion(**kwargs)
    
    @staticmethod
    def _get_adapter():
        """获取适配器实例"""
        api_key = os.getenv('DEEPSEEK_API_KEY')
        api_base = os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1')
        model = os.getenv('DEEPSEEK_API_MODEL', 'deepseek-chat')
        return DeepSeekChatCompletion(api_key, api_base, model)
    
    def _create_chat_completion(self, **kwargs):
        """创建聊天完成请求"""
        url = f"{self.api_base}/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # 转换参数格式
        data = {
            "model": kwargs.get('model', self.model),
            "messages": kwargs.get('messages', []),
            "max_tokens": kwargs.get('max_tokens', 1000),
            "temperature": kwargs.get('temperature', 0.7),
            "stream": kwargs.get('stream', False)
        }
        
        # 处理工具调用（如果支持）
        if 'tools' in kwargs:
            data['tools'] = kwargs['tools']
        if 'tool_choice' in kwargs:
            data['tool_choice'] = kwargs['tool_choice']
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=kwargs.get('timeout', 30))
            response.raise_for_status()
            
            result = response.json()
            
            # 转换为OpenAI格式
            return {
                "choices": [
                    {
                        "message": {
                            "content": result['choices'][0]['message']['content'],
                            "role": "assistant"
                        },
                        "finish_reason": result['choices'][0].get('finish_reason', 'stop')
                    }
                ],
                "usage": result.get('usage', {}),
                "model": result.get('model', self.model)
            }
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"DeepSeek API调用失败: {str(e)}")

# 全局变量，用于替换openai模块
openai = DeepSeekAdapter()

def patch_openai():
    """修补openai模块以使用DeepSeek"""
    import sys
    import types
    
    # 创建模拟的openai模块
    mock_openai = types.ModuleType('openai')
    mock_openai.ChatCompletion = DeepSeekChatCompletion
    mock_openai.api_key = None
    mock_openai.api_base = None
    
    # 替换sys.modules中的openai
    sys.modules['openai'] = mock_openai
    
    return mock_openai

def test_deepseek_adapter():
    """测试DeepSeek适配器"""
    print("🔧 测试DeepSeek适配器...")
    
    try:
        # 测试基本聊天功能
        response = DeepSeekChatCompletion.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": "Hello, this is a test."}],
            max_tokens=50
        )
        
        print("✅ DeepSeek适配器测试成功!")
        print(f"回复: {response['choices'][0]['message']['content']}")
        return True
        
    except Exception as e:
        print(f"❌ DeepSeek适配器测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    test_deepseek_adapter() 