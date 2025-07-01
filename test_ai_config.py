#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI配置测试脚本
用于验证OpenAI API配置是否正确
"""

import os
import sys
from dotenv import load_dotenv

def test_openai_config():
    """测试OpenAI配置"""
    print("🔧 测试OpenAI配置...")
    
    # 加载环境变量
    load_dotenv()
    
    # 检查API密钥
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 错误: 未找到OPENAI_API_KEY")
        return False
    
    if not api_key.startswith('sk-'):
        print("❌ 错误: API密钥格式不正确")
        return False
    
    print(f"✅ API密钥已配置: {api_key[:20]}...")
    
    # 检查模型配置
    model = os.getenv('OPENAI_API_MODEL', 'gpt-4o')
    print(f"✅ 模型配置: {model}")
    
    # 测试API调用
    try:
        import openai
        print(f"✅ OpenAI版本: {openai.__version__}")
        
        # 设置API配置
        openai.api_key = api_key
        openai.api_base = os.getenv('OPENAI_API_URL', 'https://api.openai.com/v1')
        
        # 简单测试调用
        print("🧪 测试API调用...")
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": "Hello, this is a test message."}],
            max_tokens=10
        )
        
        print("✅ API调用成功!")
        return True
        
    except Exception as e:
        print(f"❌ API调用失败: {str(e)}")
        return False

def test_stock_analyzer():
    """测试股票分析器"""
    print("\n📊 测试股票分析器...")
    
    try:
        from stock_analyzer import StockAnalyzer
        
        analyzer = StockAnalyzer()
        print("✅ 股票分析器初始化成功")
        
        # 测试获取股票信息
        stock_info = analyzer.get_stock_info('000001')
        if stock_info:
            print("✅ 股票信息获取成功")
        else:
            print("⚠️ 股票信息获取失败，可能是网络问题")
        
        return True
        
    except Exception as e:
        print(f"❌ 股票分析器测试失败: {str(e)}")
        return False

def main():
    """主函数"""
    print("🚀 开始AI配置测试...\n")
    
    # 测试OpenAI配置
    openai_ok = test_openai_config()
    
    # 测试股票分析器
    analyzer_ok = test_stock_analyzer()
    
    print("\n" + "="*50)
    print("📋 测试结果总结:")
    print(f"OpenAI配置: {'✅ 正常' if openai_ok else '❌ 异常'}")
    print(f"股票分析器: {'✅ 正常' if analyzer_ok else '❌ 异常'}")
    
    if openai_ok and analyzer_ok:
        print("\n🎉 所有测试通过！AI功能已准备就绪。")
        print("💡 您可以访问 http://localhost:8888 开始使用系统。")
    else:
        print("\n⚠️ 部分测试失败，请检查配置。")
    
    return openai_ok and analyzer_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 