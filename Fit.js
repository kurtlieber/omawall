.pragma library

// Aspect buckets for the connected screen, not hardcoded connector names.
// laptop  ~16:10 (1.6)
// wide    ~16:9  (1.778)
// ultrawide 21:9+ / 2.4:1 (>= 2.1)

function aspect(w, h) {
  if (!h) return 0
  return w / h
}

function bucket(w, h) {
  var a = aspect(w, h)
  if (a >= 2.1) return "ultrawide"
  if (a >= 1.70) return "wide"
  return "laptop"
}

function covers(imageW, imageH, screenW, screenH) {
  return imageW >= screenW && imageH >= screenH
}

function fits(imageW, imageH, screenW, screenH) {
  if (!covers(imageW, imageH, screenW, screenH)) return false
  var screenBucket = bucket(screenW, screenH)
  if (screenBucket === "laptop") return true
  return bucket(imageW, imageH) === screenBucket
}

// Omarchy injects publicPluginManifest() into third-party plugins and
// deletes __sourceDir. Resolve the plugin folder from Qt.resolvedUrl(".")
// when the stamp is gone, otherwise identify never runs.
function fileUrlToPath(url) {
  url = String(url || "")
  if (url.indexOf("file://") === 0) url = url.substring(7)
  try { url = decodeURIComponent(url) } catch (e) {}
  return url.replace(/\/$/, "")
}

function pluginDir(manifestSourceDir, resolvedDotUrl) {
  var stamped = String(manifestSourceDir || "").replace(/\/$/, "")
  if (stamped) return stamped
  return fileUrlToPath(resolvedDotUrl)
}

// Empty imageDims must not reject every path: that is a blank desktop.
// A missing path among known measurements is a skip (undecodable / not scanned).
function pathFits(imageDims, path, screenW, screenH) {
  var d = (imageDims && path) ? imageDims[path] : null
  if (!d || d.length < 2) {
    if (!imageDims) return true
    var n = 0
    for (var k in imageDims) { n++; break }
    return n === 0
  }
  return fits(Number(d[0]), Number(d[1]), screenW, screenH)
}
