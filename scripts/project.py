#!/usr/bin/env python3
"""Read-only local Markdown targets and plan/Results pairing."""
import argparse
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

SKIP = {'.git', '.venv', '.envs', '__pycache__', 'node_modules', '99_archived', 'upstream', 'templates', 'scratch'}
LINK = re.compile(r'\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\)')
NUMBERED = re.compile(r'^(\d{2})[_-].+\.md$')


def files(root, includes, excludes):
    for directory, dirs, names in os.walk(root, followlinks=False):
        base = Path(directory)
        dirs[:] = [name for name in dirs if name not in SKIP and not (base/name).is_symlink()
                   and not ((base/name)/'.git').exists()
                   and not any((base/name).is_relative_to(x) for x in excludes)]
        for name in names:
            p=base/name
            if p.suffix=='.md' and not p.is_symlink() and (not includes or any(p.is_relative_to(x) for x in includes)):
                yield p


def check(root, includes=(), excludes=()):
    root=Path(root).resolve(); includes=[root/x for x in includes]; excludes=[root/x for x in excludes]
    errors=[]; count=0
    for p in files(root, includes, excludes):
        fenced=False; comment=False
        for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
            if line.lstrip().startswith(('```','~~~')):
                fenced=not fenced; continue
            if fenced:continue
            clean=''; rest=line
            while rest:
                before,found,after=rest.partition('-->' if comment else '<!--')
                if not comment:clean+=before
                if not found:break
                comment=not comment;rest=after
            for match in LINK.finditer(clean):
                target=match.group(1).strip('<>')
                if urlsplit(target).scheme or target.startswith(('#','//')):continue
                target=unquote(target.split('#',1)[0].split('?',1)[0])
                if not target or any(x in target for x in ('<','>','{{','«')):continue
                count+=1
                if not (p.parent/target).exists():errors.append(f'{p.relative_to(root)}:{n}: missing {target}')
    plan_dir=root/'00_knowledge/02_subplans';result_dir=root/'00_knowledge/03_results'
    pairing=not includes or any(plan_dir.is_relative_to(x) or result_dir.is_relative_to(x) or x.is_relative_to(plan_dir) or x.is_relative_to(result_dir) for x in includes)
    if pairing:
        groups=[]
        for folder in (plan_dir,result_dir):
            group={}
            for p in folder.glob('*.md'):
                m=NUMBERED.match(p.name)
                if not m or p.name=='00_INDEX.md':continue
                if m[1] in group:errors.append(f'duplicate identity {m[1]} in {folder.relative_to(root)}')
                group[m[1]]=p.name
            groups.append(group)
        for key in sorted(groups[0].keys() | groups[1].keys()):
            if groups[0].get(key)!=groups[1].get(key):errors.append(f'plan/Results mismatch {key}: {groups[0].get(key)} / {groups[1].get(key)}')
    return {'links_checked':count,'pairing_checked':pairing,'errors':errors,'scope':'local file targets and plan/Results pairing; no heading-anchor, authorization, evidence or reading-state validation'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',default='.')
    parser.add_argument('--include',action='append',default=[])
    parser.add_argument('--exclude',action='append',default=[])
    parser.add_argument('command',choices=['check'])
    args=parser.parse_args()
    import json
    result=check(args.root,args.include,args.exclude)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return bool(result['errors'])

if __name__=='__main__':raise SystemExit(main())
