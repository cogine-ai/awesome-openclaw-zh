#!/usr/bin/env python3
"""Build local showcase bundles from an explicit public-file manifest, never a glob."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
MANIFEST = Path(__file__).with_name('bundle-manifest.json')


def read_public_file(root, relative):
    path = PurePosixPath(relative)
    if path.is_absolute() or not path.parts or any(part in ('', '.', '..') for part in relative.split('/')) or '\\' in relative:
        raise ValueError(f'Invalid public path: {relative}')
    target = root.joinpath(*path.parts)
    if any(root.joinpath(*path.parts[:index]).is_symlink() for index in range(1, len(path.parts) + 1)):
        raise ValueError(f'Symlinked public path: {relative}')
    if not target.is_file() or not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Missing public file: {relative}')
    return target.read_bytes()


def member(archive, name, data):
    info = zipfile.ZipInfo(name, (2026, 10, 30, 0, 0, 0))
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, data, compresslevel=9)


def bundle_bytes(root, pack):
    names = pack['files']
    if len(names) != len(set(names)):
        raise ValueError('Duplicate bundle input')
    files = {name: read_public_file(root, name) for name in sorted(names)}
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w') as archive:
        for name, data in files.items():
            member(archive, name, data)
        member(archive, 'BUNDLE-SOURCE.json', json.dumps({
            'files': {name: hashlib.sha256(data).hexdigest() for name, data in files.items()},
        }, ensure_ascii=False, indent=2) + '\n')
        member(archive, 'START-HERE.md', f"# {pack['title']}\n\n教程：`{pack['case']}`。\n\n材料目录包含输入文件、运行脚本和作品。按目录内 START-HERE.md 修改输入并重新生成。\n\n[在线教程](https://www.opcboost.com/{pack['case'].removesuffix('.md')}/) · [案例仓库](https://github.com/cogine-ai/awesome-openclaw-zh) · [Cogine](https://www.cogine.ai/)\n")
    return stream.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    # Resolve every input before writing any bundle.
    output = [(pack['output'], bundle_bytes(ROOT, pack)) for pack in manifest['packs']]
    stale = []
    for relative, data in output:
        path = PurePosixPath(relative)
        if len(path.parts) != 3 or path.parts[:2] != ('assets', 'bundles') or path.suffix != '.zip':
            raise ValueError(f'Invalid bundle target: {relative}')
        target = ROOT.joinpath(*path.parts)
        if target.is_symlink() or target.parent.is_symlink():
            raise ValueError(f'Symlinked bundle target: {relative}')
        if not target.exists() or target.read_bytes() != data:
            if args.check:
                stale.append(relative)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
    if stale:
        raise ValueError('Rebuild bundles: ' + ', '.join(stale))
    print(f'{len(output)} explicit-file bundles ' + ('verified' if args.check else 'built'))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
