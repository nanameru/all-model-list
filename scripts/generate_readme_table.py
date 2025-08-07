#!/usr/bin/env python3
"""
MDファイルからREADME.mdのテーブルを自動生成するスクリプト

使用方法:
    python scripts/generate_readme_table.py

機能:
    - models/providers/**/*.md ファイルをスキャン
    - YAML front matterからメタデータを抽出  
    - ランク順にソートしたテーブルを生成
    - README.mdファイルを更新
"""

import os
import re
import yaml
import glob
from pathlib import Path
from typing import List, Dict, Optional

def parse_model_file(file_path: str) -> Optional[Dict]:
    """
    MDファイルのYAML front matterを解析してメタデータを返す
    
    Args:
        file_path: 解析するMDファイルのパス
        
    Returns:
        メタデータのディクショナリ、エラー時はNone
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # YAML front matterを抽出
        yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            print(f"Warning: YAML front matter not found in {file_path}")
            return None
            
        yaml_content = yaml_match.group(1)
        metadata = yaml.safe_load(yaml_content)
        
        # ファイルパス情報を追加
        metadata['file_path'] = file_path
        
        return metadata
        
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def scan_model_files(base_path: str = "models/providers") -> List[Dict]:
    """
    指定ディレクトリから全てのMDファイルをスキャンしてメタデータを収集
    
    Args:
        base_path: スキャンするベースディレクトリ
        
    Returns:
        モデル情報のリスト
    """
    model_files = []
    pattern = os.path.join(base_path, "**", "*.md")
    
    for file_path in glob.glob(pattern, recursive=True):
        # ディレクトリ内のREADME.mdは除外
        if os.path.basename(file_path).lower() == 'readme.md':
            continue
            
        metadata = parse_model_file(file_path)
        if metadata:
            model_files.append(metadata)
            
    return model_files

def format_price(pricing_info: Dict) -> str:
    """
    価格情報をフォーマットして文字列として返す
    
    Args:
        pricing_info: 価格情報のディクショナリ
        
    Returns:
        フォーマットされた価格文字列
    """
    try:
        if pricing_info.get('free', False):
            return "無料"
            
        input_price = pricing_info.get('input', 0)
        output_price = pricing_info.get('output', 0)
        currency = pricing_info.get('currency', 'USD')
        
        if input_price == 0 and output_price == 0:
            return "無料"
        elif input_price == output_price:
            return f"${input_price:.2f}/M"
        else:
            return f"${input_price:.2f}/${output_price:.2f}/M"
            
    except Exception:
        return "不明"

def generate_table_markdown(models: List[Dict]) -> str:
    """
    モデル情報からMarkdownテーブルを生成
    
    Args:
        models: ソート済みのモデル情報リスト
        
    Returns:
        Markdownテーブルの文字列
    """
    if not models:
        return "| モデル名 | プロバイダー | 価格 | 主要業務カテゴリ | 特徴 |\n|---------|------------|------|-----------------|------|\n| データなし | - | - | - | - |"
        
    table_lines = [
        "| モデル名 | プロバイダー | 価格 | 主要業務カテゴリ | 特徴 |",
        "|---------|------------|------|-----------------|------|"
    ]
    
    for model in models:
        name = model.get('name', '不明')
        provider = model.get('provider', '不明')
        price = format_price(model.get('pricing', {}))
        
        # 主要カテゴリを取得（最大3つ）
        primary_cats = model.get('primary_categories', [])
        if isinstance(primary_cats, list) and primary_cats:
            categories = ', '.join(primary_cats[:3])
            if len(primary_cats) > 3:
                categories += '...'
        else:
            categories = '汎用'
            
        # 特徴を取得（最大2つ）
        features = model.get('features', [])
        if isinstance(features, list) and features:
            feature_str = ', '.join(features[:2])
            if len(features) > 2:
                feature_str += '...'
        else:
            feature_str = '-'
            
        # パイプ文字をエスケープ
        name = name.replace('|', '\\|')
        provider = provider.replace('|', '\\|')
        categories = categories.replace('|', '\\|')
        feature_str = feature_str.replace('|', '\\|')
        
        table_lines.append(f"| {name} | {provider} | {price} | {categories} | {feature_str} |")
    
    return '\n'.join(table_lines)

def update_readme(table_markdown: str, readme_path: str = "README.md") -> bool:
    """
    README.mdファイル内のテーブルを更新
    
    Args:
        table_markdown: 新しいテーブルのMarkdown文字列
        readme_path: README.mdファイルのパス
        
    Returns:
        更新成功時True、失敗時False
    """
    try:
        if not os.path.exists(readme_path):
            print(f"Warning: {readme_path} not found, creating new file")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"""# LLMモデル管理リポジトリ

## モデル一覧

<!-- AUTO_GENERATED_TABLE_START -->
{table_markdown}
<!-- AUTO_GENERATED_TABLE_END -->

## 貢献について

新しいモデル情報の追加や既存情報の更新は、Pull Requestでお願いします。
詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。
""")
            return True
            
        # 既存ファイルの更新
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # テーブル部分を置換
        pattern = r'<!-- AUTO_GENERATED_TABLE_START -->.*?<!-- AUTO_GENERATED_TABLE_END -->'
        replacement = f'<!-- AUTO_GENERATED_TABLE_START -->\n{table_markdown}\n<!-- AUTO_GENERATED_TABLE_END -->'
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # 置換されなかった場合（マーカーが見つからない場合）
        if new_content == content:
            print(f"Warning: Table markers not found in {readme_path}")
            # ファイル末尾にテーブルを追加
            new_content += f"""

## モデル一覧

<!-- AUTO_GENERATED_TABLE_START -->
{table_markdown}
<!-- AUTO_GENERATED_TABLE_END -->
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        return True
        
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")
        return False

def main():
    """メイン処理"""
    print("モデルファイルをスキャンしています...")
    
    # モデルファイルをスキャン
    models = scan_model_files()
    
    if not models:
        print("Warning: モデルファイルが見つかりませんでした")
        return
        
    print(f"見つかったモデル数: {len(models)}")
    
    # ランク順にソート
    models.sort(key=lambda x: x.get('rank', 999))
    
    # テーブル生成
    print("Markdownテーブルを生成しています...")
    table_markdown = generate_table_markdown(models)
    
    # README更新
    print("README.mdを更新しています...")
    if update_readme(table_markdown):
        print("✓ README.mdが正常に更新されました")
        
        # 統計情報の表示
        free_models = len([m for m in models if m.get('pricing', {}).get('free', False)])
        paid_models = len(models) - free_models
        
        print(f"統計: 無料モデル {free_models}個, 有料モデル {paid_models}個")
        
        # プロバイダー別統計
        providers = {}
        for model in models:
            provider = model.get('provider', '不明')
            providers[provider] = providers.get(provider, 0) + 1
            
        print("プロバイダー別:")
        for provider, count in sorted(providers.items()):
            print(f"  {provider}: {count}個")
            
    else:
        print("✗ README.mdの更新に失敗しました")

if __name__ == "__main__":
    main()