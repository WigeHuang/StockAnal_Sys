import json
import os
from typing import List, Dict

from news_fetcher import news_fetcher


def get_latest_news_result(
    days: int = 1,
    limit: int = 1000,
    only_important: bool = False,
    news_type: str = "all",
) -> List[Dict]:
    # 基础数据：从 news_fetcher 获取去重后的新闻列表
    news_data = news_fetcher.get_latest_news(days=days, limit=limit)

    # 重要新闻过滤
    if only_important:
        important_keywords = ["重要", "利好", "重磅", "突发", "关注"]
        news_data = [
            news
            for news in news_data
            if any(
                keyword in (news.get("content", "") or "")
                for keyword in important_keywords
            )
        ]

    # 舆情热点过滤
    if news_type == "hotspot":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        hotspot_file = os.path.join(base_dir, "data", "hotspot_keywords.json")
        try:
            with open(hotspot_file, "r", encoding="utf-8") as f:
                hotspot_keywords = json.load(f)
        except Exception:
            hotspot_keywords = []

        def has_keyword(item: Dict) -> bool:
            title = item.get("title", "") or ""
            content = item.get("content", "") or ""
            return any(keyword in title for keyword in hotspot_keywords) or any(
                keyword in content for keyword in hotspot_keywords
            )

        news_data = [news for news in news_data if has_keyword(news)]

    return news_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="获取最新新闻数据")
    parser.add_argument("--days", type=int, default=1, help="向前获取的天数，默认 1 天")
    parser.add_argument("--limit", type=int, default=1000, help="最多返回的新闻条数，默认 1000 条")
    parser.add_argument(
        "--important", action="store_true", help="只返回重要新闻（等同于 important=1）"
    )
    parser.add_argument(
        "--type",
        type=str,
        default="all",
        choices=["all", "hotspot"],
        help="新闻类型：all 或 hotspot，默认 all",
    )

    args = parser.parse_args()

    result = get_latest_news_result(
        days=args.days,
        limit=args.limit,
        only_important=args.important,
        news_type=args.type,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))

