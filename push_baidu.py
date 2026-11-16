# -*- coding: utf-8 -*-
"""百度搜索资源平台 URL 主动推送工具。

令牌只从本地 .workbuddy/baidu_token.txt 读取，绝不写入网站文件或提交到 GitHub。

用法：
    python push_baidu.py                 # 按优先级推送 urls.txt 中尚未推过的链接
    python push_baidu.py --file news-urls.txt   # 指定清单
    python push_baidu.py --limit 5       # 限制本次最多推送条数（当日额度有限时用）
    python push_baidu.py --dry-run       # 只看将要推送什么，不实际请求

推送记录保存在 .workbuddy/baidu_pushed.txt，避免重复推送浪费额度。
"""
import os
import re
import argparse
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://www.guancu.com'
TOKEN_FILE = os.path.join(ROOT, '.workbuddy', 'baidu_token.txt')
HISTORY_FILE = os.path.join(ROOT, '.workbuddy', 'baidu_pushed.txt')
API = 'http://data.zz.baidu.com/urls?site=' + SITE + '&token={token}'


def load_token():
    if not os.path.exists(TOKEN_FILE):
        raise SystemExit('缺少令牌文件：' + TOKEN_FILE)
    token = open(TOKEN_FILE, encoding='utf-8').read().strip()
    if not token:
        raise SystemExit('令牌文件为空')
    return token


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return set()
    return set(x.strip() for x in open(HISTORY_FILE, encoding='utf-8') if x.strip())


def save_history(urls):
    old = load_history()
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        for u in urls:
            if u not in old:
                f.write(u + '\n')


def priority(url):
    """先栏目页、再文章与名片，最后分类与分页；副本页排最后。"""
    p = url.replace(SITE, '')
    if p in ('/', '/index.html'):
        return 0
    if p in ('/about.html', '/services.html', '/companies.html',
             '/news.html', '/contact.html', '/sitemap.html'):
        return 1
    if p.startswith('/news/') and not p.startswith('/news-'):
        return 2
    if p == '/mp/tanxi.html':
        return 3
    if p.startswith('/category/'):
        return 4
    if p.startswith('/mp/'):
        return 6   # mp/index.html 是 canonical 指向 tanxi.html 的副本，不值得占额度
    return 5


def main():
    ap = argparse.ArgumentParser(description='百度 URL 主动推送')
    ap.add_argument('--file', default='urls.txt', help='URL 清单文件，默认 urls.txt')
    ap.add_argument('--limit', type=int, default=0, help='本次最多推送条数，0 表示不限')
    ap.add_argument('--dry-run', action='store_true', help='只预览不推送')
    args = ap.parse_args()

    path = os.path.join(ROOT, args.file)
    if not os.path.exists(path):
        raise SystemExit('找不到清单文件：' + path)
    urls = [x.strip() for x in open(path, encoding='utf-8') if x.strip()]
    order = {u: i for i, u in enumerate(urls)}   # 同组内保持清单原顺序（文章按日期倒序）
    history = load_history()
    todo = sorted((u for u in urls if u not in history),
                  key=lambda u: (priority(u), order[u]))
    if args.limit:
        todo = todo[:args.limit]

    if not todo:
        print('没有需要推送的新链接（全部已推送过）')
        return
    print('本次待推送 %d 条：' % len(todo))
    for u in todo:
        print('  ', u)
    if args.dry_run:
        print('dry-run，未实际推送')
        return

    token = load_token()
    body = ('\n'.join(todo) + '\n').encode('utf-8')
    req = urllib.request.Request(API.format(token=token), data=body,
                                 headers={'Content-Type': 'text/plain'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = resp.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        result = e.read().decode('utf-8', 'replace')
    except Exception as e:
        raise SystemExit('请求失败：' + str(e))

    print('接口返回：', result)
    # 只要接口返回了 success 字段且不是 0，就记入历史，避免重复推送浪费额度
    m = re.search(r'"success"\s*:\s*(\d+)', result)
    if m and int(m.group(1)) > 0:
        save_history(todo)
        print('已将本次链接记入推送记录：', HISTORY_FILE)
    else:
        print('接口未确认成功，本次链接未记入历史，可稍后重试。')
    print('当日剩余额度请以接口返回 remain 为准。')


if __name__ == '__main__':
    main()
