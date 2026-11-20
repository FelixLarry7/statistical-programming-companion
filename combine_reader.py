"""Make the single reader ZIP from the two public volumes and verify each member."""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

VOLUMES = ('Reader_Companion_1.zip', 'Reader_Companion_2.zip')


def combine(directory, output):
    expected = dict(line.split('  ', 1)[::-1] for line in (directory / 'sha256.txt').read_text().splitlines())
    manifest_name = 'Statistical_Programming_Reader_Companion/MANIFEST.sha256'
    observed = {}
    manifest = None
    if output.exists():
        raise FileExistsError(output)
    try:
        with ZipFile(output, 'w') as combined:
            for filename in VOLUMES:
                volume = directory / filename
                assert sha256(volume.read_bytes()).hexdigest() == expected[filename], filename
                with ZipFile(volume) as chapter:
                    for item in chapter.infolist():
                        key = PurePosixPath(item.filename)
                        assert key.parts[0] == 'Statistical_Programming_Reader_Companion'
                        assert not key.is_absolute() and '..' not in key.parts
                        assert item.filename not in observed, item.filename
                        raw = chapter.read(item)
                        observed[item.filename] = sha256(raw).hexdigest()
                        if item.filename == manifest_name:
                            manifest = raw.decode()
                        combined.writestr(item, raw)
            assert manifest is not None
            observed.pop(manifest_name)
            member_hashes = dict((f'Statistical_Programming_Reader_Companion/{name}', digest)
                                 for digest, name in (line.split('  ', 1) for line in manifest.splitlines()))
            assert member_hashes == observed
    except Exception:
        output.unlink(missing_ok=True)
        raise
    return len(observed)


if __name__ == '__main__':
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('volumes', type=Path, help='Directory with both public ZIPs and sha256.txt')
    cli.add_argument('output', type=Path)
    args = cli.parse_args()
    print(f'{combine(args.volumes, args.output):,} reader files verified')
