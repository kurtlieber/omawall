from __future__ import annotations

import json
import subprocess
import unittest
import zlib
from pathlib import Path
from struct import pack

ROOT = Path(__file__).resolve().parents[1]
FIT = ROOT / "bin" / "omawall-fit"


def _png(width: int, height: int) -> bytes:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return pack(">I", len(data)) + tag + data + pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + b"\x00\x00\x00" * width for _ in range(height))
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )


class OmawallFitTests(unittest.TestCase):
    def test_dims_reads_png_without_decoding_pixels(self):
        self.assertIn("-ping", FIT.read_text())
        with self.temporary_png() as path:
            out = subprocess.check_output([str(FIT), "dims", str(path)], text=True)
        data = json.loads(out)
        self.assertEqual(data[str(path)], [4, 3])

    def temporary_png(self):
        import tempfile

        class Ctx:
            def __enter__(self_inner):
                self_inner.tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                self_inner.tmp.write(_png(4, 3))
                self_inner.tmp.close()
                return Path(self_inner.tmp.name)

            def __exit__(self_inner, *exc):
                Path(self_inner.tmp.name).unlink(missing_ok=True)

        return Ctx()


if __name__ == "__main__":
    unittest.main()
