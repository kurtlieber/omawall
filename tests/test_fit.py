from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_fit():
    # Mirror Fit.js in Python so the buckets stay testable without QML.
    spec = importlib.util.spec_from_loader("fit_js", loader=None)
    mod = importlib.util.module_from_spec(spec)

    def aspect(w, h):
        if not h:
            return 0
        return w / h

    def bucket(w, h):
        a = aspect(w, h)
        if a >= 2.1:
            return "ultrawide"
        if a >= 1.70:
            return "wide"
        return "laptop"

    def covers(image_w, image_h, screen_w, screen_h):
        return image_w >= screen_w and image_h >= screen_h

    def fits(image_w, image_h, screen_w, screen_h):
        if not covers(image_w, image_h, screen_w, screen_h):
            return False
        screen_bucket = bucket(screen_w, screen_h)
        if screen_bucket == "laptop":
            return True
        return bucket(image_w, image_h) == screen_bucket

    mod.aspect = aspect
    mod.bucket = bucket
    mod.covers = covers
    mod.fits = fits
    return mod


fit = load_fit()

LAPTOP = (2560, 1600)
DESK = (3840, 2160)
TRAVEL = (3840, 1600)


class BucketTests(unittest.TestCase):
    def test_screens(self):
        self.assertEqual(fit.bucket(*LAPTOP), "laptop")
        self.assertEqual(fit.bucket(*DESK), "wide")
        self.assertEqual(fit.bucket(*TRAVEL), "ultrawide")

    def test_images(self):
        self.assertEqual(fit.bucket(3840, 2160), "wide")
        self.assertEqual(fit.bucket(3840, 1600), "ultrawide")
        self.assertEqual(fit.bucket(2560, 1600), "laptop")
        self.assertEqual(fit.bucket(5120, 2160), "ultrawide")


class FitTests(unittest.TestCase):
    def test_1080p_nowhere(self):
        for screen in (LAPTOP, DESK, TRAVEL):
            self.assertFalse(fit.fits(1920, 1080, *screen))

    def test_4k_16x9_laptop_and_desk_not_travel(self):
        self.assertTrue(fit.fits(3840, 2160, *LAPTOP))
        self.assertTrue(fit.fits(3840, 2160, *DESK))
        self.assertFalse(fit.fits(3840, 2160, *TRAVEL))

    def test_ultrawide_laptop_and_travel_not_desk(self):
        self.assertTrue(fit.fits(3840, 1600, *LAPTOP))
        self.assertFalse(fit.fits(3840, 1600, *DESK))
        self.assertTrue(fit.fits(3840, 1600, *TRAVEL))

    def test_laptop_native_not_desk(self):
        self.assertTrue(fit.fits(2560, 1600, *LAPTOP))
        self.assertFalse(fit.fits(2560, 1600, *DESK))
        self.assertFalse(fit.fits(2560, 1600, *TRAVEL))

    def test_3x2_camera_covers_laptop_not_desk_bucket(self):
        self.assertTrue(fit.fits(6000, 4000, *LAPTOP))
        self.assertFalse(fit.fits(6000, 4000, *DESK))
        self.assertFalse(fit.fits(6000, 4000, *TRAVEL))


if __name__ == "__main__":
    unittest.main()
