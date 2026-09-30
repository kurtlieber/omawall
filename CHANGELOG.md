# Changelog

## 1.7.0 (klieber fork)

* Timer and wake rotation redeal every workspace Slot on every display, not only the workspaces in view. Before, off-screen workspaces never changed, so rotation looked sporadic.
* `refresh` / `transition` IPC and the theme and background switchers repaint the Slots instead of redealing the visible workspace.
* Auto-rotate defaults to every 30 minutes (was off).
* Accept the stock `background prepare` IPC that `omarchy-theme-set` now calls.
* Skip the transient nameless / FALLBACK screens when dealing Slots.

## 1.6.2 (klieber fork)

* Paint wallpapers again after Omarchy started stripping `__sourceDir` from third-party plugin manifests (Fit never got dimensions, so every Slot stayed empty).
* `identify -ping` for dimension scans so a large Collection does not stall the painter.

## 1.6.1 (klieber fork)

* Empty or missing folder falls back to the theme background instead of a black desktop.

## 1.6.0 (klieber fork)

* Toggle **Different wallpaper per workspace** (Shuffling tab). Off: one picture per display.

## 1.5.0 (klieber fork)

* Per-workspace slots (numbered 1–10) remembered per display across reboot
* Fit filter: no upscale; desk is 16:9, travel is ultrawide, laptop accepts any bucket that covers
* Instant paint (no reveal wipe)
* Default folder `~/source/wallpapers`
* Plugin id `klieber.omawall`

## [1.4.0](https://github.com/matjam/omawall/compare/v1.3.0...v1.4.0) (2026-08-12)


### Bug Fixes

* stop reshuffling when another plugin saves a setting ([39002d2](https://github.com/matjam/omawall/commit/39002d29f849c1a90443f62f79e6cd9fb97c7ebf))

## [1.3.0](https://github.com/matjam/omawall/compare/v1.2.0...v1.3.0) (2026-08-12)


### Features

* next image, and a hover card showing what is coming ([7bd5748](https://github.com/matjam/omawall/commit/7bd5748c26da15f0a29ee4b05e81c1835a2cbb03))

## [1.2.0](https://github.com/matjam/omawall/compare/v1.1.0...v1.2.0) (2026-08-11)


### Features

* add Pixabay as a wallpaper source ([862823e](https://github.com/matjam/omawall/commit/862823e60d30b887238ee627fbf2268c215b9b98))
* per-display single mode and scaling ([ce2f12e](https://github.com/matjam/omawall/commit/ce2f12e00b96a8083d4c0edb73651d91f4abf108))
* tabbed panel with per-display settings ([2102d22](https://github.com/matjam/omawall/commit/2102d224db29988eb1d46a16e74ba8edf6352388))


### Bug Fixes

* stop the advisory CI step from failing the build ([b914eaf](https://github.com/matjam/omawall/commit/b914eaf4bc03e71f235cc53963aa8b08d32af1e7))
* write display settings to the display shown as selected ([191b059](https://github.com/matjam/omawall/commit/191b059bb7bac1599618061c205d7b7c21fe3b2f))
